import streamlit as st
import numpy as np

st.title("6. Salario y Tiempo")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Preferencia Salarial': {
        0: "El salario no es una prioridad, valora más otros factores.",
        25: "Acepta una compensación justa sin expectativas elevadas.",
        50: "Busca un salario competitivo y razonable.",
        75: "Tiene altas expectativas salariales.",
        100: "El salario es clave, espera una retribución alta y constante.",
    },
    'Gestión del Tiempo': {
        0: "Necesita alta flexibilidad y tiempo personal.",
        25: "Prefiere jornadas controladas y tiempo libre.",
        50: "Equilibra carga laboral y flexibilidad.",
        75: "Tolera jornadas largas si hay organización.",
        100: "Está dispuesto a dedicar muchas horas si el rol lo requiere.",
    },
}

# Sliders y descripciones
value = st.slider('Preferencia Salarial', 0, 100, 50, key='Preferencia Salarial')
st.markdown(f"**{obtener_desc(descripciones['Preferencia Salarial'], value)}**")
st.session_state['Preferencia Salarial'] = value

value = st.slider('Gestión del Tiempo', 0, 100, 50, key='Gestión del Tiempo')
st.markdown(f"**{obtener_desc(descripciones['Gestión del Tiempo'], value)}**")
st.session_state['Gestión del Tiempo'] = value
