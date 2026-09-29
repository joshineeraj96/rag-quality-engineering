from app.rag import RAGService


rag_service = RAGService()


def get_documents(question, search_type):

    if search_type == "semantic":
        return [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in rag_service.vectorstore.similarity_search(
                question,
                k=4
            )
        ]

    if search_type == "bm25":
        return [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in rag_service.bm25_search(
                question,
                k=4
            )
        ]

    if search_type == "hybrid":
        return [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in rag_service.hybrid_search(
                question
            )
        ]

    raise ValueError(
        f"Unsupported search type: {search_type}"
    )