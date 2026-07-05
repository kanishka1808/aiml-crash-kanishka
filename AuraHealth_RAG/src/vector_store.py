from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vector_store(chunks, embedding_model):

    print("\nCreating FAISS Vector Store...")

    documents = []

    for chunk in chunks:

        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "source": chunk["source"]
                }
            )
        )

    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    print("FAISS Vector Store Created Successfully!")

    return vector_store