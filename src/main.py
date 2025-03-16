
class Grafos:
    def __init__(self, direcionado = False, ponderado = False):
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.vertices = []

    def inserirVertice():
        raise NotImplementedError("Método deve ser implementado nas subclasses")

    def removerVertice():
        raise NotImplementedError("Método deve ser implementado nas subclasses")

    def labelVertice():
        raise NotImplementedError("Método deve ser implementado nas subclasses")

    def imprimeGrafo(): 
        raise NotImplementedError("Método deve ser implementado nas subclasses")

    def retornarVizinhos():
        raise NotImplementedError("Método deve ser implementado nas subclasses")

class GrafoLista(Grafos):
    def _init__(self, direcionado, ponderado):
        super().__init__(direcionado, ponderado)

    def inserirAresta():
        zero = 0

    def removerAresta():
        zero = 0

    def existeAresta():
        zero = 0

    def pesoAresta():
        zero = 0

class GrafoMatriz(Grafos):
    def _init__(self, direcionado, ponderado):
        super().__init__(direcionado, ponderado)
