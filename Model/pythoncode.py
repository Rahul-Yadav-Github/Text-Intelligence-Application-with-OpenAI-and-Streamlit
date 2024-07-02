import os  # Import the OS module
import streamlit as st  # Import the Streamlit module
import pickle  # Import the pickle module
import time  # Import the time module
from langchain_openai import OpenAI  # Import the OpenAI module from langchain
from langchain.chains import RetrievalQAWithSourcesChain  # Import the chain for retrieval-based QA with sources
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Import the text splitter
from langchain_community.document_loaders import UnstructuredURLLoader  # Import the URL loader for unstructured documents
from langchain_community.embeddings import OpenAIEmbeddings  # Import the OpenAI embeddings
from langchain_community.vectorstores import FAISS  # Import the FAISS vector store
from dotenv import load_dotenv  # Import the load_dotenv function from dotenv

# Load environment variables (especially OpenAI API key)
load_dotenv()

st.title("NewsNexus 📈")  # Set the title of the Streamlit app
st.sidebar.title("News Article URLs")  # Set the sidebar title

# Prompt for OpenAI API key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key  # Set the API key in the environment variables

urls = []  # Initialize an empty list to store URLs
for i in range(3):  # Loop to get three URLs from user input
    url = st.sidebar.text_input(f"URL {i+1}")  # Get URL input from the user
    urls.append(url)  # Append the URL to the list

process_url_clicked = st.sidebar.button("Process URLs")  # Button to process URLs
file_path = "faiss_store_openai.pkl"  # File path for saving the FAISS index

main_placeholder = st.empty()  # Placeholder for main text

if api_key:
    llm = OpenAI(api_key=api_key, temperature=0.9, max_tokens=500)  # Initialize the OpenAI LLM with the API key

    if process_url_clicked:  # If the process URLs button is clicked
        loader = UnstructuredURLLoader(urls=urls)  # Load data from URLs
        main_placeholder.text("Data Loading...Started...✅✅✅")  # Display loading message
        data = loader.load()  # Load the data

        text_splitter = RecursiveCharacterTextSplitter(  # Initialize the text splitter
            separators=['\n\n', '\n', '.', ','],  # Separators for splitting text
            chunk_size=1000  # Chunk size
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")  # Display text splitter message
        docs = text_splitter.split_documents(data)  # Split the documents

        embeddings = OpenAIEmbeddings(api_key=api_key)  # Initialize OpenAI embeddings with the API key
        vectorstore_openai = FAISS.from_documents(docs, embeddings)  # Create FAISS vector store from documents
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")  # Display embedding vector message
        time.sleep(2)  # Sleep for 2 seconds

        with open(file_path, "wb") as f:  # Save the FAISS index to a pickle file
            pickle.dump(vectorstore_openai, f)

    query = main_placeholder.text_input("Question: ")  # Get the user's question
    if query:  # If there is a query
        if os.path.exists(file_path):  # Check if the FAISS index file exists
            with open(file_path, "rb") as f:  # Open the FAISS index file
                vectorstore = pickle.load(f)  # Load the vector store
                chain = RetrievalQAWithSourcesChain.from_llm(  # Create the retrieval-based QA chain
                    llm=llm,  # Pass the LLM
                    retriever=vectorstore.as_retriever()  # Pass the vector store as retriever
                )
                result = chain({"question": query}, return_only_outputs=True)  # Get the answer

                st.header("Answer")  # Display the answer header
                st.write(result["answer"])  # Display the answer

                sources = result.get("sources", "")  # Get the sources
                if sources:  # If there are sources
                    st.subheader("Sources:")  # Display the sources header
                    sources_list = sources.split("\n")  # Split the sources by newline
                    for source in sources_list:  # Loop through the sources
                        st.write(source)  # Display each source
else:
    st.warning("Please enter your OpenAI API key to proceed.")
