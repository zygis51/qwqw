from TransportoPriemone import TransportoPriemone
from Automobilis import Automobilis
from Mikroautobusas import Mikroautobusas

class TransportoPriemonesFactory:
    @staticmethod
    def sukurti_priemone(tipas, *args, **kwargs):
        if tipas == "automobilis":
            return Automobilis(*args, **kwargs)
        elif tipas == "mikroautobusas":
            return Mikroautobusas(*args, **kwargs)
        else:
            raise ValueError(f"Nežinomas transporto priemonės tipas: {tipas}")