import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
dframe = pd.read_excel('Datos_Aleatorios.xlsx')

st.title("Data-Frame")
st.dataframe(dframe)
#st.text("Campo de Texto")
st.title("Gráfico de torta")
#st.header("Mi cabecera")
#st.subheader("Mi subcabecera")
#st.code("for i in range(8): print(a)")
if 'Profesión' in dframe.columns:
    profesion_counts = dframe['Profesión'].value_counts()

fig, ax = plt.subplots()
ax.pie(profesion_counts, labels=profesion_counts.index, autopct='%1.1f%%')
ax.set_title('Distribución de Profesiones')
st.pyplot(fig)
