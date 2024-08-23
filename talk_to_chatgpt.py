import json
import requests
import uuid  # Import the uuid module for generating unique keys
import re
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Replace 'your_project_name' with the name of your Django project
django.setup()
from amazon.models import AmazonItem, Urls
from openai import OpenAI
from docx import Document
from datetime import datetime
from dotenv import load_dotenv
from django.contrib.auth.models import User  # Adjust this import as per your Django model


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

    def fetch_amazon_items_content(self):
        # Fetch data from your Django model
        amazon_items = AmazonItem.objects.all()

        # Concatenate the content from all AmazonItems into a single string
        content = ' '.join([f"{item.title} {item.text1} {item.text2} {item.text3} {item.text4}" for item in amazon_items])
        return content

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
    for paragraph in paragraphs
]

        return text_blocks

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
    content = blog_post_generator.fetch_amazon_items_content()
    completion = blog_post_generator.generate_blog_post(content)
    if completion:
        title, description, rest_of_text = blog_post_generator.extract_blog_post_info(completion)
        text_blocks = blog_post_generator.create_paragraph_blocks(rest_of_text)
        blog_post_generator.create_draft_post(title, description, text_blocks)
