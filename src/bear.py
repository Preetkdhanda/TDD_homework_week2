class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def bear_eats_fish(self,fish):
         self.stomach.append(fish)

    def bear_food_count(self):
        return len(self.stomach)

  

