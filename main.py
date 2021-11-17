import streamlit as st
import pandas as pd
import datetime as dt
from PIL import Image
from openpyxl import load_workbook


st.title('With MANAO')
st.header('มะนาว') 
'名 : まなお'

"""
###
"""

Startday = dt.date(year=2021, month=7, day=3)
Today = dt.date.today()
passed=Today-Startday

f" \n今日は {Today.strftime(' %Y年 %m月 %d日')} "
f" お迎えして {passed.days} 日目 ！  （ お迎えした日 : 2021年 7月 4日 ）"

img = Image.open('manao.jpeg')
st.image(img, caption='まなちゃん',width=400)


#データベース読み込み
df = pd.read_excel('ham_DB.xlsx',header=0, index_col=0)

#今までのきょり
Accum_Dist = df['メーター'].max()
st.subheader(f'ここまで全部で {Accum_Dist} km 走ったよ ！ ')

if st.checkbox('記録する'):
    Ipt = st.number_input('今の メーター [km]',step=0.001,format="%.3f")
    Memo = st.text_input('メモ欄')
    if st.button("登録！"):
        #記入日の1日前の日付を計算
        Yesterday = Today-dt.timedelta(days=1)
        Whatday = Yesterday.strftime('%a')  
        #1日の距離計算
        Day_Dist = Ipt - Accum_Dist
        #dfに追加
        df.loc[Yesterday.strftime('%Y/%m/%d')] = [str(Whatday), Ipt, Day_Dist, Memo]
        #DB更新
        df.to_excel('ham_DB.xlsx',sheet_name='new')
"""
###
"""
"走った距離の推移"
#グラフ描画
st.bar_chart(df['1日あたり'])
"""
###
"""
if st.checkbox("データ一覧を見る"):
    #欠損を 空欄(スペース) に変換
    df_disp = df.fillna('　')
    st.table(df_disp.sort_values('メーター', ascending=False))


