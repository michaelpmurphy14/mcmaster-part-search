from flask import Flask, request, render_template
from retriever import search_parts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query")
        results = search_parts(query)

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
