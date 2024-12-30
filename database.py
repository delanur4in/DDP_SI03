import streamlit as st

# Class Database untuk fitur database kendaraan
class Database:
    @staticmethod
    def run_database():
        st.title("Database Kendaraan")

        if "kendaraan" not in st.session_state:
            st.session_state["kendaraan"] = []

        def tambah_kendaraan(nama_kendaraan, saldo):
            kendaraan_baru = {
                "id_kendaraan": len(st.session_state["kendaraan"]) + 1,
                "nama_kendaraan": nama_kendaraan,
                "saldo": saldo
            }
            st.session_state["kendaraan"].append(kendaraan_baru)

        menu = st.sidebar.selectbox("Pilih Menu", ["Tambah Kendaraan", "Lihat Data Kendaraan"])

        if menu == "Tambah Kendaraan":
            nama_kendaraan = st.text_input("Nama Kendaraan")
            saldo = st.number_input("Saldo Awal", min_value=0, step=1000)
            if st.button("Simpan"):
                if nama_kendaraan and saldo >= 0:
                    tambah_kendaraan(nama_kendaraan, saldo)
                    st.success("Kendaraan berhasil ditambahkan.")
                else:
                    st.error("Isi semua data dengan benar.")

        elif menu == "Lihat Data Kendaraan":
            st.write("Data Kendaraan")
            if len(st.session_state["kendaraan"]) == 0:
                st.warning("Belum ada kendaraan yang terdaftar.")
            else:
                for kendaraan in st.session_state["kendaraan"]:
                    st.write(f"ID: {kendaraan['id_kendaraan']}, Nama: {kendaraan['nama_kendaraan']}, Saldo: {kendaraan['saldo']}")
