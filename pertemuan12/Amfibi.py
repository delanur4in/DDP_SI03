from Animal import *

# setiap class child itu mempunyai 2 properti dan method
class Amfibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas
        
    def info_amfibi(self):
        super().info_animal(),
        print("Jenis Air \t\t\t :", self.jenis_air,
              "\nBernapas \t\t\t :", self.bernapas)
        
amfibi = Amfibi("Katak", "Serangga", 'Dua alam', "Bertelur", "Air Tawar", "Kulit dan Paru-paru")
amfibi.info_amfibi()