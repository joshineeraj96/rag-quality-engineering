from app.rag import RAGService


rag_service = RAGService()


def generate_answer(question, context):

    return rag_service.generate(
        question,
        context
    )