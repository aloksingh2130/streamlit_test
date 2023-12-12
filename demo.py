import streamlit as st
import time

st.title("Hello Alok")

st.header("Header")

st.subheader("Sub Header")

st.text("This is my first stramlit app")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
** bold **
_ italics _
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

d ={
    "name":"Alok",
    "language":"Python",
    "topic":"Streamlit"
} 
### Display to your web app
st.write(d)

# st.write(st)
st.write("Alok", "Singh")

st.write("# Alok")  # as header

@st.cache_data
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())