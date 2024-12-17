import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Retrieve environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Initialize Pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings(
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
)

def ingest_data():
    """Ingest data from the translated Excel file into Pinecone."""
    # Step 1: Read the Excel file
    file_path = r"C:\Users\GayanukaAmarasuriya\OneDrive - BCS TECHNOLOGY INTERNATIONAL PTY LIMITED\Repositories\ChatBot-QA\v2-qatool\data\translated_file.xlsx"

    df = pd.read_excel(file_path)

    # Step 2: Restructure data into 'question-answer' pairs
    data = []
    for idx, row in df.iterrows():
        for column in df.columns:
            question = column.strip()  # Question from the column header
            answer = str(row[column]).strip()  # Corresponding answer from the row
            if answer and answer != "nan":  # Skip empty or NaN answers
                combined_text = f"Q: {question} A: {answer}"
                data.append({"id": f"{idx}-{column}", "text": combined_text})

    # Step 3: Create Pinecone index if it doesn't exist
    existing_indexes = pc.list_indexes().names()
    if PINECONE_INDEX_NAME not in existing_indexes:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,  # Embedding dimension for OpenAI models
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region=PINECONE_ENVIRONMENT
            )
        )
    index = pc.Index(PINECONE_INDEX_NAME)

    # Step 4: Embed and upload data to Pinecone
    vectors = []
    for item in data:
        vector = embeddings.embed_query(item["text"])
        vectors.append((item["id"], vector, {"text": item["text"]}))

    # Upload to Pinecone
    index.upsert(vectors)
    print("Data ingestion complete. Embeddings stored in Pinecone.")

if __name__ == "__main__":
    ingest_data()