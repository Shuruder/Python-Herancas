class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor 
        self.placa = placa 
        self.n_rodas = n_rodas 
        
    def ligar_motor(self):
        print("Ligando motor...")
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado):
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
        

moto = Motocicleta("Preta", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("Branco", "XDE-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("Roxo", "GFD-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()