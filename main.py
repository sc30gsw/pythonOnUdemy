import streamlit as st
import numpy as np
import pandas as pd

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('DataFrame')

df = pd.DataFrame(
  # 3列20行の乱数を生成
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)
# DataFrameの表示(最大値にハイライト)
# st.dataframe(df.style.highlight_max(axis=0))

# 折れ線グラフの表示
st.line_chart(df)