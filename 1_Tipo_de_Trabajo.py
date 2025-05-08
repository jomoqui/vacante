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
        20: "Requiere algo de iniciativa en contextos conocidos.",
        40: "Retos moderados con recursos disponibles.",
        60: "Requiere adaptarse a cambios frecuentes.",
        80: "Entorno muy exigente, con presión constante.",
        100: "Desafíos constantes en situaciones nuevas y complejas.",
    },
    'Nivel de Habilidad Requerida': {
        0: "Puede ser desempeñado con habilidades básicas.",
        20: "Requiere conocimientos generales o experiencia previa.",
        40: "Necesita formación técnica o experiencia específica.",
        60: "Competencias avanzadas y experiencia sólida.",
        80: "Requiere dominio especializado en el área.",
        100: "Nivel experto con habilidades altamente especializadas.",
    },
}

# Sliders con step=20 para forzar los 6 niveles
value_reto = st.slider('Nivel de Reto del Puesto', 0, 100, 40, step=20, key='Nivel de Reto del Puesto')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Reto del Puesto'], value_reto)}**")
st.session_state['Nivel de Reto del Puesto'] = value_reto

value_habilidad = st.slider('Nivel de Habilidad Requerida', 0, 100, 40, step=20, key='Nivel de Habilidad Requerida')
st.markdown(f"**{obtener_desc(descripciones['Nivel de Habilidad Requerida'], value_habilidad)}**")
st.session_state['Nivel de Habilidad Requerida'] = value_habilidad
