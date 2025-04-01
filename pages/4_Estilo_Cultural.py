import streamlit as st
import numpy as np

st.title("4. Estilo Cultural")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Estabilidad vs. Cambio': {
        0: "Entorno muy estructurado, reglas claras, cambios mínimos.",
        25: "Predomina la estabilidad con pequeños ajustes puntuales.",
        50: "Equilibrio entre procesos definidos e innovación.",
        75: "Entorno dinámico, con cambios frecuentes y adaptativos.",
        100: "Cultura en constante evolución, se espera agilidad y transformación continua.",
    },
    'Independencia vs. Interdependencia': {
        0: "Cultura orientada al logro individual y autonomía total.",
        25: "Trabajo autónomo con interacción ocasional.",
        50: "Balance entre responsabilidad personal y cooperación.",
        75: "Se espera coordinación y construcción conjunta de resultados.",
        100: "Alto nivel de interdependencia, el éxito depende del grupo y la colaboración constante.",
    },
}

estabilidad_cambio_slider_value = st.slider('Estabilidad vs. Cambio', 0, 100, 50, key='estabilidad_cambio_slider')
st.markdown(f"**{obtener_desc(descripciones['Estabilidad vs. Cambio'], estabilidad_cambio_slider_value)}**")
st.session_state['Estabilidad vs. Cambio'] = estabilidad_cambio_slider_value

independencia_interdep_slider_value = st.slider('Independencia vs. Interdependencia', 0, 100, 50, key='independencia_interdep_slider')
st.markdown(f"**{obtener_desc(descripciones['Independencia vs. Interdependencia'], independencia_interdep_slider_value)}**")
st.session_state['Independencia vs. Interdependencia'] = independencia_interdep_slider_value
