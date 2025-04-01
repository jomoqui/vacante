import streamlit as st

st.title('7. Seguridad y Proyección')

st.markdown('### Preferencia por Estabilidad')
estabilidad_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='estabilidad_slider')
st.session_state['Preferencia por Estabilidad'] = estabilidad_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se siente cómodo con cambios frecuentes o roles temporales.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tolera cierta inestabilidad si hay aprendizaje.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Busca cierta continuidad sin rigidez.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Valora un entorno estable con proyección.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Necesita seguridad laboral a largo plazo.</div>''', unsafe_allow_html=True)

st.markdown('### Ambición de Posición')
ambicion_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='ambicion_slider')
st.session_state['Ambición de Posición'] = ambicion_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">No le interesa destacar ni subir jerárquicamente.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Está cómodo en roles de soporte o ejecución.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Le interesa avanzar si hay oportunidades claras.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tiene una visión clara de crecimiento.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Aspira a cargos de liderazgo o alta visibilidad.</div>''', unsafe_allow_html=True)