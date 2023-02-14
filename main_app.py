import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

image = Image.open('./data/horse.jpg')
st.image(image, width=200)