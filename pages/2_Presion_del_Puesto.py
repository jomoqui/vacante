import streamlit as st

st.title('2. Presión del Puesto')

st.markdown('### Nivel de Reto del Entorno')
reto_entorno_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='reto_entorno_slider')
st.session_state['Nivel de Reto del Entorno'] = reto_entorno_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Entorno muy estable, sin imprevistos.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Cambios puntuales y bajo nivel de exigencia externa.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Retos situacionales manejables, sin desbordar.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Ritmo exigente, con situaciones de presión frecuentes.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Alta presión constante, con urgencias y demandas simultáneas.</div>''', unsafe_allow_html=True)

st.markdown('### Nivel de Habilidad para Manejar Presión')
habilidad_presion_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='habilidad_presion_slider')
st.session_state['Nivel de Habilidad para Manejar Presión'] = habilidad_presion_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Bajo control frente a la presión, necesita condiciones estables.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tolera cierta presión con apoyo y estructura.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se adapta con flexibilidad a entornos moderadamente exigentes.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Maneja con eficacia entornos de alta demanda.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Rinde al máximo bajo presión intensa y continua.</div>''', unsafe_allow_html=True)

