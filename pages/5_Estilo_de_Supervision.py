import streamlit as st

st.title('5. Estilo de Supervisión')

st.markdown('### Permiso para actuar (Autonomía)')
permiso_autonomia_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='permiso_autonomia_slider')
st.session_state['Permiso para actuar (Autonomía)'] = permiso_autonomia_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Necesita instrucciones claras y seguimiento constante.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Prefiere que le indiquen el camino, con algo de autonomía.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Equilibrio entre guía del líder y libertad personal.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Le gusta tener iniciativa con poco control externo.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Funciona mejor con total libertad para decidir y ejecutar.</div>''', unsafe_allow_html=True)

st.markdown('### Necesidad de consideración personal (Respeto)')
consideracion_respecto_slider_val = st.slider('', 0, 100, 50, step=10, label_visibility='collapsed', key='consideracion_respecto_slider')
st.session_state['Necesidad de consideración personal (Respeto)'] = consideracion_respecto_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">No necesita validación, se motiva por su propio criterio.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Valora cierto reconocimiento del líder, sin dependencia.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Le gusta sentirse valorado sin necesidad constante.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Agradece atención frecuente y feedback personalizado.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Necesita sentirse reconocido y acompañado de forma continua.</div>''', unsafe_allow_html=True)
