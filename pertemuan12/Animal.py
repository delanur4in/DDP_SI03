# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class animal:
    def __init__ (self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def info_animal(self):
        print(f"Nama Hewan : {self.name} , Makanan nya : {self.makanan} ,Hidup di : {self.hidup} ,berkembang biak dengan cara  : {self.berkembang_biak}")
              
kucing = animal ("kucing", "daging", "rumah", "melahirkan")
kucing.info_animal()

# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method