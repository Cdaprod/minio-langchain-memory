# minio_integration.py
from minio import Minio
from minio.error import S3Error
import json

class MinIOClient:
    def __init__(self, endpoint, access_key, secret_key, bucket_name):
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)
        self.bucket_name = bucket_name
        self.ensure_bucket()

    def ensure_bucket(self):
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def save_conversation(self, conversation_id, conversation_data):
        try:
            self.client.put_object(
                self.bucket_name,
                f"{conversation_id}.json",
                data=json.dumps(conversation_data, ensure_ascii=False).encode('utf-8'),
                length=len(json.dumps(conversation_data, ensure_ascii=False).encode('utf-8')),
                content_type="application/json"
            )
        except S3Error as exc:
            print(f"Error occurred: {exc}")

    def retrieve_conversation(self, conversation_id):
        try:
            response = self.client.get_object(self.bucket_name, f"{conversation_id}.json")
            conversation_data = json.loads(response.read().decode('utf-8'))
            return conversation_data
        except S3Error as exc:
            print(f"Error occurred: {exc}")
            return None