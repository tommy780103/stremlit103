import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プレグレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

st.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("お問い合わせ１")
expander1.write("お問い合わせ１の回答")
expander2 = st.expander("お問い合わせ２")
expander2.write("お問い合わせ２の回答")

#option = st.selectbox(
#    "あなたが好きな数字を教えてください",
#    list(range(1,11))
#)
#"あなたの好きな数字は", option, "です。"

#st.write("Interactive Widgets")

#text = st.text_input("あなたの趣味を教えてください。")
#"あなたの趣味：", text

#condition = st.slider("あなたの今の調子は？",0,100,50)
#"コンディション：", condition

#st.write("Display Image")
#if st.sidebar.checkbox("Show Image"):
#    img = Image.open("DALL·E 2024-01-07 14.37.30 - An image capturing the essence of 'the ultimate bowl of ramen', embodying a moment of culinary perfection. The scene focuses on a single, beautifully .png")
#    st.image(img, caption="ra-men", use_column_width=True)