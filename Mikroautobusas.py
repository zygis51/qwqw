from TransportoPriemone import TransportoPriemone

class Mikroautobusas(TransportoPriemone):
    def gauti_tipą(self):
        return "mikroautobusas"
    
    def __init__(self, marke, modelis, metai, kaina, prieinamumas="laisva", vietu_sk=None):
        super().__init__(marke, modelis, metai, kaina, prieinamumas)
        self.vietu_sk = vietu_sk or 8
    
    def __str__(self):
        return f"{super().__str__()}, Vietų sk.: {self.vietu_sk}"