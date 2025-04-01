import streamlit as st

st.title('4. Estilo Cultural')

st.markdown('### Estabilidad vs. Cambio')
estabilidad_cambio_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='estabilidad_cambio_slider')
st.session_state['Estabilidad vs. Cambio'] = estabilidad_cambio_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Entorno muy estructurado, reglas claras, cambios mínimos.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Predomina la estabilidad con pequeños ajustes puntuales.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Equilibrio entre procesos definidos e innovación.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Entorno dinámico, con cambios frecuentes y adaptativos.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Cultura en constante evolución, se espera agilidad y transformación continua.</div>''', unsafe_allow_html=True)

st.markdown('### Independencia vs. Interdependencia')
independencia_interdep_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='independencia_interdep_slider')
st.session_state['Independencia vs. Interdependencia'] = independencia_interdep_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Cultura orientada al logro individual y autonomía total.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Trabajo autónomo con interacción ocasional.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Balance entre responsabilidad personal y cooperación.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se espera coordinación y construcción conjunta de resultados.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Alto nivel de interdependencia, el éxito depende del grupo y la colaboración constante.</div>''', unsafe_allow_html=True)
