from pathlib import Path

def load_documents():
    """
    Load all .txt documents from the synthetic_data folder.
    """

    # Project root folder
    project_root = Path(__file__).parent.parent

    # Path to synthetic_data
    data_folder = project_root / "synthetic_data"

    # Find all text files
    text_files = list(data_folder.glob("*.txt"))

    print("=" * 50)
    print("AuraHealth Nexus RAG Project")
    print("=" * 50)
    print()

    print(f"Found {len(text_files)} text documents.\n")

    documents = []

    for file in text_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        documents.append(
            {
                "filename": file.name,
                "content": content
            }
        )

        print(f"Loaded: {file.name}")

    print("\nAll documents loaded successfully.")

    return documents