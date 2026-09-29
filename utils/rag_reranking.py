from app.rag import RAGService


rag_service = RAGService()


def get_reranked_documents(question):

    documents = rag_service.hybrid_search(
        question
    )

    ranked_documents = rag_service.rerank(
        question,
        documents
    )

    return [
        {
            "score": score,
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for score, doc in ranked_documents
    ]