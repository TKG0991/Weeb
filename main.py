import streamlit as st
#import numpy as np
#import pandas as pd
import datetime as dt
from PIL import Image

st.title('มะนาว')
st.write('まなお')

Firstday = dt.date(year=2021, month=7, day=4)
Today = dt.date.today()
passed=Today-Firstday

"お迎えした日 : ", Firstday
"お迎えしてから ", passed.days, "日たったよ！"
#st.write(passed.strftime("お迎えしてから%Y年%mヶ月%d日"))

img = Image.open('manao.jpeg')
st.image(img, caption='มะนาว(まなお)氏 0歳',use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)
