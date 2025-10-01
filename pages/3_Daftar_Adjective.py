# pages/3_Daftar_Adjective.py

import streamlit as st
import pandas as pd

def adjective_app():
    st.set_page_config(layout="centered")
    st.title("🌟 Daftar Adjective (Kata Sifat)")
    st.markdown("Adjective (kata sifat) digunakan untuk mendeskripsikan noun (kata benda).")

    # Data contoh Adjective (beserta Comparative dan Superlative)
    data_adjective = {
        'Adjective (V1)': ['good', 'bad', 'big', 'small', 'happy', 'beautiful', 'tall'],
        'Comparative (V2)': ['better', 'worse', 'bigger', 'smaller', 'happier', 'more beautiful', 'taller'],
        'Superlative (V3)': ['best', 'worst', 'biggest', 'smallest', 'happiest', 'most beautiful', 'tallest'],
        'Arti': ['baik', 'buruk', 'besar', 'kecil', 'senang', 'indah', 'tinggi']
    }
    df_adjective = pd.DataFrame(data_adjective)

    st.subheader("Contoh Adjective dan Tingkat Perbandingannya:")
    st.dataframe(df_adjective, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.info("Halaman ini menampilkan bentuk V1 (dasar), V2 (Comparative), dan V3 (Superlative) untuk kata sifat.")

if __name__ == "__main__":
    adjective_app()