# NWMSU RAG-Enabled AI Chatbot

** Live Demo:** [https://nwmsu-rag-chatbot.streamlit.app](https://nwmsu-rag-chatbot.streamlit.app)  

An intelligent Q&A chatbot built for Northwest Missouri State University (NWMSU) that uses Retrieval Augmented Generation (RAG) to provide accurate, context aware responses based on structured and unstructured university data.

---

## Features

- Neo4j knowledge graph construction from academic web content  
- Vector similarity search with OpenAI embeddings  
- Hybrid retrieval (graph + unstructured)  
- LangChain LLM pipeline for entity extraction and answer generation  
- Streamlit web UI for interactive Q&A  

---

## Tech Stack

- Python  
- LangChain  
- Neo4j  
- Streamlit  
- OpenAI (GPT-3.5)  
- Google Colab (for development)  

---

## How to Run

1. Clone the repository  
2. Set your environment variables (see `.env.example`)  
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## Project Structure

- `main.py` – RAG pipeline logic  
- `app.py` – Streamlit chatbot frontend  
- `RAG_enabled_NWMSU_Chatbot.ipynb` – Original notebook  
- `requirements.txt` – Dependencies  
- `.env.example` – Example for API and DB config  
- `.gitignore` – To exclude venv, `.env`, and cache  

---

## Deployment Notes

Do **NOT** commit actual API keys. Use `.env` locally or set them securely in Streamlit Cloud.

---

## Project Impact and Takeaways

This project demonstrates:

- Real world implementation of Retrieval Augmented Generation (RAG)  
- Integration of Neo4j Graph Database with LangChain + OpenAI  
- End-to-end deployment on Streamlit Cloud with secure secrets management  
- Debugging of TOML configs, vector retrieval, and knowledge schema mapping  

This project highlights my ability to build and deploy AI solutions end-to-end, and is included in my portfolio to demonstrate real world implementation of machine learning.

---

## License

This project is for academic and demonstration purposes only.  
© 2025 Priyanka Bolem
