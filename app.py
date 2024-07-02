import os
import streamlit as st
import pickle
import time
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables (especially OpenAI API key)
load_dotenv()

st.title("LLM End-to-End Project Guide 📈")
st.sidebar.title("Data URLs")

# Prompt for OpenAI API key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(api_key=api_key, temperature=0.9, max_tokens=500) if api_key else None

if process_url_clicked and api_key:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Loading data...")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Splitting text...")
    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings(api_key=api_key)
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Building embeddings...")
    time.sleep(2)

    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Ask a question:")
if query and os.path.exists(file_path):
    with open(file_path, "rb") as f:
        vectorstore = pickle.load(f)
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )
        result = chain({"question": query}, return_only_outputs=True)

        st.header("Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            for source in sources.split("\n"):
                st.write(source)
elif not api_key:
    st.warning("Please enter your OpenAI API key to proceed.")
