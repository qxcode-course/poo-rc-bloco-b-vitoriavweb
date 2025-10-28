class notebook:
    def __init__(self):
        self.ligado: bool = false
        self.tempo: int = 0

    
    def __str__(self):
        return f"status: "
    
    def usar(self):
        self.ligado

class bateria:
    def __init__(self, capacidade):
        self.capacidade: int = capacidade
        self.carga: int = capacidade
    
    def __str__(self):
        return f"{self.carga}/{self.capacidade}"

    def tempogasto (self, tempo: int):
        self.carga -= tempo
        if self.carga <=0:
            self.carga = 0
    
    def cerregar(self, tempo: int, quantidade: int):
        self.carga += quantidade*tempo
        if self.carga > self.capacidade:
            self.carga = self.capacidade
    
    
#parte 3
class Carregador:
    def __init__(self, potencia):
        self.potencia: int = potencia
