# assignment1_class.py

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def take_photo(self):
        print(f"📸 {self.brand} {self.model} is taking a photo!")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    def play_game(self, game):
        print(f"🎮 Playing {game} at {self.refresh_rate}Hz on {self.brand} {self.model}!")


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S21", 128)
    print(phone1)
    phone1.call("0722334455")
    phone1.take_photo()

    phone2 = GamingPhone("Asus", "ROG Phone 6", 256, 144)
    print(phone2)
    phone2.play_game("PUBG Mobile")