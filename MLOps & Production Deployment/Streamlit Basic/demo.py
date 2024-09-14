import streamlit as st

st.title('Hello Streamlit')
st.header('Header')
st.subheader('Sub header')

st.text('Like this video and subscribe to this channel')

st.markdown('''
## This is h2 tag
### This is h3 tag
:moon:
:sunglasses:
:heart: 
''')

st.markdown('''
**This is bold text** </br>
__This is italic text__            
''',True)

st.write('Emon Hasan is a machine learning engineer')

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')

d = {
    'name':'Emon',
    'language':'Python',
    'topic':'Data Science'
}
st.write(d)
