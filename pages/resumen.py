import streamlit as st
import plotly.graph_objects as go

st.title("Resumen Interactivo de tu Perfil")

# Recolectar los valores guardados
valores = {}
for key in st.session_state:
    valores[key] = st.session_state[key]

if len(valores) >= 3:
    # Selección arbitraria de 3 dimensiones para visualización 3D
    keys = list(valores.keys())
    x = valores[keys[0]]
    y = valores[keys[1]]
    z = valores[keys[2]]

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=[x], y=[y], z=[z],
        mode='markers+text',
        marker=dict(size=10, color='orange'),
        text=["Tu Perfil"],
        name="Tu Perfil"
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title=keys[0],
            yaxis_title=keys[1],
            zaxis_title=keys[2]
        ),
        width=800,
        height=600
    )

    st.plotly_chart(fig)
else:
    st.warning("Aún no se han completado suficientes secciones para generar el resumen.")