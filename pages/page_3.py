import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# データ分析関連
df = pd.read_csv('./data/temp.csv', index_col='月')
st.line_chart(df)
st.bar_chart(df['2021年'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021年'])
ax.set_title('matplotlib graph')
st.pyplot(fig)