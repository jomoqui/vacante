import streamlit as st
import numpy as np

st.title("4. Estilo Cultural")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Estabilidad vs. Cambio': {
        0: "Entorno muy estructurado, con reglas claras y cambios mínimos.",
        20: "Estabilidad predominante con ajustes muy puntuales.",
        40: "Procesos definidos con apertura a mejoras ocasionales.",
        60: "Entorno ágil, con cambios frecuentes y gestionados.",
        80: "Cultura dinámica en evolución constante.",
        100: "Transformación continua, alta adaptabilidad y agilidad.",
    },
    'Independencia vs. Interdependencia': {
        0: "Cultura centrada en la autonomía y logros individuales.",
        20: "Mayoritariamente autónoma, con colaboración limitada.",
        40: "Responsabilidad personal combinada con algo de cooperación.",
        60: "Colaboración frecuente y metas compartidas.",
        80: "Trabajo coordinado y alineado en equipo.",
        100: "Éxito colectivo mediante colaboración constante y fuerte interdependencia.",
    },
}

# Sliders con step=20 para 6 niveles
value_estabilidad = st.slider('Estabilidad vs. Cambio', 0, 100, 40, step=20, key='Estabilidad vs. Cambio')
st.markdown(f"**{obtener_desc(descripciones['Estabilidad vs. Cambio'], value_estabilidad)}**")
st.session_state['Estabilidad vs. Cambio'] = value_estabilidad

value_interdependencia = st.slider('Independencia vs. Interdependencia', 0, 100, 40, step=20, key='Independencia vs. Interdependencia')
st.markdown(f"**{obtener_desc(descripciones['Independencia vs. Interdependencia'], value_interdependencia)}**")
st.session_state['Independencia vs. Interdependencia'] = value_interdependencia

value = st.slider('Independencia vs. Interdependencia', 0, 100, 50, key='Independencia vs. Interdependencia')
st.markdown(f"**{obtener_desc(descripciones['Independencia vs. Interdependencia'], value)}**")
st.session_state['Independencia vs. Interdependencia'] = value
