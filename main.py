import streamlit as st
import datetime as dt
from PIL import Image

st.title('มะนาว')
st.write(' まなお ')

Zeroday = dt.date(year=2021, month=7, day=3)
Today = dt.date.today()
passed=Today-Zeroday

"お迎えした日 : 2021年 7月 4日"
"お迎えしてから今日で ", passed.days, "日目だよ！"

img = Image.open('manao.jpeg')
st.image(img, caption='มะนาว(まなお)氏 0歳',use_column_width=True)

