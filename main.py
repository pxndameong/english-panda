import streamlit as st
import pandas as pd
import os

# Nama file Excel untuk data irregular verbs
FILE_NAME = "data_irreguralverb.xlsx"

# --- Fungsi untuk Memuat Data ---
# Menggunakan st.cache_data agar data hanya dimuat sekali dan cepat diakses
@st.cache_data
def load_data(file_path):
    """Memuat data irregular verbs dari file Excel."""
    
    # 1. Cek keberadaan file
    if not os.path.exists(file_path):
        st.error(f"File '{file_path}' tidak ditemukan. Pastikan Anda memiliki file Excel dengan nama tersebut di folder yang sama.")
        return None
        
    try:
        # 2. Baca file Excel
        # Catatan: Kolom harus diberi nama V1, V2, V3 di baris pertama Excel.
        df = pd.read_excel(file_path, header=0, names=['V1', 'V2', 'V3'])
        
        # 3. Konversi V1 menjadi dictionary untuk pencarian yang sangat cepat
        # key = V1 (Infinitive), value = [V2, V3]
        verb_dictionary = df.set_index('V1').T.to_dict('list')
        return verb_dictionary
        
    except Exception as e:
        st.error(f"Gagal memuat data dari Excel. Pastikan format kolom di Excel adalah V1, V2, V3. Error: {e}")
        return None

# --- Fungsi Utama Streamlit ---
def main():
    st.set_page_config(page_title="Kamus Irregular Verb V1 V2 V3", layout="centered")

    st.title("📚 Kamus Irregular Verbs (V1, V2, V3)")
    st.markdown("Ketik kata kerja. Hasil akan dicari otomatis dari daftar lokal.")

    # Muat data kamus
    verb_dictionary = load_data(FILE_NAME)

    if verb_dictionary is None:
        # Hentikan eksekusi jika data gagal dimuat
        return

    # Input pengguna yang memicu pencarian otomatis
    search_term = st.text_input(
        "Masukkan Kata Kerja (Verb 1):", 
        placeholder="Contoh: go, write, break"
    ).strip().lower()

    # Logika Pencarian Otomatis
    if search_term:
        
        # Cek apakah kata kerja ada di kamus lokal (Irregular Verbs)
        if search_term in verb_dictionary:
            v2, v3 = verb_dictionary[search_term]
            
            st.subheader(f"Hasil untuk: **{search_term.upper()}**")
            
            # Tampilkan hasil dalam kolom
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Verb 1 (Infinitive)", search_term)
            
            with col2:
                st.metric("Verb 2 (Past Simple)", v2)
                
            with col3:
                st.metric("Verb 3 (Past Participle)", v3)
            
            st.success("Kata kerja tak beraturan ditemukan!")

        else:
            # Penanganan untuk kata kerja yang tidak ditemukan dalam daftar irregular
            st.info(f"Kata **'{search_term.upper()}'** tidak ditemukan dalam daftar Irregular Verbs.")
            
            # Tampilkan asumsi bentuk Regular Verb jika input cukup panjang
            if len(search_term) > 2:
                st.markdown("---")
                st.caption("*Asumsi: Jika kata kerja ini beraturan (regular), maka bentuknya adalah:*")
                
                # Pastikan indentasi di bawah ini konsisten (4 spasi)
                colA, colB, colC = st.columns(3)
                
                with colA:
                    st.metric("V1", search_term)
                with colB:
                    st.metric("V2 (Regular)", f"{search_term}ed")
                with colC:
                    st.metric("V3 (Regular)", f"{search_term}ed")
            
# Jalankan aplikasi
if __name__ == "__main__":
    main()