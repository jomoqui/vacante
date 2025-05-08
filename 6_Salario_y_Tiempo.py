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
        20: "Acepta una compensación justa, sin enfocarse en lo económico.",
        40: "Busca una retribución adecuada según su rol.",
        60: "Aspira a un salario competitivo por su desempeño.",
        80: "Tiene expectativas salariales altas y consistentes.",
        100: "El salario es lo principal; busca retribución elevada y constante.",
    },
    'Gestión del Tiempo': {
        0: "Prioriza tiempo personal y alta flexibilidad.",
        20: "Prefiere jornadas predecibles y tiempo libre garantizado.",
        40: "Equilibra bien la carga laboral con flexibilidad.",
        60: "Tolera jornadas intensas si hay organización y propósito.",
        80: "Está dispuesto a trabajar más si es valorado y reconocido.",
        100: "Acepta largas jornadas como parte natural del rol.",
    },
}

# Sliders ajustados con paso de 20
value_salario = st.slider('Preferencia Salarial', 0, 100, 40, step=20, key='Preferencia Salarial')
st.markdown(f"**{obtener_desc(descripciones['Preferencia Salarial'], value_salario)}**")
st.session_state['Preferencia Salarial'] = value_salario

value_tiempo = st.slider('Gestión del Tiempo', 0, 100, 40, step=20, key='Gestión del Tiempo')
st.markdown(f"**{obtener_desc(descripciones['Gestión del Tiempo'], value_tiempo)}**")
st.session_state['Gestión del Tiempo'] = value_tiempo
