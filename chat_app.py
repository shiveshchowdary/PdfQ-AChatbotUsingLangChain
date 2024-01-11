from dotenv import load_dotenv
import os

import streamlit as st 

from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


def main():
    load_dotenv()
    st.set_page_config(page_title='Ask your PDF')
    st.header("Ask Your PDF....")

    pdf = st.file_uploader("Upload your PDF", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n",'\n',' ', ''],
            chunk_size = 400,
            chunk_overlap = 50,
            length_function = len
        )   
        chunks = text_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        chat = ChatOpenAI(
            temperature = 0,
            model = 'gpt-3.5-turbo'
        )
        system = "You are a Helpful assistant who answers questions based on the information user gives you"
        messages = [SystemMessage(content=system)]
        st.title("EchoBot")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt := st.chat_input("Ask a short question about pdf"):
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role":"user","content":prompt})
            question = prompt
            docs = knowledge_base.similarity_search(question)
            context = docs[0].page_content + '\n\n' + docs[1].page_content + '\n\n' + docs[2].page_content + '\n\n' + docs[3].page_content + '\n\n' 
            input = "Answer the question by looking at the context given and make sure that the answer is no more than 150 characters. both context and question are given below\n"
            messages.append(HumanMessage(content = f"{input} CONTEXT : {context} \n QUESTION : {question}"))
            res = chat(messages)
            messages.append(res)
            response = f"echo: {res.content}"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role":"assistant","content":response})

if __name__ == '__main__':
    main()