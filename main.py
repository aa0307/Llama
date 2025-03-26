# Go to path
# cd D:\GitHub\Llama
# create venv
# python 
# Activate venv
# D:\GitHub\Llama\Llama\Scripts\Activate.ps1

# pip install langchain langchain-community pypdf docarray

# ollama pull znbang/bge:small-en-v1.5-f32
# from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from sys import argv

# 1. Create the model
#llm = ChatOllama(model='llama3.2')
llm = ChatOllama(model='QwQ')
embeddings = OllamaEmbeddings(model='znbang/bge:small-en-v1.5-f32')

# 2. Load the PDF file and create a retriever to be used for providing context
#loader = PyPDFLoader(argv[1])
loader = PyPDFLoader(r"D:\PDF\001_Intro_and_Topic_1.pdf")
pages = loader.load_and_split()
store = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
retriever = store.as_retriever()

# 3. Create the prompt template
template = """
Answer the question based only on the context provided.

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)

def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)

# 4. Build the chain of operations
chain = (
  {
    'context': retriever | format_docs,
    'question': RunnablePassthrough(),
  }
  | prompt
  | llm
  | StrOutputParser()
)

# 5. Start asking questions and getting answers in a loop
while True:
  question = input('What do you want to learn from the document?\n')
  print()
  print(chain.invoke({'question': question}))
  print()
  


# python main.py <PDF_FILE_PATH>

# python main.py <"D:\PDF\001_Intro_and_Topic_1.pdf">