from sentence_transformers import SentenceTransformer

class QASystem:
    def __init__(self, vector_store):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.store = vector_store

    def build_index(self, texts):
        embeddings = self.model.encode(texts)
        self.store.add(embeddings, texts)

    def answer(self, query):
        query_embedding = self.model.encode([query])
        results = self.store.search(query_embedding, k=3)

        context = " ".join(results)

        query_lower = query.lower()

        if "what" in query_lower or "issues" in query_lower:
            return context
        elif "why" in query_lower:
            return context
        else:
            return f"Based on data: {context}"