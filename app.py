import streamlit as st
import warnings

warnings.filterwarnings("ignore")

from ingestion.data_loader import load_data
from rag.qa_system import QASystem
from rag.vector_store import VectorStore


# -------------------------------
# 🔹 Initialize System (cached)
# -------------------------------
@st.cache_resource
def initialize_system():
    data = load_data()   # loads dataset.pkl

    store = VectorStore()
    qa = QASystem(store)

    qa.build_index(data)

    return qa


qa = initialize_system()


# -------------------------------
# 🔹 UI
# -------------------------------
st.title("🧠 AI Knowledge Graph Builder")

st.subheader("💬 Ask Questions")

question = st.text_input("Enter your question:")

if question:
    answer = qa.answer(question)

    st.subheader("📌 Answer:")
    st.success(answer)