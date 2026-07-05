def retrieve_documents(vector_store, query, k=3):

    print("\nSearching Relevant Documents...")

    results = vector_store.similarity_search(
        query,
        k=k
    )

    print(f"Found {len(results)} Relevant Chunks\n")

    return results