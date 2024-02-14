# From HF_Chat Mistral-8x7B-Instruct-v0.1

Absolutely! To achieve this updated goal, we need two functions – one for storing messages and another for retrieving message histories. We'll create unique file names for each conversation ID.

First, let's install the required packages if needed:
```bash
pip install huggingface_transformers minio
```
Now here's some sample code demonstrating these functions:

```python
import os
import json
from datetime import datetime
from pathlib import Path
import random
import string
from typing import Dict, Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from minio import Minio

def upload_message_history_to_minio(minio_client: Minio, bucket_name: str, conversation_id: str, messages: list):
    """Upload message history to a specified MinIO bucket."""
    
    # Generate a filename based on the conversation_id
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{conversation_id}_{timestamp}.json"

    # Convert messages to JSON format
    data = {"messages": messages}
    data_json = json.dumps(data, indent=4)

    # Upload the JSON content to MinIO
    minio_client.fput_object(bucket_name, filename, data_json)

def download_message_history_from_minio(minio_client: Minio, bucket_name: str, conversation_id: str) -> dict:
    """Download message history given a conversation_id."""
    
    # Create a temporary filename
    temp_filename = f"./{os.urandom(10).hex()}.json"

    # List all objects in the bucket
    objects = minio_client.list_objects(bucket_name)

    for obj in objects:
        # Find the object matching the provided conversation_id
        if obj.object_name.startswith(f"{conversation_id}_"):
            # Download the object to a local file
            minio_client.fget_object(bucket_name, obj.object_name, temp_filename)
            break

    else:
        print(f"No object found for conversation_id '{conversation_id}'.")
        return {}

    # Read the contents of the downloaded file
    with open(temp_filename, "r") as file:
        file_content = file.read()

    # Remove the temporary file
    Path(temp_filename).unlink()

    try:
        # Parse the JSON contents
        data = json.loads(file_content)
        
        # Extract messages and remove unnecessary wrapping
        messages = data["messages"]

    except Exception as e:
        print(f"Error parsing JSON data: {e}")
        messages = []

    finally:
        return {"messages": messages}
```
These helper functions allow you to save and load message histories associated with specific conversations using a randomly generated conversation\_id. You just need to initialize a MinIO client with valid connection details and call these functions accordingly. For instance:

```python
# Set up a MinIO client
minio_client = Minio('your-minio-endpoint',
                      access_key='your-access-key',
                      secret_key='your-secret-key')

# Store a new conversation
conversation_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
sample_messages = [{'role': 'user', 'content': 'Hello there!'}, {'role': 'assistant', 'content': 'Hi! How can I assist you today?'}]
upload_message_history_to_minio(minio_client, 'conversations', conversation_id, sample_messages)

# Retrieve an existing conversation
retrieved_messages = download_message_history_from_minio(minio_client, 'conversations', conversation_id)
for msg in retrieved_messages['messages']:
    print(msg)
```
Remember to change the endpoint, access\_key, and secret\_key with your actual MinIO server information.