class roupa:
    def __init__(self):
        self.tamanho: str = ""

    def settamanho(self, etiqueta: str):
        sla = ["PP", "P", "M", "G", "GG", "XG"]
        if etiqueta in sla:
            self.tamanho = etiqueta
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def gettamanho(self):
        return self.tamanho
    
    def __str__(self):
        return f"size: ({self.tamanho})"
    
def main():
    roupinha = roupa()

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
            print(roupinha)
        elif args[0] == "size":
            roupinha.settamanho(str(args[1]))
        else:
            print("NAOOOOOO")

main()
