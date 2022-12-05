class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = None

    def miinus(self, arvo,komento=None):
        self.tulos = self.tulos - arvo
        self.edellinen = komento

    def plus(self, arvo,komento=None):
        self.tulos = self.tulos + arvo
        self.edellinen = komento

    def nollaa(self,komento=None):
        self.tulos = 0
        self.edellinen = komento

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        if self.edellinen:
            self.edellinen.kumoa()