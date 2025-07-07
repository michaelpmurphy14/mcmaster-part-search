import os
from dotenv import load_dotenv
from chromadb import PersistentClient
from openai import OpenAI

# Load environment variables and OpenAI key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Connect to existing ChromaDB collection
chroma_client = PersistentClient(path="data/chroma_db")
collection = chroma_client.get_collection(name="parts")

def search_parts(query: str, n_results: int = 5):
    try:
        # Create embedding for the query
        response = client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        )
        query_embedding = response.data[0].embedding

        # Query ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        # Structure results for return
        matched_parts = []
        for i in range(len(results["ids"][0])):
            meta = results["metadatas"][0][i]
            matched_parts.append({
                "part_number": meta["part_number"],
                "name": meta["name"],
                "description": meta["description"]
            })

        return matched_parts

    except Exception as e:
        print(f"❌ Error during search: {e}")
        return []
