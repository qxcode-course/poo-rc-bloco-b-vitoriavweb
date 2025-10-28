class Chinela:
    def __init__(self):    
        self.tamanho: int = 0  

    def __str__(self):
        return f"tamanho da chinela: {self.tamanho}"

    def gettamanho(self): 
        return self.tamanho

    def settamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("erro")
        elif valor % 2 != 0:
            print("erro")
        else:
            self.tamanho = valor
            print("YES")

def main():
    chinela = Chinela()

    while True:
        try:
            line: str = input()
        except EOFError:
            break

        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(chinela)
        elif args[0] == "init":
            try:
                tamanho = int(args[1])
                chinela.settamanho(tamanho)
            except (IndexError, ValueError):
                print("erro: valor inválido para tamanho")

main()
