import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y ='b',tooltip=['a','b']
)
st.altair_chart(chart,use_container_width=True)

plt.scatter(data['a'],data['b'])
st.pyplot()

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.graphviz_chart('''
digraph{
    watch -> like
    like -> share
    share -> subscribe
    share -> watch
}
''')

st.graphviz_chart('''
digraph{
    boys -> girls
    girls -> boys
}
''')

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)

st.map()

# st.image("C:/Users/emon1/OneDrive/Desktop/Streamlit Basic/1.jpg", caption='Sunrise by the mountains')

st.video('https://www.youtube.com/watch?v=0KNk-Joi-NM')