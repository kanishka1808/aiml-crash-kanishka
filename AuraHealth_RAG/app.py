from src.data_loader import load_documents
from src.text_splitter import split_documents
from src.embedding_model import load_embedding_model
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.generator import generate_answer


def main():

    print("=" * 60)
    print("AuraHealth Nexus RAG Chatbot")
    print("=" * 60)

    print("\nLoading documents... Please wait.\n")

    # Step 1: Load Documents
    documents = load_documents()

    # Step 2: Split Documents
    chunks = split_documents(documents)

    # Step 3: Load Embedding Model
    embedding_model = load_embedding_model()

    # Step 4: Create Vector Store
    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    print("\n✅ System Ready!")
    print("Type 'exit' to quit.\n")

    # Conversation Memory
    chat_history = []

    while True:

        query = input("Ask your question: ")

        if query.lower() == "exit":
            print("\nThank you for using AuraHealth Nexus RAG!")
            break

        # Retrieve relevant chunks
        retrieved_docs = retrieve_documents(
            vector_store,
            query,
            k=5
        )

        print("\n" + "=" * 60)
        print("Retrieved Chunks")
        print("=" * 60)

        for i, doc in enumerate(retrieved_docs, 1):

            print(f"\nChunk {i}")
            print(f"Source : {doc.metadata['source']}")
            print("-" * 60)
            print(doc.page_content[:350])
            print("-" * 60)

        # Generate Answer
        answer = generate_answer(
            query,
            retrieved_docs,
            chat_history
        )

        # Save conversation
        chat_history.append({
            "question": query,
            "answer": answer
        })

        print("\n" + "=" * 60)
        print("FINAL ANSWER")
        print("=" * 60)
        print(answer)

        # Display Sources
        sources = sorted(
            set(doc.metadata["source"] for doc in retrieved_docs)
        )

        print("\nSources Used:")

        for source in sources:
            print(f"• {source}")

        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()