import streamlit as st
import pandas as pd

st.title("Resumen de tus respuestas")

# Mostrar todo el contenido de session_state
if st.session_state:
    st.subheader("🔍 Contenido completo de session_state")
    st.json(st.session_state)

    # Filtrar valores numéricos solamente
    valores = {key: st.session_state[key] for key in st.session_state if isinstance(st.session_state[key], int)}

    if valores:
        st.subheader("📊 Valores seleccionados")
        df = pd.DataFrame(list(valores.items()), columns=["Parámetro", "Valor"])
        st.table(df.sort_values("Parámetro"))
    else:
        st.warning("No se encontraron valores numéricos aún.")
else:
    st.info("session_state está vacío. Asegúrate de haber navegado por las secciones anteriores.")