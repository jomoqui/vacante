import streamlit as st
import numpy as np

st.title("3. Entorno Ideal")

def obtener_desc(diccionario, valor):
    keys = np.array(list(diccionario.keys()))
    closest = keys[np.abs(keys - valor).argmin()]
    return diccionario[closest]

descripciones = {
    'companerismo': {
        0: "Trabajo completamente individual, sin interacción con otros.",
        20: "Interacciones ocasionales, sin necesidad de colaboración.",
        40: "Colaboración esporádica, generalmente trabajo autónomo.",
        60: "Colaboración frecuente en tareas compartidas.",
        80: "Trabajo regular en equipo con alta coordinación.",
        100: "Trabajo diario y constante en equipo, alto nivel de conexión interpersonal."
    },
    'influencia': {
        0: "Las ideas propias rara vez se consideran.",
        20: "A veces se escucha, pero con poco impacto.",
        40: "Las aportaciones son valoradas en ocasiones.",
        60: "Participa activamente y su opinión es tomada en cuenta.",
        80: "Tiene influencia significativa en decisiones del equipo.",
        100: "Alto impacto personal: sus ideas guían el rumbo del equipo o proyecto."
    },
    'reconocimiento': {
        0: "No busca ni espera reconocimiento externo.",
        20: "Valora algo de reconocimiento, sin que sea crucial.",
        40: "Le agrada el reconocimiento ocasional como refuerzo.",
        60: "Se motiva claramente al recibir reconocimiento frecuente.",
        80: "Requiere reconocimiento continuo para mantener su motivación.",
        100: "Necesita reconocimiento constante como fuente principal de motivación."
    }
}

# Sliders ajustados a 6 niveles (step de 20)
valor_companerismo = st.slider("Nivel de Compañerismo", 0, 100, 40, step=20, key="companerismo_slider")
st.markdown(f"**{obtener_desc(descripciones['companerismo'], valor_companerismo)}**")
st.session_state["Nivel de Compañerismo"] = valor_companerismo

valor_influencia = st.slider("Nivel de Influencia", 0, 100, 40, step=20, key="influencia_slider")
st.markdown(f"**{obtener_desc(descripciones['influencia'], valor_influencia)}**")
st.session_state["Nivel de Influencia"] = valor_influencia

valor_reconocimiento = st.slider("Nivel de Reconocimiento", 0, 100, 40, step=20, key="reconocimiento_slider")
st.markdown(f"**{obtener_desc(descripciones['reconocimiento'], valor_reconocimiento)}**")
st.session_state["Nivel de Reconocimiento"] = valor_reconocimiento
