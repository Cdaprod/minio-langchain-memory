

### Step 1: Import MinIO Client
from minio import Minio
from minio.error import S3Error

### Step 2: Initialize MinIO Client
minioClient = Minio(
    'minio_server_url',
    access_key='minio_access_key',
    secret_key='minio_secret_key',
    secure=True
)

### Step 3: Define MinIO Storage Class
class MinIOStorage:
    def __init__(self, client, bucket_name):
        self.client = client
        self.bucket_name = bucket_name
        # Ensure the bucket exists
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def fetch_memory(self, user_id):
        try:
            data = self.client.get_object(self.bucket_name, f"{user_id}.json")
            memory_data = data.read().decode('utf-8')
            return json.loads(memory_data)
        except S3Error:
            return {}  # Return an empty dict if the file does not exist

    def upsert_memory(self, user_id, memory_data):
        memory_string = json.dumps(memory_data).encode('utf-8')
        self.client.put_object(
            self.bucket_name, 
            f"{user_id}.json", 
            BytesIO(memory_string), 
            len(memory_string),
            content_type='application/json'
        )

### Step 4: Use MinIO Storage in Your Script
if __name__ == "__main__":
    # Initialize MinIO client and storage
    minioClient = Minio(
        'minio_server_url',
        access_key='minio_access_key',
        secret_key='minio_secret_key',
        secure=True
    )
    storage = MinIOStorage(minioClient, 'langchain-memory')

    # Continue with the script as before
    user_id = "user123"
    question = "What's the weather like today?"
    response = simulate_conversation(storage, user_id, question)
    print("Response:", response)

    # Fetch and display updated memory
    updated_memory = storage.fetch_memory(user_id)
    print("Updated Memory:", json.dumps(updated_memory, indent=4))

"""

### Final Notes

This script integrates MinIO for persistent storage of conversational memory, leveraging its S3-compatible API for object storage. Ensure your MinIO server is correctly set up and accessible by this script, and replace placeholders with actual values for your MinIO setup.

This approach allows for scalable and efficient management of conversational contexts, suitable for production-level conversational AI applications.

"""