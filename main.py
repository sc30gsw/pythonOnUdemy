import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('Interactive Widgets')

# チェックボックスの表示
# チェック時に画像を表示
# if st.checkbox('Show Image'):
  # 画像の読み込み
  # img = Image.open('icon.png')
  # 画像の表示
  # st.image(img, caption='柴犬', use_column_width=False)

# セレクトボックスの表示
# option = st.selectbox(
#   'あなたが好きな数字を教えてください。',
#   list(range(1, 11))
# )
# セレクトしたものを表示
# 'あなたの好きな数字は、', option, 'です。'

# テキストボックスの表示
# text= st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味:', text

# スライダーの表示
condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション:', condition