class Vertice:
    def __init__(self, valor: int) -> None:
        self.vizinhos = []
        self.valor = valor

    def get_vizinhos(self) -> list:
        return [(vizinho[0], vizinho[1]) for vizinho in self.vizinhos]
    
    def add_vizinho(self, vizinho: object, peso: int):
        self.vizinhos.append(tuple((vizinho, peso)))

    def get_grau(self) -> int:
        return len(self.vizinhos)




    