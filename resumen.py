import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Resumen Interactivo de tu Perfil")

# Recolectar los valores guardados
valores = {key: st.session_state[key] for key in st.session_state if isinstance(st.session_state[key], int)}

# Mostrar resumen numérico
if valores:
    st.subheader("📊 Valores seleccionados")
    df = pd.DataFrame(list(valores.items()), columns=["Parámetro", "Valor"])
    st.table(df.sort_values("Parámetro"))

# Mostrar gráfico 3D si hay suficientes valores
if len(valores) >= 3:
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
    st.warning("Aún no se han completado suficientes secciones para generar el gráfico.")