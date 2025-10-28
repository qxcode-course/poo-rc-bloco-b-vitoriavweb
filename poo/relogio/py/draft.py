class watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.hora = 0
        self.minuto=0
        self.segundo=0
        self.sethora(hora)
        self.setminuto(minuto)
        self.setsegundo(segundo)
    
    
    def gethora(self) -> int:
        return self.hora
    def getminuto(self) -> int:
        return self.minuto
    def getsegundo(self) -> int:
        return self.segundo

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
    def sethora(self, hora: int):
        if 0<=hora<=23:
            self.hora=hora
        else:
            print("fail: hora invalida")

    def setminuto(self,minuto: int):
        if 0<=minuto<=59:
            self.minuto=minuto
        else:
            print("fail: minuto invalido")

    def setsegundo(self,segundo: int):
        if 0<=segundo<=59:
            self.segundo=segundo
        else:
            print("fail: segundo invalido")

    def proxsegundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1
                if self.hora == 24:
                    self.hora = 0

def main():
    relogio = watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "init":
            relogio = watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            relogio.sethora(int(args[1]))
            relogio.setminuto(int(args[2]))
            relogio.setsegundo(int(args[3]))
        elif args[0] == "next":
            relogio.proxsegundo()
        else:
            print("fail")
main() 