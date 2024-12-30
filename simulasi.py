import streamlit as st

# Class Simulasi untuk fitur simulasi
class Simulasi:
    @staticmethod
    def run_simulasi():
        st.title("Simulasi Sistem Pembayaran")

        if 'jumlah' not in st.session_state:
            st.session_state['jumlah'] = []

        def total(jumlah):
            # Perulangan untuk menghitung total pembayaran
            total_pembayaran = 0
            for t in jumlah:
                if t['tipe'] == 'Dibayar':
                    total_pembayaran += t['jumlah']
            return total_pembayaran

        st.header("Tambah Transaksi")
        tipe = st.selectbox("Pilih Tipe Transaksi", ["Dibayar", "Belum Dibayar"])
        jumlah_input = st.number_input("Masukkan Jumlah", min_value=0)

        if st.button("Tambah Transaksi"):
            st.session_state['jumlah'].append({'tipe': tipe, 'jumlah': jumlah_input})
            st.success("Transaksi berhasil ditambahkan!")

        st.subheader("Daftar Transaksi")
        if st.session_state['jumlah']:
            for idx, t in enumerate(st.session_state['jumlah']):
                st.write(f"{idx + 1}. Tipe: {t['tipe']}, Jumlah: {t['jumlah']}")
        else:
            st.write("Belum ada transaksi.")

        total_pembayaran = total(st.session_state['jumlah'])
        st.write(f"Total Pembayaran (Dibayar): {total_pembayaran}")
