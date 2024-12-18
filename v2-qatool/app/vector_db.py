import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
# PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

pc = Pinecone(api_key=PINECONE_API_KEY)

embeddings = OpenAIEmbeddings(
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
)

def ingest_data():
    """Ingest data from the translated Excel file into Pinecone."""
    file_path = "data/translated_file.csv"
    df = pd.read_csv(file_path)

    print("Columns in CSV file:", df.columns)

    # Prepare data for embedding
    data = []
    for idx, row in df.iterrows():
        for column in df.columns:
            answer = str(row[column]).strip()
            if answer or answer.lower() != "nan":  # Skip empty or NaN cells
                combined_text = f"Q: {column.strip()} A: {answer}"
                data.append({"id": f"{idx}-{column}", "text": combined_text})

    print(f"Processed {len(data)} question-answer pairs for embedding.")

    index = pc.Index(PINECONE_INDEX_NAME)
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT")

    # Embed data and upsert into Pinecone
    vectors = []
    for item in data:
        print(f"Embedding: {item['text']}")
        vector = embeddings.embed_query(item["text"])
        vectors.append((item["id"], vector, {"text": item["text"]}))

    print("Upserting embeddings into Pinecone...")
    index.upsert(vectors)
    print("Data ingestion complete. Embeddings successfully stored in Pinecone.")


if __name__ == "__main__":
    ingest_data()