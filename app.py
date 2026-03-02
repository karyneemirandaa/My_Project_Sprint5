import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("vehicles.csv")

st.header('Histograma de Veículos')
hist_button = st.button('Criar Gráfico de Histograma')

if hist_button:
    st.write('Criando um histograma quando o botão é clicado')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, user_container_width=True)

scatter_button = st.button('Criar Gráfico de Dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão quando o botão é clicado')

    fig = px.scatter(car_data, x='odemeter', y='price')

    st.plotly_chart(fig, user_container_width=True)