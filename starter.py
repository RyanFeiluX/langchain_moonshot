import os
# from openai import OpenAI
from langchain_moonshot import ChatOpenAI, OpenAIEmbeddings, OpenAIClone
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

api_key = "sk-l6Wg4HFd1uIjU2nlxTonoqVHJ2k8Vz0UXrszBWJoXqqw1N6v"
base_url = "https://api.moonshot.cn/v1"
proxy = "https://10.144.1.10:8080"

os.environ['MOONSHOT_API_KEY'] = api_key
os.environ['MOONSHOT_API_BASE'] = base_url
# os.environ['OPENAI_PROXY'] = proxy

llm = ChatOpenAI(model_name="moonshot-v1-8k")
print('API_BASE: %s' % llm.openai_api_base)
print('PROXY: %s' % llm.openai_proxy)
print('API_KEY: %s' % llm.openai_api_key)
print('Model: %s' % llm.model_name)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chat_chain = prompt | llm | output_parser

# output = chat_chain.invoke({"input": "how can langsmith help with testing?"})
# print(output)

embeddings = OpenAIEmbeddings()

client = OpenAIClone()

file_object = client.files.create(file=Path("README.md"), purpose="file-extract")
file_content = client.files.content(file_id=file_object.id).text
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents([Document(file_content)])

# from langchain_community.vectorstores import FAISS
vector = FAISS.from_documents(documents, embeddings)  # TODO Investigate its logic

# from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based only on the provided context:

    <context>
    {context}
    </context>
    
    Question: {input}
    """
    )

# Create a chain for passing a list of Documents to a model.
document_chain = create_stuff_documents_chain(llm, prompt)  # llm | prompt

# from langchain_core.documents import Document

document_chain.invoke({
    "input": "How can LLM parameter be leveraged efficiently?",
    "context": [Document(page_content="LLM parameters can be helpful.")]
})
