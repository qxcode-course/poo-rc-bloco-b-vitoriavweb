
class camisa:
    def __init__(self):
        self.tamanho: str = ""

    def gettamanho(self) -> str:
        return self.tamanho

    def settamanho(self, valor: str):
        etiqueta = ["PP", "P", "M", "G", "GG", "XG"]

        if valor in etiqueta:
            self.tamanho = valor
        else:
            print(f"fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def __str__(self):
        return f"size: ({self.tamanho})"

def main():
    camiseta = camisa()

    while True:
        try:
            line: str = input()
        except EOFError:
            break
        print("$" + line)
        args: list[str]=line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(camiseta)
        elif args[0] == "size":
            camiseta.settamanho(args[1])
        else:
            print("fail: comando invalido")
main()