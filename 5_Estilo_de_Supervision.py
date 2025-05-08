import streamlit as st
import numpy as np

st.title("5. Estilo de Supervisión")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Permiso para actuar (Autonomía)': {
        0: "Necesita instrucciones claras y supervisión constante.",
        20: "Prefiere orientación precisa antes de actuar.",
        40: "Trabaja bien con cierta libertad bajo una estructura definida.",
        60: "Se siente cómodo tomando decisiones propias con poco control.",
        80: "Busca independencia para decidir y actuar.",
        100: "Prefiere total libertad para ejecutar con criterio propio.",
    },
    'Necesidad de consideración personal (Respeto)': {
        0: "Se guía por su propio criterio, sin necesidad de validación.",
        20: "Aprecia algo de reconocimiento ocasional del líder.",
        40: "Valora sentirse tenido en cuenta sin necesidad constante.",
        60: "Agradece atención frecuente y comunicación personalizada.",
        80: "Requiere presencia cercana del líder y apoyo emocional.",
        100: "Necesita sentirse constantemente acompañado y valorado.",
    },
}

# Sliders con valores en múltiplos de 20
value_autonomia = st.slider('Permiso para actuar (Autonomía)', 0, 100, 40, step=20, key='Permiso para actuar (Autonomía)')
st.markdown(f"**{obtener_desc(descripciones['Permiso para actuar (Autonomía)'], value_autonomia)}**")
st.session_state['Permiso para actuar (Autonomía)'] = value_autonomia

value_respeto = st.slider('Necesidad de consideración personal (Respeto)', 0, 100, 40, step=20, key='Necesidad de consideración personal (Respeto)')
st.markdown(f"**{obtener_desc(descripciones['Necesidad de consideración personal (Respeto)'], value_respeto)}**")
st.session_state['Necesidad de consideración personal (Respeto)'] = value_respeto
