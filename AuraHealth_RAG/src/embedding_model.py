from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():

    print("\nLoading Embedding Model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embedding Model Loaded Successfully!")

    return embeddings