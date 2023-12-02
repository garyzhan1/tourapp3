import streamlit as st
import pandas as pd

st.set_page_config(page_title="快速基于Dataframe构建数据大屏", layout="wide")
 
file = st.sidebar.file_uploader("请上传csv表格", type=["csv"])
if file is not None:
    df1 = pd.read_csv(file, encoding="gbk")
    column = df1.columns  #获取表头
    df = pd.DataFrame(df1, columns=column)
    st.write(df)

data3 = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'gender': ['F', 'M', 'M', 'M'],
        'salary': [50000, 70000, 90000, 110000]}

st.line_chart(data3)
st.bar_chart(data3)
st.area_chart(data3)

data_df = pd.DataFrame(
    {
        "Dow Jones trend": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "Dow Jones trend": st.column_config.LineChartColumn(
            "Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
         ),
    },
    hide_index=True,
)

data = [1,2,3,4,5]
df2 = pd.DataFrame(data)
st.table(df2)
st.table(data)

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
