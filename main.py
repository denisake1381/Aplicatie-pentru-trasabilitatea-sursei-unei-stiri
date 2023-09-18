# Tema L33 Python
# Implementati o aplicatie pentru trasabilitatea sursei unei stiri. Fiecare stire va avea un Titlu, Autor si
# Continut. De asemenea, fiecare Stire va avea o referinta catre stirea sursa (stirea pe care se bazeaza
# informatia). Implementati un singletone cu metoda “verificaStiri” care primeste 2 stiri si returneaza True
# daca exista cel putin o stire sursa comuna intre cele 2 stiri

class Stire:
    def __init__(self, titlu, autor, continut, sursa=None):
        self.titlu = titlu
        self.autor = autor
        self.continut = continut
        self.sursa = sursa  

class TrasabilitateStiri:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.stiri = []
        return cls._instance

    def adauga_stire(self, stire):
        self.stiri.append(stire)

    def verificaStiri(self, stire1, stire2):
        surse_stire1 = set()
        surse_stire2 = set()

        self._collect_sources(stire1, surse_stire1)
        self._collect_sources(stire2, surse_stire2)

        return bool(surse_stire1.intersection(surse_stire2))

    def _collect_sources(self, stire, surse):
        if stire.sursa is not None:
            surse.add(stire.sursa)
            self._collect_sources(stire.sursa, surse)


if __name__ == "__main__":
    aplicatie = TrasabilitateStiri()

    stire_sursa = Stire("Stire sursa", "Autor Sursa", "Continut stire sursa")
    stire1 = Stire("Stire 1", "Autor 1", "Continut stire 1", stire_sursa)
    stire2 = Stire("Stire 2", "Autor 2", "Continut stire 2", stire_sursa)

    aplicatie.adauga_stire(stire_sursa)
    aplicatie.adauga_stire(stire1)
    aplicatie.adauga_stire(stire2)

    rezultat = aplicatie.verificaStiri(stire1, stire2)
    print("Există stire sursă comună între stire1 și stire2:", rezultat)
