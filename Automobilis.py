from TransportoPriemone import TransportoPriemone

class Automobilis(TransportoPriemone):
    def gauti_tipą(self):
        return "automobilis"
    
    def __init__(self, marke, modelis, metai, kaina, prieinamumas="laisva", duru_sk=None):
        super().__init__(marke, modelis, metai, kaina, prieinamumas)
        self.duru_sk = duru_sk or 5
    
    def __str__(self):
        return f"{super().__str__()}, Durų sk.: {self.duru_sk}"