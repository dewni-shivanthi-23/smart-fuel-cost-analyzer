import streamlit as st
import requests

st.title("Smart Fuel Cost Analyzer (Sri Lanka)")

distance = st.slider("Distance per day (km)", 1, 50, 10)
vehicle = st.selectbox("Vehicle Type", ["bike", "car", "van"])
fuel_price = st.slider("Fuel price (Rs.)", 250, 450, 300)

if st.button("Calculate Cost"):
    url = f"http://backend:8000/predict?distance={distance}&vehicle={vehicle}&fuel_price={fuel_price}"
    res = requests.get(url)
    data = res.json()

    st.success(f"Daily Cost: Rs. {data['daily_cost']}")
    st.success(f"Weekly Cost: Rs. {data['weekly_cost']}")

    st.info(data["suggestion"])