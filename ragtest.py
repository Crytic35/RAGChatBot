from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

query = "What is LangGraph?"

results = db.similarity_search(query, k=3)

context = "\n\n".join([doc.page_content for doc in results])

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt = f"""
Answer only using the provided context.
Context: {context}
Question: {query}
"""

response = llm.invoke(prompt)

print("\nANSWER:\n")
print(response.content)