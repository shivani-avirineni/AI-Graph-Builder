import streamlit as st
from ingestion.data_loader import load_data
from rag.qa_system import QASystem
from rag.vector_store import VectorStore

st.title("🧠 AI Knowledge Graph Builder")

# -----------------------------
# Load Dataset
# -----------------------------
data = load_data("data/dataset.pkl")

# -----------------------------
# Clean Dataset
# -----------------------------
cleaned_data = []
for text in data:
    text = text.replace("{product_purchased}", "product")
    cleaned_data.append(text)

# -----------------------------
# Initialize RAG
# -----------------------------
vector_store = VectorStore()
qa = QASystem(vector_store)

# Build index
qa.build_index(cleaned_data)

# -----------------------------
# UI
# -----------------------------
st.subheader("📄 Data Preview")

for d in cleaned_data[:5]:
    st.write(d)

st.subheader("🤖 Ask Questions")

query = st.text_input("Enter your question:")

if query:
    answer = qa.answer(query)

    st.subheader("📌 Answer:")
    st.write(answer)