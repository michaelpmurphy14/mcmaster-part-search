import os
import pandas as pd
from openai import OpenAI
from chromadb import PersistentClient
from dotenv import load_dotenv

# Load OpenAI API key
print("📦 embedder.py started")
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)
print("🔑 OpenAI API key loaded.")

# Load CSV
csv_path = "data/parts_catalog.csv"
df = pd.read_csv(csv_path)
print(f"📄 Loaded {len(df)} parts from catalog.")

# ChromaDB setup
chroma_client = PersistentClient(path="data/chroma_db")
collection = chroma_client.get_or_create_collection(name="parts")

# Embed and store
for _, row in df.iterrows():
    part_id = str(row["part_number"])
    try:
        response = client.embeddings.create(
            input=row["description"],
            model="text-embedding-3-small"
        )
        embedding = response.data[0].embedding

        metadata = {
            "part_number": part_id,
            "name": row["name"],
            "description": row["description"],
            "category": row.get("category", "Uncategorized")
        }

        collection.add(
            documents=[row["description"]],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[part_id]
        )

        print(f"✅ Embedded: {part_id} - {row['name']}")

    except Exception as e:
        print(f"❌ Error embedding {part_id}: {e}")
