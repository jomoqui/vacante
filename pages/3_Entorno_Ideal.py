import streamlit as st
import numpy as np

st.title("3. Entorno Ideal")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Nivel de Compañerismo': {
        0: "Trabajo completamente individual, sin interacción con otros.",
        25: "Interacciones puntuales sin necesidad de colaboración.",
        50: "Equilibrio entre trabajo autónomo y colaborativo.",
        75: "Participación activa en un equipo con coordinación frecuente.",
        100: "Trabajo diario y constante en equipo, alto nivel de conexión interpersonal.",
    },
    'Nivel de Influencia': {
        0: "Las ideas propias rara vez se consideran.",
        25: "Se escuchan aportaciones, pero el impacto es limitado.",
        50: "Las contribuciones son valoradas de forma equilibrada.",
        75: "Se espera que influya activamente en decisiones del equipo.",
        100: "Alto impacto personal: sus ideas guían el rumbo del equipo o proyecto.",
    },
    'Nivel de Reconocimiento': {
        0: "No busca ni espera reconocimiento externo.",
        25: "Valora reconocimiento puntual, pero no depende de él.",
        50: "Equilibra autovaloración con feedback externo.",
        75: "Se estimula al recibir reconocimiento frecuente.",
        100: "Necesita reconocimiento constante como fuente principal de motivación.",
    },
}

companerismo_slider_value = st.slider('Nivel de Compañerismo', 0, 100, 50, key='companerismo_slider')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Compañerismo'], companerismo_slider_value)}**")
st.session_state['Nivel de Compañerismo'] = companerismo_slider_value

influencia_slider_value = st.slider('Nivel de Influencia', 0, 100, 50, key='influencia_slider')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Influencia'], influencia_slider_value)}**")
st.session_state['Nivel de Influencia'] = influencia_slider_value

reconocimiento_slider_value = st.slider('Nivel de Reconocimiento', 0, 100, 50, key='reconocimiento_slider')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Reconocimiento'], reconocimiento_slider_value)}**")
st.session_state['Nivel de Reconocimiento'] = reconocimiento_slider_value
