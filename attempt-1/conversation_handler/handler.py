# conversation_handler.py
from langchain.schema import HumanMessage, AIMessage
from minio_integration import MinIOClient
import os

class ConversationHandler:
    def __init__(self, chat_model, minio_client):
        self.chat_model = chat_model
        self.minio_client = minio_client

    def handle_message(self, conversation_id, message_content):
        # Retrieve previous conversation history, if any
        conversation_history = self.minio_client.retrieve_conversation(conversation_id) or []

        # Append new human message
        conversation_history.append(HumanMessage(content=message_content).dict())

        # Get response from chat model
        response = self.chat_model(conversation_history)

        # Append AI message
        conversation_history.append(AIMessage(content=response.content).dict())

        # Save updated conversation
        self.minio_client.save_conversation(conversation_id, conversation_history)

        return response.content