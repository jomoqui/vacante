import streamlit as st
import numpy as np

st.title("1. Tipo de Trabajo")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Nivel de Reto del Puesto': {
        0: "Tareas predecibles, sin necesidad de adaptación.",
        25: "Requiere algo de iniciativa en situaciones conocidas.",
        50: "Retos equilibrados con recursos disponibles.",
        75: "Entorno exigente, requiere adaptación frecuente.",
        100: "Desafíos constantes, situaciones nuevas y complejas.",
    },
    'Nivel de Habilidad Requerida': {
        0: "Puede ser desempeñado con habilidades básicas.",
        25: "Requiere conocimientos o experiencia general.",
        50: "Se necesita formación técnica específica.",
        75: "Requiere experiencia sólida y competencias avanzadas.",
        100: "Nivel experto, habilidades altamente especializadas.",
    },
}

# Sliders y descripciones
value = st.slider('Nivel de Reto del Puesto', 0, 100, 50, key='Nivel de Reto del Puesto')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Reto del Puesto'], value)}**")
st.session_state['Nivel de Reto del Puesto'] = value

value = st.slider('Nivel de Habilidad Requerida', 0, 100, 50, key='Nivel de Habilidad Requerida')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Habilidad Requerida'], value)}**")
st.session_state['Nivel de Habilidad Requerida'] = value
