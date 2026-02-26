#Membuat Class
class Game:
    def __init__ (self, judul, genre, harga):
        self.judul = judul
        self.genre = genre
        self.harga =  harga

    def introduce_self(self):
        print(f"Nama game ini {self.judul} yang bergenre {self.genre} dan harganya {self.harga}")
    
    def change_harga(self, new_harga):
        self.harga = new_harga
        print(f"Harga baru game ini {self.harga}")

Game1 = Game("GenshinImpact", "RPG", "0")
Game2 = Game("Valorant", "FPS", "0")
Game3 = Game("GTAV", "OpenWorld", "800")

print(Game1.judul)
print(Game1.genre)
Game1.introduce_self()
Game2.introduce_self()
Game3.introduce_self()
Game3.change_harga(700)