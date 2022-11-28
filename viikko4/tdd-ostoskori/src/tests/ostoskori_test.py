import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        maito = Tuote("Maito", 3)
        pekoni = Tuote("Pekoni", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(pekoni)
        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kahden_tavaran_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        pekoni = Tuote("Pekoni", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(pekoni)
        self.assertEqual(self.kori.hinta(),4)

    def test_kahden_sama_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_sama_tuotteen_lisaamisen_jalkeen_korissa_kahden_tavaran_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),6)
    