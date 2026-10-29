import streamlit as st
from irribio.model import FEATURES,get_model,recommendation

st.set_page_config(page_title='IRRIBIO | Prototype',page_icon='🌱')
st.title('IRRIBIO — Smart Irrigation Demonstration')
st.warning('Synthetic data and demonstration model. Not calibrated or validated for real farms.')
st.write('Explore how soil conditions and an illustrative microbial-activity index can be inputs to moisture estimation.')
micro=st.slider('Microbial activity index (illustrative, 0–100)',0.,100.,55.)
temp=st.slider('Soil temperature (°C)',15.,42.,27.)
humidity=st.slider('Relative humidity (%)',20.,95.,65.)
rain=st.slider('Recent rainfall (mm)',0.,25.,5.)
prev=st.slider('Previous moisture (%)',10.,80.,43.)
if st.button('Predict simulated moisture'):
    result=float(get_model().predict([[micro,temp,humidity,rain,prev]])[0])
    st.metric('Predicted soil moisture (synthetic model)',f'{result:.1f}%')
    st.info(recommendation(result))
    st.caption('A microbial activity index is not direct laboratory measurement. Recommendations are illustrative only.')
st.subheader('Input features')
st.write(', '.join(FEATURES))
