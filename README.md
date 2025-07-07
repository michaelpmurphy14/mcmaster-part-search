# 🧠 McMaster-Carr Semantic Part Search

This project is a natural-language search tool for a simulated McMaster-Carr industrial parts catalog. It uses OpenAI embeddings and a local vector database (ChromaDB) to let users search by description instead of part number or strict keywords.

Built with:
- 🔍 OpenAI's `text-embedding-3-small`
- 🗂️ ChromaDB for local semantic search
- 🌐 Flask for the web interface

---

## ⚠️ Why Not Use McMaster-Carr’s Real Catalog?

McMaster-Carr's [Terms of Use](https://www.mcmaster.com/) prohibit scraping or reusing content from their live site without permission.

To respect that, this project uses **a small, fictional sample catalog** based on typical part types (e.g., bolts, tubing, fittings). It simulates how a semantic search system could enhance customer experience without using their proprietary data.

---

## 🛠️ Features

- Search by description (e.g., “heat-resistant tubing”)
- Uses OpenAI embeddings to understand meaning, not just keywords
- Stores embeddings locally with ChromaDB
- Clean Flask frontend to demo functionality

---

## 🚀 Project Roadmap

### ✅ Phase 1 — MVP (complete)
- [x] Create mock part catalog (`parts_catalog.csv`)
- [x] Build embedding pipeline with OpenAI API
- [x] Store and query vectors using ChromaDB
- [x] Develop Flask UI for query input and result display
- [x] Connect retriever to web interface

### 🧭 Phase 2 — Planned Enhancements
- [ ] Add CSS styling for product cards
- [ ] Add metadata filters (e.g. category, material, thread size)
- [ ] Integrate a download/export option (PDF spec sheet or JSON API)
- [ ] Simulate price + stock status for realism
- [ ] Deploy to Fly.io or Render for public access
- [ ] Replace OpenAI with a local model (`sentence-transformers`) for offline use

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/michaelpmurphy14/mcmaster-part-search.git
cd mcmaster-part-search
```
### 2. Set up environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Add your OpenAI API key
Create a .env file in the root:
```bash
OPENAI_API_KEY=sk-...
```
### 4. Embed the product catalog
```bash
python src/embedder.py
```
### 5. Run the web app
```bash
python src/app.py
```
Open your browser to: http://localhost:5000

## 🧪 Example Queries
Try queries like:

- get me some tubes
- 1/4 inch vibration-resistant fasteners
- brass elbow for compression fittings
- clear flexible plastic for liquid transport

## 📁 File Structure
```bash
mcmaster-part-search/
├── data/
│   └── parts_catalog.csv
├── src/
│   ├── app.py
│   ├── embedder.py
│   ├── retriever.py
│   └── test_retriever.py
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧠 Why This Matters
McMaster-Carr is known for its massive product catalog. Helping customers find the right part faster — using semantic understanding — could eliminate friction in ordering and reduce costly support cycles. This project shows what that might look like in practice.

## 📬 Questions or Feedback?
This is a demo project built for portfolio/interview purposes. If you'd like to see additional functionality or collaborate on related tools, feel free to reach out.

