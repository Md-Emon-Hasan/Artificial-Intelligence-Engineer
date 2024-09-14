import streamlit as st

st.title('WIDGETS')

# button
st.button("This is button tag")

if st.button('Subscribe'):
    st.write('Like this video too')

# text input
name = st.text_input('Name')
st.write(name)

address = st.text_area('Enter your address')
st.write(address)

# data time input
st.date_input('enter a date')
st.time_input('enter a time')

# st.checkbox('you accept the T&C',value=False)

if st.checkbox('you accept the T&C',value=False):
    st.write('Thank You')

# radio button  
v1 = st.radio('Colors',['R','G','B'],index=0)

# selectbox
v2 = st.selectbox('Colors',['R','G','B'],index=1)

st.write(v1,v2)

# select multiple
v3 = st.multiselect('Colors',['R','G','B'])
st.write(v3)

# selectbox
st.slider('age',min_value=18,max_value=60,value=30,step=2)

# numbers
st.number_input('Numbers')

# uploade a file
img = st.file_uploader('Upload a file')
st.image(img)
