# pages/2_Daftar_Adverb.py

import streamlit as st
import pandas as pd

def adverb_app():
    st.set_page_config(layout="centered")
    st.title("🏃‍♀️ Daftar Adverb (Kata Keterangan)")
    st.markdown("Adverb (kata keterangan) sering dibentuk dari adjective dengan menambahkan **-ly**.")

    # Data contoh Adverb
    data_adverb = {
        'Adjective': ['quick', 'careful', 'easy', 'sudden', 'bad', 'fast', 'hard'],
        'Adverb (+ly)': ['quickly', 'carefully', 'easily', 'suddenly', 'badly', 'fast (irregular)', 'hard (irregular)'],
        'Arti (Contoh)': ['Dengan cepat', 'Dengan hati-hati', 'Dengan mudah', 'Tiba-tiba', 'Dengan buruk', 'Cepat', 'Keras/Sulit']
    }
    df_adverb = pd.DataFrame(data_adverb)

    st.subheader("Contoh Adverb Umum:")
    st.dataframe(df_adverb, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.warning("Fitur pencarian otomatis untuk Adverb belum diimplementasikan di halaman ini.")
    st.write("Anda bisa menambahkan *search box* di sini jika Anda memiliki *dataset* Adverb yang lebih lengkap!")

if __name__ == "__main__":
    adverb_app()