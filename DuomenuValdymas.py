import csv
from Klientas import Klientas
from Nuoma import Nuoma

class DuomenuValdymas:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DuomenuValdymas, cls).__new__(cls)
            cls._instance._init_data()
        return cls._instance
    
    def _init_data(self):
        self._init_csv_file('transporto_priemones.csv', 
                          ['marke', 'modelis', 'metai', 'kaina', 'prieinamumas', 'tipas'])
        self._init_csv_file('klientai.csv', ['vardas', 'pavarde'])
        self._init_csv_file('nuomos.csv', 
                          ['kliento_vardas', 'kliento_pavarde', 'transporto_marke', 
                           'transporto_modelis', 'pradzia', 'pabaiga', 'kaina'])
    
    def _init_csv_file(self, filename, headers):
        try:
            with open(filename, 'x', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
        except FileExistsError:
            pass
    
    def gauti_klientus(self):
        klientai = []
        try:
            with open('klientai.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    klientai.append(Klientas(row['vardas'], row['pavarde']))
        except FileNotFoundError:
            pass
        return klientai
    
    def prideti_klienta(self, klientas):
        with open('klientai.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([klientas.vardas, klientas.pavarde])
        return len(self.gauti_klientus())  # Grąžiname kliento ID
    
    def issaugoti_nuoma(self, nuoma):
        with open('nuomos.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                nuoma.klientas.vardas,
                nuoma.klientas.pavarde,
                nuoma.transporto_priemone.marke,
                nuoma.transporto_priemone.modelis,
                nuoma.pradzia,
                nuoma.pabaiga or "",
                nuoma.kaina
            ])
    
    def gauti_nuomas(self):
        nuomos = []
        try:
            with open('nuomos.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    
                    nuomos.append({
                        'klientas': f"{row['kliento_vardas']} {row['kliento_pavarde']}",
                        'transportas': f"{row['transporto_marke']} {row['transporto_modelis']}",
                        'pradzia': row['pradzia'],
                        'pabaiga': row['pabaiga'],
                        'kaina': row['kaina']
                    })
        except FileNotFoundError:
            pass
        return nuomos