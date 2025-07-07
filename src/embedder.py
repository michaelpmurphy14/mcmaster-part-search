import os
import pandas as pd
import openai
from chromadb import PersistentClient
from dotenv import load_dotenv

# Start message
print("📦 embedder.py started")

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

openai.api_key = api_key
print("🔑 OpenAI API key loaded.")

# Load parts catalog
csv_path = "data/parts_catalog.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"❌ CSV file not found at: {csv_path}")

df = pd.read_csv(csv_path)
print(f"📄 Loaded {len(df)} parts from catalog.")

# Set up ChromaDB
chroma_client = PersistentClient(path="data/chroma_db")
collection = chroma_client.get_or_create_collection(name="parts")

# Clear old data (optional, uncomment to reset every time)
# collection.delete(where={})

from openai import OpenAI
client = OpenAI(api_key=api_key)

# Embed and store
for i, row in df.iterrows():
    part_id = str(row["part_number"])
    try:
        response = client.embeddings.create(
            input=row["description"],
            model="text-embedding-3-small"
        )
        embedding = response.data[0].embedding

        collection.add(
            documents=[row["description"]],
            embeddings=[embedding],
            metadatas=[{
                "part_number": part_id,
                "name": row["name"],
                "description": row["description"]
            }],
            ids=[part_id]
        )

        print(f"✅ Embedded: {part_id} - {row['name']}")

    except Exception as e:
        print(f"❌ Error embedding {part_id}: {e}")


print("✅ All parts embedded and saved to ChromaDB.")
