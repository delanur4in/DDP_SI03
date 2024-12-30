import streamlit as st
from fitur.kendaraan import Kendaraan
from fitur.simulasi import Simulasi
from fitur.pembayaran import Pembayaran
from fitur.database import Database
from fitur.laporan import Laporan

# Class utama untuk mengelola aplikasi
class Aplikasi:
    def __init__(self):
        # Pemetaan menu ke fungsi-fungsi modul
        self.menu = {
            "Kendaraan": Kendaraan.run_kendaraan,
            "Simulasi": Simulasi.run_simulasi,
            "Pembayaran": Pembayaran.run_pembayaran,
            "Database": Database.run_database,
            "Laporan": Laporan.run_laporan,
            
        }

    def jalankan_menu(self):
        st.sidebar.title("Menu Aplikasi")
        pilihan = st.sidebar.radio("Pilih Menu", list(self.menu.keys()))

        # Perulangan untuk menjalankan menu
        for nama_menu, fungsi in self.menu.items():
            if pilihan == nama_menu:
                try:
                    fungsi()  # Memanggil fungsi dari modul yang sesuai
                except Exception as e:
                    st.error(f"Terjadi kesalahan pada {nama_menu}: {e}")
                break
        else:
            st.warning("Menu tidak ditemukan!")

# Menjalankan aplikasi
if __name__ == "__main__":
    app = Aplikasi()
    app.jalankan_menu()
