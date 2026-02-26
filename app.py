from rag.loader import load_logs, split_documents
from rag.vectorstore import create_vectorstore
from agent.incident_agent import run_agent


def main():

    # Load logs
    documents = load_logs("data/sample_logs.txt")

    # Split documents
    split_docs = split_documents(documents)

    # Create vector store
    vectorstore = create_vectorstore(split_docs)

    # Retrieve context
    query = "production application crash"
    retrieved_docs = vectorstore.similarity_search(query, k=1)

    if not retrieved_docs:
        print("No relevant logs found.")
        return

    context = retrieved_docs[0].page_content

    # Run AI Agent
    result = run_agent(context)

    print("\n🚨 Severity:", result["severity"])
    print("\n🧠 Analysis:\n", result["analysis"])
    print("\n🛠 Fix:\n", result["fix"])
    print("\n📄 Final Report:\n", result["report"])


if __name__ == "__main__":
    main()