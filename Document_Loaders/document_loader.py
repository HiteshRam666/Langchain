from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Document_Loaders\\Books",
    glob="*.pdf", 
    loader_cls=PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load() # For many documents

# print(len(docs))
print(docs)