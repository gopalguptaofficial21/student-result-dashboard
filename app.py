import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Student Result Analysis Dashboard')

df = pd.read_excel('student_data.xlsx')

df['Total'] = df['Python'] + df['Mathematics'] + df['Electronics']
df['Percentage'] = (df['Total'] / 300) * 100
df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

st.subheader('Student Data')
st.dataframe(df)

st.subheader('Pass and Fail Summary')
result_counts = df['Result'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%', colors=['green','red'])
ax1.set_title('Pass Fail Percentage')
st.pyplot(fig1)

st.subheader('Subject Wise Average Marks')
subject_avg = df[['Python','Mathematics','Electronics']].mean()
fig2, ax2 = plt.subplots()
ax2.bar(subject_avg.index, subject_avg.values, color=['blue','orange','green'])
ax2.set_ylabel('Average Marks')
ax2.set_title('Subject Wise Performance')
st.pyplot(fig2)

st.subheader('Top 5 Students')
top5 = df.nlargest(5, 'Percentage')[['Student Name','Percentage','Result']]
st.dataframe(top5)

st.subheader('Attendance vs Marks')
fig3, ax3 = plt.subplots()
ax3.scatter(df['Attendance'], df['Percentage'], color='purple', s=100)
for i, row in df.iterrows():
    ax3.annotate(row['Student Name'], (row['Attendance'], row['Percentage']))
ax3.set_xlabel('Attendance Percentage')
ax3.set_ylabel('Marks Percentage')
ax3.set_title('Attendance vs Marks')
st.pyplot(fig3)