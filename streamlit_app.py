pip3 install matplotlib

import streamlit as st
import pandas as pd
import matplotlib

st.set_page_config(page_title="快速基于Dataframe构建数据大屏", layout="wide")
 
file = st.sidebar.file_uploader("请上传csv表格", type=["csv"])
if file is not None:
    df1 = pd.read_csv(file, encoding="gbk")
    column = df1.columns  #获取表头
    df = pd.DataFrame(df1,columns=column)

print(df1)

st.title("深圳翩翩-测试")
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
# React to user input
if prompt := st.chat_input("您的问题是？"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = f"答复: {prompt}"
    # Display assistant response in chat message container
 
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
