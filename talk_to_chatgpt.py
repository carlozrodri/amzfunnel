import base64
import json
from time import sleep
import requests
import uuid  # Import the uuid module for generating unique keys
import re
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amzfunnel.settings')  # Replace 'your_project_name' with the name of your Django project
django.setup()
from core.models import Items, Urls
from openai import OpenAI
# from docx import Document
from datetime import datetime
from dotenv import load_dotenv
from django.contrib.auth.models import User  # Adjust this import as per your Django model
from io import BytesIO



class BlogPostGenerator:
    def __init__(self, project_id=None, dataset=None, openai_api_key=None, sanity_api_key=None):
        # Load environment variables from .env file
        load_dotenv()

        # Fetch required environment variables
        self.project_id = project_id or os.environ.get("project_id")
        self.dataset = dataset or os.environ.get("dataset")
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        self.sanity_api_key = sanity_api_key or os.environ.get("SANITY_API_KEY")

        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.openai_api_key)
    
        def get_asset_from_url(self, url):
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Return a file-like object containing the content
                return BytesIO(response.content)
            else:
                # Raise an error if the request failed
                response.raise_for_status()

        def create_json_payload_with_asset(url):
            # Get the asset from the URL
            asset = get_asset_from_url(url)
            
            # Convert the asset to Base64-encoded string
            encoded_asset = base64.b64encode(asset.read()).decode('utf-8')
            
            # Create a JSON payload
            payload = {
                'filename': url.split('/')[-1],  # Extract filename from URL
                'file_data': encoded_asset
            }
            
            return json.dumps(payload)
        

    def fetch_items_for_blogs(self):
        # Fetch data from your Django model

        amazon_items = Items.objects.all() # Fetch the first item for demonstration purpos
        print(f'Amazon Items: {amazon_items[0]}')

    
        title = amazon_items[0].title
        item_image = amazon_items[0].item_pictures
        # asset = get_asset_from_url(item_image)
        # print(f'Amazon Items: {amazon_items}')
        

        # Concatenate the content from all AmazonItems into a single string
        # content = ' '.join([f"{item.title} {item.text1} {item.text2} {item.text3} {item.text4}" for item in amazon_items])
        return title, item_image

    def generate_blog_post(self, content):
        try:
            # Create completion request to generate blog post
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a blog Writer expert, skilled in marketing a genius of SEO."},
                    {"role": "user", "content": f"I Want you make me a blog post about the following articles {content}, the blog post has to be at least 500 words long and SEO optimized. it should also include a catchy title and a featured image. the title has to be quite big also take in mind that i will be just copying and paste so it has to be a finished job with no need of editing. title should have around 60 characters also description has to be around 150 characters long."}
                ]
            )

            return completion

        except Exception as e:
            print("An error occurred during blog post generation:", e)
            return None

    def extract_blog_post_info(self, completion):
        if completion:
            # Extract sections from the completion
            sections = completion.choices[0].message.content.split(':')

            # Extract title from completion
            title_match = re.search(r'Title:\s*(.*)', completion.choices[0].message.content)
            title = title_match.group(1).strip() if title_match else None

            # Extract description from completion
            description_match = re.search(r'Description:\s*(.*)', completion.choices[0].message.content)
            description = description_match.group(1).strip() if description_match else None

            # Extract rest of the text after description
            start_index = completion.choices[0].message.content.find("Description:") + len("Description:")
            rest_of_text = completion.choices[0].message.content[start_index:]

            return title, description, rest_of_text

        else:
            return None, None, None

    def create_paragraph_blocks(self, text):
        # Split text into paragraphs
        paragraphs = text.split('\n\n')

        # Create block objects for each paragraph
        text_blocks = [
    {
        '_key': str(uuid.uuid4()),  # Generate a unique key for the block
        '_type': 'block',
        'style': 'normal',
        'children': [
            {
                '_key': str(uuid.uuid4()),  # Generate a unique key for the child span
                '_type': 'span',
                'text': paragraph,
                # 'marks': []  # Marks can be empty for plain text
            }
        ],
        'markDefs': []  # Ensure markDefs is present even if empty
    }
    for paragraph in paragraphs]

        return text_blocks
        

    def send_asset(self, asset_url):
        try:
            # Retrieve the asset content from the provided URL
            response = requests.get(asset_url)
            if response.status_code != 200:
                print(f"Failed to retrieve asset from {asset_url}")
                return
            
            # Open image to verify its validity
            try:
                img = open(BytesIO(response.content))
                img.verify()  # Verify image integrity
            except (IOError, SyntaxError) as e:
                print("Invalid image or unsupported format:", e)
                return

            # Prepare the asset for upload
            asset = BytesIO(response.content)
            filename = asset_url.split('/')[-1]

            # Sanity API endpoint for asset uploads
            url = f'https://{self.project_id}.api.sanity.io/v2021-06-07/assets/images/{self.dataset}'

            # Define headers
            headers = {
                'Authorization': f'Bearer {self.sanity_api_key}'
            }

            # Determine Content-Type based on file extension
            content_type = 'image/png'  # Default content type
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                content_type = 'image/jpeg'
            elif filename.lower().endswith('.gif'):
                content_type = 'image/gif'

            # Prepare files for the POST request
            files = {
                'file': (filename, asset, content_type)
            }

            # Send request to upload asset
            response = requests.post(url, headers=headers, files=files)

            # Check if the request was successful
            if response.status_code == 200:
                print('Asset uploaded successfully.')
                # Parse and print the response content (which contains the asset reference)
                print(response.json())
            else:
                print('Failed to upload asset:', response.content)

        except Exception as e:
            print("An error occurred during asset creation:", e)
    def create_draft_post(self, title, description, text_blocks):
        if not all([title, description, text_blocks]):
            print("Cannot create draft post. Missing required information.")
            return

        try:
            # Define draft content
            current_datetime = datetime.now()
            serialized_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S')

            draft_content = {
                "mutations": [
                    {
                        "create": {
                            "_type": "post",  # Define the schema type for your document
                            '_key': str(uuid.uuid4()),  # Generate a unique key
                            "title": title,
                            "description": description,
                            "publishedAt": serialized_datetime,  # Replace with actual publish date
                            "body": text_blocks,
                            # 'markDefs': []   # Replace with actual content
                        }
                    }
                ]
            }

            # Sanity API endpoint for mutations
            url = f'https://{self.project_id}.api.sanity.io/v2021-06-07/data/mutate/{self.dataset}'

            # Define headers
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.sanity_api_key}'
            }

            # Send request to create draft post
            response = requests.post(url, headers=headers, json=draft_content)

            # Check if the request was successful
            if response.status_code == 200:
                print('Draft post created successfully.')
            else:
                print('Failed to create draft post:', response.content)

        except Exception as e:
            print("An error occurred during draft post creation:", e)

# Example usage
if __name__ == "__main__":
    blog_post_generator = BlogPostGenerator()
    content = blog_post_generator.fetch_items_for_blogs()
    completion = blog_post_generator.generate_blog_post(content[0])
    asset_url = content[1]
    print(f'Asset URL: {asset_url}')
    send_asset = blog_post_generator.send_asset(asset_url)
    if completion:
        title, description, rest_of_text = blog_post_generator.extract_blog_post_info(completion)
        text_blocks = blog_post_generator.create_paragraph_blocks(rest_of_text)
        blog_post_generator.create_draft_post(title, description, text_blocks)
