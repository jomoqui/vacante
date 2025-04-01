import streamlit as st

st.title('1. Tipo de Trabajo')

st.markdown('### Nivel de Reto del Puesto')
reto_puesto_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='reto_puesto_slider')
st.session_state['Nivel de Reto del Puesto'] = reto_puesto_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tareas predecibles, sin necesidad de adaptación.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Requiere algo de iniciativa en situaciones conocidas.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Retos equilibrados con recursos disponibles.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Entorno exigente, requiere adaptación frecuente.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Desafíos constantes, situaciones nuevas y complejas.</div>''', unsafe_allow_html=True)

st.markdown('### Nivel de Habilidad Requerida')
habilidad_puesto_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='habilidad_puesto_slider')
st.session_state['Nivel de Habilidad Requerida'] = habilidad_puesto_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Puede ser desempeñado con habilidades básicas.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Requiere conocimientos o experiencia general.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se necesita formación técnica específica.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Requiere experiencia sólida y competencias avanzadas.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Nivel experto, habilidades altamente especializadas.</div>''', unsafe_allow_html=True)
