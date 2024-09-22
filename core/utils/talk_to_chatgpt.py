import json
import requests
import uuid  # Import the uuid module for generating unique keys
import re
import os
import django
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.append(project_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amzfunnel.settings')

# Set the DJANGO_SETTINGS_MODULE to point to the settings modulos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
  # Replace 'your_project_name' with the name of your Django project
django.setup()
from core.models import Items, Urls
from openai import OpenAI
# from docx import Document
from datetime import datetime
from dotenv import load_dotenv
from time import sleep



# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# URL for the ChatGPT API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Your API key for accessing the ChatGPT API

# Request headers including your API key
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {OPENAI_API_KEY}"
# }

# Fetch data from your Django model
amazon_items = Items.objects.first(title='arai')
content = ''
for item in amazon_items:
    content += item.title + ' ' + item.text1 + ' ' + item.text2 + ' ' + item.text3 + ' ' + item.text4 + ' '
    print(item.title)
    sleep(10)

# Concatenate the content from all AmazonItems into a single string
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a blog Writer expert, skilled in marketing a genius of SEO."},
        {"role": "user", "content": f"I Want you make me a blog post about the following articles {content} , the blog post has to be at least 500 words long and SEO optimized. it should also include a catchy title and a featured image. the title has to be quite big also take in mind that i will be just copying and paste so it has to be a finished job with no need of editing. title should have around 60 characters also description has to be around 150 characters long."}
    ]
)
"from now on, I will be your blog writer assistant, skilled in marketing a genius of SEO."
varas = completion.choices[0].message


# print(varas.content)
sections = varas.content.split(':')

# Assuming 'Title' is followed by the actual title, 'Description' is followed by description, and 'Blog Post' is followed by the blog post content
try:
    title_index = sections.index('Title')
    description_index = sections.index('Description')
    blog_post_index = sections.index('Blog Post')

    print('Title:', sections[title_index + 1])
    
except ValueError:
    print('Error: Missing required sections in the response.')

# print(varas)
title_match = re.search(r'Title:\s*(.*)', completion.choices[0].message.content)
title = title_match.group(1).strip() if title_match else None

# Extracting text after "Description:"
description_match = re.search(r'Description:\s*(.*)', completion.choices[0].message.content)
description = description_match.group(1).strip() if description_match else None

start_index = completion.choices[0].message.content.find("Description:") + len("Description:")

# Get the substring starting from the end of the description
rest_of_text = completion.choices[0].message.content[start_index:]

print(rest_of_text)
# Printing extracted title and description
print("Title:", title)
print("Description:", description)

 # Extracting blog post content

def create_paragraph_block(text):
    return {
        '_type': 'block',
        'style': 'normal',
        'children': [{'_type': 'span', 'text': text}]
    }

# Example text content
text_content = rest_of_text

# Split text into paragraphs
paragraphs = text_content.split('\n\n')

# Create block objects for each paragraph
blocks = [create_paragraph_block(paragraph) for paragraph in paragraphs]

# Create block content array
text_blocks = [
    {
        '_key': str(uuid.uuid4()),  # Generate a unique key
        '_type': 'block',
          "children": [
                        {
                        "_key": str(uuid.uuid4()), 
                        "_type": "span",
                        "text": "1. **Smartphone"
                        }
  ],
        'style': 'normal',
        'children': [{'_type': 'span', 'text': paragraph}],
        "markDefs": [] 

    }
    for paragraph in paragraphs
]



# Define your Sanity project ID and dataset name
project_id = 'qgkr9v7j'
dataset = 'production'

# Define your Sanity API token
current_datetime = datetime.now()

# Convert datetime to string using ISO 8601 format
serialized_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S')

print(serialized_datetime)
# Define the content for the draft post
# Define the content for the draft post
draft_content = {
    "mutations": [
        {
            "create": {
                "_type": "post",  # Define the schema type for your document
                '_key': str(uuid.uuid4()),  # Generate a unique key

                "title": title,
                "description": description,

                "publishedAt": serialized_datetime,  # Replace with actual publish date
                "body": text_blocks  # Replace with actual content
            }
        }
    ]
}

# Sanity API endpoint for mutations///////////////////
url = f'https://{project_id}.api.sanity.io/v2021-06-07/data/mutate/{dataset}'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.environ.get("SANITY_API_KEY")}'
}
response = requests.post(url, headers=headers, json=draft_content)

# Check if the request was successful
if response.status_code == 200:
    print('Draft post created successfully.')
else:
    print('Failed to create draft post:', response.content)
# Sanity API endpoint for mutations///////////////////