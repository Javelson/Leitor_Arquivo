class Veiculo:
    def __init__(self, placa, modelo, ano, km):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def exibir(self):
        print(f'Veiculo Placa: {self.placa}')
        print(f'Modelo:{self.modelo}, Ano: {self.ano} - km: {self.km}')