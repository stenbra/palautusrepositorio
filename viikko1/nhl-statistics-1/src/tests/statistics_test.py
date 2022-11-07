import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_players_set(self):
        a  = self.statistics._players
        b=PlayerReaderStub().get_players()
        self.assertEqual(a[0].name,b[0].name)
    
    def test_search_exist(self):
        a=self.statistics.search("Semenko")
        self.assertAlmostEqual(a.name,"Semenko")
    
    def test_search_not_found(self):
        self.assertIsNone(self.statistics.search("asdad"))

    def test_team(self):
        self.assertAlmostEqual(self.statistics.team("PIT")[0].name,"Lemieux")
    
    def test_top(self):
        self.assertAlmostEqual(self.statistics.top(1)[0].name,"Gretzky")
    def test_top_points(self):
        self.assertAlmostEqual(self.statistics.top(1)[0].name,"Gretzky")
    def test_top_goals(self):
        self.assertAlmostEqual(self.statistics.top(1,2)[0].name,"Lemieux")
    def test_top_assists(self):
        self.assertAlmostEqual(self.statistics.top(1,3)[0].name,"Gretzky")
    