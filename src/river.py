class River:
    def __init__(self, name, fishes):
        self.name = name
        self.fish = fishes

    def name_of_river(self):
        self.river.name

    def fish_count(self):
        return len(self.fish())

    def remove_fish(self,fish):
        self.fish.remove(fish)

    def bear_eats_fish_from_river(self,bear,fish):
       bear.bear_eats_fish(fish)
       self.remove_fish(fish)

