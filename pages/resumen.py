import streamlit as st
import plotly.graph_objects as go

st.title("Resumen Interactivo de tu Perfil")

# Recolectar los valores guardados
puntos = {
    'Compañerismo': st.session_state.get('Nivel de Compañerismo', 50),
    'Influencia': st.session_state.get('Nivel de Influencia', 50),
    'Reconocimiento': st.session_state.get('Nivel de Reconocimiento', 50)
    # Aquí se agregarán los demás parámetros
}

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=[puntos['Compañerismo']],
    y=[puntos['Influencia']],
    z=[puntos['Reconocimiento']],
    mode='markers+text',
    marker=dict(size=10, color='orange'),
    text=["Tu Perfil"],
    name="Tu Perfil"
))

fig.update_layout(
    scene=dict(
        xaxis_title="Compañerismo",
        yaxis_title="Influencia",
        zaxis_title="Reconocimiento"
    ),
    width=800,
    height=600
)

st.plotly_chart(fig)