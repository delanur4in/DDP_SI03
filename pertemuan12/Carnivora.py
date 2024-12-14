from Animal import *

class Carnivora(animal):
    def __init__ (self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_carnivora(self):
        super().info_animal()
        print("Ukuran Tubuh \t\t\t :", self.ukuran_tubuh,
              "\nJenis Kulit \t\t\t :", self.jenis_kulit)
        
harimau = Carnivora("Harimau Sumatera", "Daging", "Darat", "Melahirkan", "Sangat Besar", "Sedikit Berbulu")
harimau.info_carnivora()
print("===================================================")
Ular = Carnivora("Ular piton", "Daging", "Darat", "Bertelur","Sedang", "Bersisik")
Ular.info_carnivora()
print("===================================================")
Beruang = Carnivora("Beruang kutub", "Daging", "Darat", "Melahirkan", "Besar", "Berbulu")
Beruang.info_carnivora()