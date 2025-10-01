# main.py
import streamlit as st

st.set_page_config(
    page_title="English Panda App",
    layout="centered"
)

st.title("🐼 Selamat Datang di English Panda App")
st.markdown("---")

st.header("Kamus Kata Kerja V1, V2, V3")
st.write("Silakan pilih **'1 Kamus Irregular Verb'** di menu sidebar kiri untuk memulai pencarian kata kerja tak beraturan (V1, V2, V3) dari data lokal Anda.")

st.info("💡 Semua data Irregular Verb dimuat dari file 'file.xlsx' lokal.")