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
        20: "Cambios puntuales con bajo nivel de presión.",
        40: "Exigencia moderada, con retos ocasionales.",
        60: "Frecuencia creciente de presión y cambios.",
        80: "Entorno dinámico con exigencias constantes.",
        100: "Alta presión continua, con urgencias simultáneas.",
    },
    'Nivel de Habilidad para Manejar Presión': {
        0: "Necesita condiciones muy estables para rendir.",
        20: "Tolera cierta presión con apoyo y estructura.",
        40: "Se adapta en entornos con presión moderada.",
        60: "Maneja eficazmente demandas exigentes.",
        80: "Rinde bien en entornos de alta presión.",
        100: "Rinde al máximo bajo presión intensa y constante.",
    },
}

# Sliders con step de 20
value_reto = st.slider('Nivel de Reto del Entorno', 0, 100, 40, step=20, key='Nivel de Reto del Entorno')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Reto del Entorno'], value_reto)}**")
st.session_state['Nivel de Reto del Entorno'] = value_reto

value_habilidad = st.slider('Nivel de Habilidad para Manejar Presión', 0, 100, 40, step=20, key='Nivel de Habilidad para Manejar Presión')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Habilidad para Manejar Presión'], value_habilidad)}**")
st.session_state['Nivel de Habilidad para Manejar Presión'] = value_habilidad
