from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

vector = embeddings.embed_query("What is LangChain?")
# Checking if my embedding model can convert text into a vector.

print(vector)