import streamlit as st

st.title('6. Salario y Tiempo')

st.markdown('### Preferencia Salarial')
preferencia_salarial_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='preferencia_salarial_slider')
st.session_state['Preferencia Salarial'] = preferencia_salarial_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">El salario no es una prioridad, valora más otros factores.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Acepta una compensación justa sin expectativas elevadas.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Busca un salario competitivo y razonable.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tiene altas expectativas salariales.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">El salario es clave, espera una retribución alta y constante.</div>''', unsafe_allow_html=True)

st.markdown('### Gestión del Tiempo')
gestion_tiempo_slider_val = st.slider('', 0, 100, 50, step=25, label_visibility='collapsed', key='gestion_tiempo_slider')
st.session_state['Gestión del Tiempo'] = gestion_tiempo_slider_val
cols = st.columns(5)
with cols[0]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Necesita alta flexibilidad y tiempo personal.</div>''', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Prefiere jornadas controladas y tiempo libre.</div>''', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Equilibra carga laboral y flexibilidad.</div>''', unsafe_allow_html=True)
with cols[3]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Tolera jornadas largas si hay organización.</div>''', unsafe_allow_html=True)
with cols[4]:
    st.markdown(f'''<div style="padding:10px; background:#f9f9f9; border:1px solid #ddd; border-radius:10px; text-align:center;">Está dispuesto a dedicar muchas horas si el rol lo requiere.</div>''', unsafe_allow_html=True)
