import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.sidebar.write("Display Image")

option = st.sidebar.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
"あなたの好きな数字は", option, "です。"

st.sidebar.write("Interactive Widgets")

text = st.sidebar.text_input("あなたの趣味を教えてください。")
"あなたの趣味：", text

condition = st.sidebar.slider("あなたの今の調子は？",0,100,50)
"コンディション：", condition

if st.sidebar.checkbox("Show Image"):
    img = Image.open("DALL·E 2024-01-07 14.37.30 - An image capturing the essence of 'the ultimate bowl of ramen', embodying a moment of culinary perfection. The scene focuses on a single, beautifully .png")
    st.image(img, caption="ra-men", use_column_width=True)