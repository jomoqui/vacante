import streamlit as st

st.title('3. Entorno Ideal')

st.markdown('### Nivel de Compañerismo')
companerismo_slider_val = st.slider('', 0, 100, 50, step=5, label_visibility='collapsed', key='companerismo_slider')
st.session_state['Nivel de Compañerismo'] = companerismo_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Trabajo completamente individual, sin interacción con otros.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Interacciones puntuales sin necesidad de colaboración.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Equilibrio entre trabajo autónomo y colaborativo.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Participación activa en un equipo con coordinación frecuente.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Trabajo diario y constante en equipo, alto nivel de conexión interpersonal.</div>''', unsafe_allow_html=True)

st.markdown('### Nivel de Influencia')
influencia_slider_val = st.slider('', 0, 100, 50, step=5, label_visibility='collapsed', key='influencia_slider')
st.session_state['Nivel de Influencia'] = influencia_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Las ideas propias rara vez se consideran.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se escuchan aportaciones, pero el impacto es limitado.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Las contribuciones son valoradas de forma equilibrada.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se espera que influya activamente en decisiones del equipo.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Alto impacto personal: sus ideas guían el rumbo del equipo o proyecto.</div>''', unsafe_allow_html=True)

st.markdown('### Nivel de Reconocimiento')
reconocimiento_slider_val = st.slider('', 0, 100, 50, step=5, label_visibility='collapsed', key='reconocimiento_slider')
st.session_state['Nivel de Reconocimiento'] = reconocimiento_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">No busca ni espera reconocimiento externo.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Valora reconocimiento puntual, pero no depende de él.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Equilibra autovaloración con feedback externo.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Se estimula al recibir reconocimiento frecuente.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Necesita reconocimiento constante como fuente principal de motivación.</div>''', unsafe_allow_html=True)

