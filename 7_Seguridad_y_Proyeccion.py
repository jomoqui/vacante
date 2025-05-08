import streamlit as st
import numpy as np

st.title("7. Seguridad y Proyección")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'Preferencia por Estabilidad': {
        0: "Se siente cómodo con cambios constantes o trabajos temporales.",
        20: "Tolera inestabilidad si hay aprendizaje y novedad.",
        40: "Prefiere cierta continuidad sin necesidad de permanencia.",
        60: "Valora estabilidad en un entorno predecible.",
        80: "Busca una trayectoria estable con opciones a futuro.",
        100: "Necesita seguridad laboral duradera y entorno previsible.",
    },
    'Ambición de Posición': {
        0: "No le interesa ascender ni destacar jerárquicamente.",
        20: "Prefiere roles de soporte con baja visibilidad.",
        40: "Se interesa por crecer si hay condiciones claras.",
        60: "Busca progresar y ganar reconocimiento.",
        80: "Tiene metas claras de liderazgo o proyección.",
        100: "Aspira a posiciones de alto liderazgo o gran visibilidad.",
    },
}

# Sliders con paso de 20 para 6 niveles
value_estabilidad = st.slider('Preferencia por Estabilidad', 0, 100, 40, step=20, key='Preferencia por Estabilidad')
st.markdown(f"**{obtener_desc(descripciones['Preferencia por Estabilidad'], value_estabilidad)}**")
st.session_state['Preferencia por Estabilidad'] = value_estabilidad

value_ambicion = st.slider('Ambición de Posición', 0, 100, 40, step=20, key='Ambición de Posición')
st.markdown(f"**{obtener_desc(descripciones['Ambición de Posición'], value_ambicion)}**")
st.session_state['Ambición de Posición'] = value_ambicion
