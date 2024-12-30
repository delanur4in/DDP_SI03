import streamlit as st

# Class Laporan untuk fitur laporan
class Laporan:
    @staticmethod
    def run_laporan():
        st.title("Laporan dan Visualisasi")

        dates = st.text_area("Masukkan Tanggal (pisahkan dengan koma)", "2024-12-18, 2024-12-19, 2024-12-20")
        transactions = st.text_area("Masukkan Jumlah Transaksi", "100, 150, 120")
        earnings = st.text_area("Masukkan Pendapatan (dalam Rupiah)", "500000, 750000, 600000")

        if st.button("Proses Data"):
            try:
                date_list = [date.strip() for date in dates.split(",")]
                transaction_list = [int(tx.strip()) for tx in transactions.split(",")]
                earnings_list = [int(earn.strip()) for earn in earnings.split(",")]

                st.write("Data Transaksi:")
                for date, transaction, earning in zip(date_list, transaction_list, earnings_list):
                    st.write(f"Tanggal: {date}, Transaksi: {transaction}, Pendapatan: {earning} Rupiah")

            except ValueError as ve:
                st.error(f"Kesalahan nilai: {ve}")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
