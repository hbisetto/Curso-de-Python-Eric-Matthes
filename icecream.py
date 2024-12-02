from exercise_restaurant import Restaurant

class IceCreamStand (Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        self.number_served = 0
        
    def showFlavors(self):
        for flavor in self.flavors:
            print(flavor)
    
sabores = ['Manga', 'Morango', 'Limao']    
pitanga = IceCreamStand('Pitanga', 'Sorveteria', sabores)

pitanga.describe_restaurant()
pitanga.showFlavors()
pitanga.increment_number_served(3)
pitanga.describe_restaurant()
        
    