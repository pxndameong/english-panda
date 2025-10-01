# main.py

import streamlit as st

st.set_page_config(
    page_title="English Panda App",
    layout="centered"
)

st.title("🐼 Selamat Datang di English Panda App")
st.markdown("---")

st.header("Kamus Kata Kerja V1, V2, V3")
st.write("Silakan pilih **'Kamus Irregular Verb'** di menu sidebar kiri untuk memulai pencarian kata kerja tak beraturan (V1, V2, V3) dari data lokal Anda.")

st.info("💡 Semua data Irregular Verb dimuat dari file 'file.xlsx' lokal, sehingga pencarian sangat cepat dan tidak memerlukan API key!")

st.markdown("""
### Cara Penggunaan:
1. Klik menu di sidebar (kiri atas)
2. Pilih '1 Kamus Irregular Verb'
3. Mulai ketikkan kata kerja (V1) di kolom pencarian.
""")

if st.button("Lihat Daftar Kata Kerja yang Dimuat"):
    st.warning("Pastikan Anda sudah mengisi file.xlsx dengan data yang lengkap!")
    # Anda bisa tambahkan logika untuk menampilkan sebagian data di sini jika diperlukan.