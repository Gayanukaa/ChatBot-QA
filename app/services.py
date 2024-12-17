import os
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI Chat Model
llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),  # Changed from openai_api_base
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
)


def generate_response(user_input: str) -> str:
    """Generate a response using AzureChatOpenAI."""
    # Create a list of messages for the conversation
    messages = [
        HumanMessage(content=user_input)
    ]

    # Generate a response using the AzureChatOpenAI model
    response = llm(messages)
    return response.content