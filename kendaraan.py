import streamlit as st
from datetime import datetime
import pandas as pd

# Class Kendaraan untuk fitur simulasi kendaraan
class Kendaraan:
    @staticmethod
    def run_kendaraan():
        if 'data' not in st.session_state:
            st.session_state.data = pd.DataFrame(columns=['Nomor Kendaraan', 'Waktu Masuk', 'Waktu Keluar'])

        st.title("Simulasi Kendaraan Masuk dan Keluar di Pintu Tol")

        nomor_kendaraan = st.text_input("Masukkan Nomor Kendaraan:")

        if st.button("Kendaraan Masuk"):
            if nomor_kendaraan:
                waktu_masuk = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame({
                    'Nomor Kendaraan': [nomor_kendaraan],
                    'Waktu Masuk': [waktu_masuk],
                    'Waktu Keluar': [None]
                })], ignore_index=True)
                st.success(f"Kendaraan {nomor_kendaraan} berhasil masuk.")
            else:
                st.error("Masukkan nomor kendaraan terlebih dahulu!")

        if st.button("Kendaraan Keluar"):
            if nomor_kendaraan:
                waktu_keluar = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                mask = (st.session_state.data['Nomor Kendaraan'] == nomor_kendaraan) & (st.session_state.data['Waktu Keluar'].isnull())
                if mask.any():
                    st.session_state.data.loc[mask, 'Waktu Keluar'] = waktu_keluar
                    st.success(f"Kendaraan {nomor_kendaraan} berhasil keluar.")
                else:
                    st.error("Nomor kendaraan tidak ditemukan atau sudah keluar!")
            else:
                st.error("Masukkan nomor kendaraan terlebih dahulu!")

        st.subheader("Data Kendaraan")
        st.dataframe(st.session_state.data)

        if st.button("Hapus Semua Data"):
            st.session_state.data = pd.DataFrame(columns=['Nomor Kendaraan', 'Waktu Masuk', 'Waktu Keluar'])
            st.warning("Semua data telah dihapus!")
