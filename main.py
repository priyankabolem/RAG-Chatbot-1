import os
from langchain.graphs import Neo4jGraph
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings import OpenAIEmbeddings

def run_chatbot(question):
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    vector_index = Neo4jVector.from_existing_graph(
        embedding=OpenAIEmbeddings(),
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=vector_index.as_retriever(),
        return_source_documents=False,
    )

    result = chain.run(question)
    return result
