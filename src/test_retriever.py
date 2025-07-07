from retriever import search_parts

# Sample query
query = "heat-resistant tubing 1/2 inch"

# Call the search function
results = search_parts(query)

# Print formatted results
print(f"\n🔍 Top results for query: \"{query}\"\n")
for r in results:
    print(f"{r['name']} (Part #{r['part_number']}): {r['description']}")
