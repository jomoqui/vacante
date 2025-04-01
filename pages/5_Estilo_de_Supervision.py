import streamlit as st
import numpy as np

st.title("5. Estilo de Supervisión")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Permiso para actuar (Autonomía)': {
        0: "Necesita instrucciones claras y seguimiento constante.",
        25: "Prefiere que le indiquen el camino, con algo de autonomía.",
        50: "Equilibrio entre guía del líder y libertad personal.",
        75: "Le gusta tener iniciativa con poco control externo.",
        100: "Funciona mejor con total libertad para decidir y ejecutar.",
    },
    'Necesidad de consideración personal (Respeto)': {
        0: "No necesita validación, se motiva por su propio criterio.",
        25: "Valora cierto reconocimiento del líder, sin dependencia.",
        50: "Le gusta sentirse valorado sin necesidad constante.",
        75: "Agradece atención frecuente y feedback personalizado.",
        100: "Necesita sentirse reconocido y acompañado de forma continua.",
    },
}

permiso_autonomia_slider_value = st.slider('Permiso para actuar (Autonomía)', 0, 100, 50, key='permiso_autonomia_slider')
st.markdown(f"**{obtener_desc(descripciones['Permiso para actuar (Autonomía)'], permiso_autonomia_slider_value)}**")
st.session_state['Permiso para actuar (Autonomía)'] = permiso_autonomia_slider_value

consideracion_respecto_slider_value = st.slider('Necesidad de consideración personal (Respeto)', 0, 100, 50, key='consideracion_respecto_slider')
st.markdown(f"**{obtener_desc(descripciones['Necesidad de consideración personal (Respeto)'], consideracion_respecto_slider_value)}**")
st.session_state['Necesidad de consideración personal (Respeto)'] = consideracion_respecto_slider_value

