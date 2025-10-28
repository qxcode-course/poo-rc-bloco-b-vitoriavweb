class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade
    
    def __str__(self):
        return f"{self._nome}:{self._idade}"
    
class Motoca:
    def __init__(self,potencia = 1):
        self.potencia = potencia
        self.time = 0
        self.pessoa = None

    def inserir(self, pessoa: Pessoa):
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.pessoa = pessoa
        return True
    
    def remove(self):
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoa = self.pessoa
        self.pessoa = None
        print(pessoa)
        return pessoa
    
    def buyTime(self, time: int):
        self.time += time

    def drive(self, time: int):
        if self.time <= 0:
            print("fail: buy time first")
            return 
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.pessoa.getIdade() > 10:
            print("fail: too old to drive")
            return 
        if time > self.time:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0
        else:
            self.time -= time

    def honk(self):
        return "P" + ("e" * self.potencia) + "m"

    def __str__(self):
        pessoa_str = str(self.pessoa) if self.pessoa else "empty"
        return f"power:{self.potencia}, time:{self.time}, person:({pessoa_str})"

def main():
    motoca = Motoca()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            motoca = Motoca(int(args[1]))
        elif args[0] == "leave":
            motoca.remove()
        elif args[0] == "enter":
            pessoa = Pessoa(args[1], int(args[2]))
            motoca.inserir(pessoa)
        elif args[0] == "buy":
            motoca.buyTime(int(args[1]))
        elif args[0] == "drive":
            motoca.drive(int(args[1]))
        elif args[0] == "honk":
            print(motoca.honk())
        elif args[0] == "show":
            print(motoca)

main()
