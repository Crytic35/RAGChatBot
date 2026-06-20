from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

results = db.similarity_search("What is LangGraph?", k=3)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc.page_content)