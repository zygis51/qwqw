from abc import ABC, abstractmethod
import csv

class TransportoPriemone(ABC):
    def __init__(self, marke, modelis, metai, kaina, prieinamumas="laisva"):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.kaina = kaina
        self.prieinamumas = prieinamumas
    
    @abstractmethod
    def gauti_tipą(self):
        pass
    
    def __str__(self):
        return f"{self.marke} {self.modelis} ({self.metai}), Kaina: {self.kaina}€/d., Būsena: {self.prieinamumas}"
    
    @classmethod
    def gauti_visas(cls):
        priemones = []
        try:
            with open('transporto_priemones.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['tipas'] == 'automobilis':
                        priemones.append(Automobilis(**row))
                    elif row['tipas'] == 'mikroautobusas':
                        priemones.append(Mikroautobusas(**row))
        except FileNotFoundError:
            pass
        return priemones
    
    @classmethod
    def gauti_laisvas(cls):
        return [tp for tp in cls.gauti_visas() if tp.prieinamumas == 'laisva']
    
    def išsaugoti(self):
        with open('transporto_priemones.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                self.marke, self.modelis, self.metai, 
                self.kaina, self.prieinamumas, self.gauti_tipą()
            ])
    
    def atnaujinti_prieinamumą(self, nauja_būsena):
        self.prieinamumas = nauja_būsena
        visos_priemones = self.gauti_visas()
        with open('transporto_priemones.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['marke', 'modelis', 'metai', 'kaina', 'prieinamumas', 'tipas'])
            for tp in visos_priemones:
                if tp.marke == self.marke and tp.modelis == self.modelis:
                    tp.prieinamumas = nauja_būsena
                writer.writerow([
                    tp.marke, tp.modelis, tp.metai, 
                    tp.kaina, tp.prieinamumas, tp.gauti_tipą()
                ])