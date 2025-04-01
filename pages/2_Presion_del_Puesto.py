import streamlit as st
import numpy as np

st.title("2. Presión del Puesto")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Nivel de Reto del Entorno': {
        0: "Entorno muy estable, sin imprevistos.",
        25: "Cambios puntuales y bajo nivel de exigencia externa.",
        50: "Retos situacionales manejables, sin desbordar.",
        75: "Ritmo exigente, con situaciones de presión frecuentes.",
        100: "Alta presión constante, con urgencias y demandas simultáneas.",
    },
    'Nivel de Habilidad para Manejar Presión': {
        0: "Bajo control frente a la presión, necesita condiciones estables.",
        25: "Tolera cierta presión con apoyo y estructura.",
        50: "Se adapta con flexibilidad a entornos moderadamente exigentes.",
        75: "Maneja con eficacia entornos de alta demanda.",
        100: "Rinde al máximo bajo presión intensa y continua.",
    },
}

reto_entorno_slider_value = st.slider('Nivel de Reto del Entorno', 0, 100, 50, key='reto_entorno_slider')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Reto del Entorno'], reto_entorno_slider_value)}**")
st.session_state['Nivel de Reto del Entorno'] = reto_entorno_slider_value

habilidad_presion_slider_value = st.slider('Nivel de Habilidad para Manejar Presión', 0, 100, 50, key='habilidad_presion_slider')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Habilidad para Manejar Presión'], habilidad_presion_slider_value)}**")
st.session_state['Nivel de Habilidad para Manejar Presión'] = habilidad_presion_slider_value

