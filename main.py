import streamlit as st

st.title("Aplikasi Perhitungan Molaritas")

bobot = st.number_input("Masukkan nilai bobot")
volume = st.number_input("Masukkan nilai volume")
mr = st.number("Masukkan nilai mr")

tombol = st.button("hitung nilai molaritas")

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.succes(f 'Nilai molaritas adalah' { nilai_molaritas}')