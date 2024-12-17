# AI-Powered Chatbot Platform

This project is an AI-powered chatbot using FastAPI, Azure OpenAI, LangChain, and Streamlit for Q&A capabilities.

## Features

- FastAPI for the backend API.
- Streamlit for frontend visualization.
- Azure OpenAI for generating responses.
- LangChain for building conversational pipelines.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Start the backend: `uvicorn app.main:app --reload`.
3. Start the frontend: `streamlit run streamlit_app/app.py`.

## Workflow

1. User inputs a query in Streamlit.
2. Streamlit sends the query to FastAPI.
3. FastAPI calls the LangChain pipeline using Azure OpenAI.
4. The response is sent back to Streamlit and displayed to the user.

## API Endpoints

### `/chat` [POST]

- **Description**: Sends user input to the chatbot and retrieves a response.

- **Request Body**:

  ```json
  {
      "user_input": "Your question here"
  }
  ```
  
## Environment Variables

The following environment variables are required for the chatbot to interact with Azure OpenAI:

- **AZURE_OPENAI_API_KEY**: Your Azure OpenAI API key.
- **AZURE_OPENAI_DEPLOYMENT_NAME**: The deployment name configured in your Azure OpenAI resource.
- **AZURE_OPENAI_ENDPOINT**: The endpoint URL for your Azure OpenAI resource, e.g., `https://<your-resource-name>.openai.azure.com/`.
- **OPENAI_API_VERSION**: The API version, e.g., `2023-06-01-preview`.

## Future Improvements

- Incorporate RAG (Retrieval-Augmented Generation) with Pinecone for domain-specific Q&A.
