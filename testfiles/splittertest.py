from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("documents/ai.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)

chunks = splitter.split_documents(docs)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk.page_content)