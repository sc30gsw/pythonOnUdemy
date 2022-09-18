import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの表示
st.write('Display Image')

# チェックボックスの表示
# チェック時に画像を表示
if st.checkbox('Show Image'):
  # 画像の読み込み
  img = Image.open('icon.png')
  # 画像の表示
  st.image(img, caption='柴犬', use_column_width=False)
