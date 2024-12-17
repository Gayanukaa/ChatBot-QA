import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# embeddings are used to convert text to vectors which are stored in Pinecone and used for similarity search
embeddings = OpenAIEmbeddings(
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
)

def ingest_data():
    """Ingest data from the translated Excel file into Pinecone."""
    file_path = "data/translated_file.xlsx"
    df = pd.read_excel(file_path)

    # Validate data
    if "question" not in df.columns or "answer" not in df.columns:
        raise ValueError("Excel file must have 'question' and 'answer' columns")

    # Step 2: Prepare data for embedding
    data = []
    for _, row in df.iterrows():
        question = row["question"]
        answer = row["answer"]
        combined_text = f"Q: {question} A: {answer}"
        data.append({"id": str(_), "text": combined_text})

    # Step 3: Embed and upload to Pinecone
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(name=PINECONE_INDEX_NAME, dimension=1536)

    index = pinecone.Index(PINECONE_INDEX_NAME)

    for item in data:
        vector = embeddings.embed_query(item["text"])
        index.upsert([(item["id"], vector, {"text": item["text"]})])

    print("Data ingestion complete. Embeddings stored in Pinecone.")

if __name__ == "__main__":
    ingest_data()
