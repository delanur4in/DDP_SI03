import streamlit as st

# Class Pembayaran untuk fitur pembayaran
class Pembayaran:
    @staticmethod
    def run_pembayaran():
        st.title("Pembayaran")

        if 'saldo' not in st.session_state:
            st.session_state['saldo'] = 100000

        def kurangi_saldo(tarif):
            if st.session_state.saldo >= tarif:
                st.session_state.saldo -= tarif
                st.success(f"Saldo berhasil dikurangi sebesar {tarif}. Saldo tersisa: {st.session_state.saldo}")
                if st.session_state.saldo < 20000:
                    st.warning("Saldo Anda rendah. Mohon segera isi ulang!")
            else:
                st.error("Saldo tidak cukup untuk membayar tarif ini.")

        tarif_tol = st.number_input("Masukkan tarif tol:", min_value=0, step=1000)

        if st.button("Bayar Tarif"):
            if tarif_tol > 0:
                kurangi_saldo(tarif_tol)
            else:
                st.error("Masukkan tarif tol yang valid.")

        st.write(f"Saldo Anda saat ini: {st.session_state.saldo}")

        if st.button("Isi Ulang Saldo"):
            st.session_state.saldo += 50000
            st.success(f"Saldo berhasil diisi ulang. Saldo saat ini: {st.session_state.saldo}")
