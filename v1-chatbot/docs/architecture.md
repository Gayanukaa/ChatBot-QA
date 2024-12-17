# Architecture Overview

## Components

1. **Backend**: FastAPI serves API endpoints.
2. **Frontend**: Streamlit provides a user-friendly interface.
3. **Azure OpenAI**: Powers the chatbot's conversational capabilities.
4. **LangChain**: Constructs conversational workflows.

## Workflow

1. User inputs a query in Streamlit.
2. Streamlit sends the query to FastAPI.
3. FastAPI calls the LangChain pipeline using Azure OpenAI.
4. The response is sent back to Streamlit and displayed to the user.

![Architecture Diagram](link-to-diagram-if-needed)
