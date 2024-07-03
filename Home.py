import streamlit as st

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("# Kidney Failure Risk Calculator 💊")
st.divider()

st.markdown("""
    [**Paper**](https://jamanetwork.com/journals/jama/fullarticle/897102) 📖 | 
    [**Website**](https://kidneyfailurerisk.com/) 💻 
    """)

st.markdown("""
The kidney failure risk equations were initially developed using patients in Canada with chronic kidney disease (CKD) stages G3-G5. These equations have since been validated in a diverse population of over 700,000 individuals across more than 30 countries worldwide.

This 8 variable calculator accurately predicts the 5 year probability of treated kidney failure (dialysis or transplantation) for a potential patient with CKD Stage 3 to 5. It's important to note that predicted risks may vary from actual risks observed in clinical populations with different risk profiles.

Assessing the probability of kidney failure can be valuable for facilitating communication between patients and healthcare providers, guiding the triage and management of nephrology referrals, and determining the optimal timing for dialysis access placement and living related kidney transplants.
""")

st.divider()
#st.markdown("""App Created by [Health Universe](https://www.healthuniverse.com) 🚀
#           (Kinal Patel & Mitchell Parker)""")
st.image("HU_Logo.svg")
