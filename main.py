import streamlit as st
import numpy as np
import pandas as pd

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('DataFrame')

df = pd.DataFrame({
  '1列目': [1, 2, 3, 4],
  '2列目': [10, 20, 30, 40]
})
# DataFrameの表示(最大値にハイライト)
st.dataframe(df.style.highlight_max(axis=0))