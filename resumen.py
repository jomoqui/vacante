import streamlit as st
import pandas as pd

st.title("Resumen de tus respuestas")

# Recolectar todos los valores numéricos seleccionados
valores = {key: st.session_state[key] for key in st.session_state if isinstance(st.session_state[key], int)}

if valores:
    st.subheader("📊 Valores seleccionados en cada categoría")
    df = pd.DataFrame(list(valores.items()), columns=["Parámetro", "Valor"])
    st.table(df.sort_values("Parámetro"))
else:
    st.info("Aún no se han seleccionado valores.")