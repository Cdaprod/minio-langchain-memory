import streamlit as st
from langchain.chat_models import ChatOpenAI
from conversation_handler import ConversationHandler
from minio_integration import MinIOClient
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize MinIO Client
minio_client = MinIOClient(
    endpoint=os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    bucket_name="conversations"
)

# Initialize LangChain Chat Model
chat_model = ChatOpenAI(temperature=0.5)

# Initialize Conversation Handler
conversation_handler = ConversationHandler(chat_model, minio_client)

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

conversation_id = "default_session"  # This could be dynamically generated or user-specific

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    response = conversation_handler.handle_message(conversation_id, input_text)
    st.subheader("The Response is")
    st.write(response)