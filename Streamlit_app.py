import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write("hello wordl !!!")
st.markdown("#### Hello wordl !!!")


df = pd.read_csv("Speed_Dating_Data.csv")
df['age'] = df['age'].apply(pd.to_numeric)
# sns.boxplot(data=df, x=df['age'])
# st.write(plt.title('age'))
# st.write(plt.show())
st.write(sns.boxplot(data=df, x=df['age']))
chart_data = sns.boxplot(data=df, x=df['age'])

st.area_chart(chart_data)

# st.area_chart(df['age'], x="col1", y="col2", color="col3")

fig, ax = plt.subplots()
ax.hist(df['age'], bins=40)
st.pyplot(fig)

st.line_chart(df['age'])
