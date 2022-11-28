from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []

    def tavaroita_korissa(self):
        maara=0
        for i in self.kori:
            maara += i.lukumaara()
        return maara

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta=0
        for i in self.kori:
            hinta += i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for i in self.kori:
            if i.tuotteen_nimi()== lisattava.nimi():
                i.muuta_lukumaaraa(1)
                return
        osto = Ostos(lisattava)
        self.kori.append(osto)

    def poista_tuote(self, poistettava: Tuote):
        for i in self.kori:
            if i.tuotteen_nimi()== poistettava.nimi():
                if i.lukumaara()>1:
                    i.muuta_lukumaaraa(-1)
                else:
                    self.kori.remove(i)

    def tyhjenna(self):
        self.kori=[]

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
