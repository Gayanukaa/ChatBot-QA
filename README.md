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

## Future Improvements

- Incorporate RAG (Retrieval-Augmented Generation) with Pinecone for domain-specific Q&A.
