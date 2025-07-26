from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Document_Loaders\\Attention.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100, 
    chunk_overlap = 0, 
    separator = ''
)

result = splitter.split_documents(docs)

print(len(result))
print(result[0])