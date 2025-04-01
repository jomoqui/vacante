import streamlit as st
import numpy as np

st.title("7. Seguridad y Proyección")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Preferencia por Estabilidad': {
        0: "Se siente cómodo con cambios frecuentes o roles temporales.",
        25: "Tolera cierta inestabilidad si hay aprendizaje.",
        50: "Busca cierta continuidad sin rigidez.",
        75: "Valora un entorno estable con proyección.",
        100: "Necesita seguridad laboral a largo plazo.",
    },
    'Ambición de Posición': {
        0: "No le interesa destacar ni subir jerárquicamente.",
        25: "Está cómodo en roles de soporte o ejecución.",
        50: "Le interesa avanzar si hay oportunidades claras.",
        75: "Tiene una visión clara de crecimiento.",
        100: "Aspira a cargos de liderazgo o alta visibilidad.",
    },
}

estabilidad_slider_value = st.slider('Preferencia por Estabilidad', 0, 100, 50, key='estabilidad_slider')
st.markdown(f"**{obtener_desc(descripciones['Preferencia por Estabilidad'], estabilidad_slider_value)}**")
st.session_state['Preferencia por Estabilidad'] = estabilidad_slider_value

ambicion_slider_value = st.slider('Ambición de Posición', 0, 100, 50, key='ambicion_slider')
st.markdown(f"**{obtener_desc(descripciones['Ambición de Posición'], ambicion_slider_value)}**")
st.session_state['Ambición de Posición'] = ambicion_slider_value