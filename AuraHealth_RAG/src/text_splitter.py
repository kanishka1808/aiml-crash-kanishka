from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for document in documents:

        chunks = splitter.split_text(document["content"])

        for chunk in chunks:

            all_chunks.append({
                "source": document["filename"],
                "content": chunk
            })

    print("\nChunking Completed")
    print(f"Total Chunks Created : {len(all_chunks)}")

    return all_chunks