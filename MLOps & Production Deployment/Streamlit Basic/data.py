import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))

dic = {
    'name':'Emon',
    'age':22,
    'city':'Dhaka'
}

data = pd.read_csv("C:/Users/emon1/OneDrive/Desktop/Streamlit Basic/Salary_Data.csv")
# print(data)
st.dataframe(a)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data,width=100,height=500)

st.table(a)
st.table(data)

st.json(dic)

st.write(a)

@st.cache
def ret_time():
    time.sleep(5)
    return time.time()
if st.checkbox('1'):
    st.write(ret_time())
if st.checkbox('2'):
    st.write(ret_time())
