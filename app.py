import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')

modelo = LinearRegression()

x = df[['diametro']]
y = df[['preco']]

modelo.fit(x, y)

st.title('🤖Modelo de Regressão Linear que prevê o preço de uma pizza a partir do diâmetro')
st.divider()
diametro = st.number_input('Digite o tamamnho do diâmetro da pizza (cm): ')

if diametro:
    previsao_preco = modelo.predict([[diametro]])[0][0]
    st.write(f'O preço da pizza de {diametro}cm é R$ {previsao_preco:.2f}')