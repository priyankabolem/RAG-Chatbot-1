from dotenv import load_dotenv
import os
from langchain.graphs import Neo4jGraph
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

def run_chatbot(question):
    # Connect to Neo4j
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    # Load existing vector index from Neo4j
    vector_index = Neo4jVector.from_existing_graph(
        embedding=OpenAIEmbeddings(),
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        node_label="Document",  # Replace if your label is different
        embedding_node_property="embedding",
        text_node_properties=["text"]
    )

    # Build the QA chain
    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=vector_index.as_retriever(),
        return_source_documents=False,
    )

    # Run the chatbot
    result = chain.run(question)
    return result
