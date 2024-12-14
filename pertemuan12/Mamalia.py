from Animal import *

class Mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal()
        print("Ukuran Tubuh \t\t\t :", self.ukuran_tubuh,
              "\nJenis Kulit \t\t\t :", self.jenis_kulit)
        

gajah = Mamalia("Gajah", "Tumbuhan", "Darat", "Melahirkan", "Sangat Besar", "Sedikit Berbulu")
gajah.info_mamalia()
print("===================================================")
kucing = Mamalia("Kucing", "Hewan", "Darat", "Melahirkan","Kecil", "Berbulu")
kucing.info_mamalia()
print("===================================================")
kelinci = Mamalia("Kelinci", "Tumbuhan", "Darat", "Melahirkan", "Kecil", "Berbulu")
kelinci.info_mamalia()