from langchain_community.document_loaders import TextLoader

loader = TextLoader("documents/ai.txt")

docs = loader.load()

print(docs)