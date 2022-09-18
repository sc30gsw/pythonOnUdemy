import streamlit as st
import numpy as np
import pandas as pd

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('DataFrame')

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