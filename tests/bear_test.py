import unittest
from src.bear import Bear
from src.fish import Fish
from src.river import River

class TestBear(unittest.TestCase):
    
    def setUp(self):
        self.bear = Bear("Yogi", "Grizzly")
        self.fish = Fish("Dory")
        self.fish1 = Fish("Nemo")
        self.fish2 = Fish("Toto")

        fishes = [self.fish, self.fish1, self.fish2]
        self.river = River("Amazon", fishes)
  
        
    def test_bear_has_a_name(self):

        self.assertEqual("Yogi", self.bear.name)

    def test_bear_fullness(self):
        self.assertEqual(0, len(self.bear.stomach))

    def test_bear_eats_fish(self):
        self.bear.bear_eats_fish("Dory")
        self.assertEqual(["Dory"], self.bear.stomach)

    def test_bear_food_count(self):
        self.bear.bear_eats_fish("Dory")
        self.assertEqual(1,self.bear.bear_food_count())
    
 