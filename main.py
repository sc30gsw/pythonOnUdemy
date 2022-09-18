import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('Display Image')

# 画像の読み込み
img = Image.open('icon.png')
# 画像の表示
st.image(img, caption='柴犬', use_column_width=False)

df = pd.DataFrame(
  # 2列100行の乱数を生成
  np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
  # 緯度・経度
  columns=['lat', 'lon']
)
# DataFrameの表示(最大値にハイライト)
# st.dataframe(df.style.highlight_max(axis=0))

# 地図の表示
st.map(df)