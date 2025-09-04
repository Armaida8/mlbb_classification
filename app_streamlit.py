import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_mlbb.joblib")

st.title("Machine Learning Classification")
st.markdown("Aplikasi Machine Learning Sederhana")

kill = st.slider("Jumlah Kill",0,20)
assist = st.slider("Jumlah Assist",0,20)
death = st.slider("Jumlah Death",0,20)
turret = st.slider("Jumlah Turret",0,20)

if st.button("Prediksi"):
	data_baru = pd.DataFrame([[kill,assist,death,turret]], columns=["kill","assist","death","turret"])
	
	hasil = model.predict(data_baru)[0]
	st.success(f"Hasil Prediksinya : {hasil}")
	st.snow()
	st.balloons()
st.caption("Dibuat dengan :heart: dan :skull: oleh Armaida")