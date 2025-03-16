class Grafos:
    def __init__(self, direcionado = False, ponderado = False):
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.vertices = []

class GrafoLista(Grafos):
    def __init__(self, direcionado, ponderado):
        super().__init__(direcionado, ponderado)
        self.grafo_lista = []
        self.arestas = []

    def inserirVertice(self, label : str) -> bool:
        is_vertice_existente = False
        if any(vertice["label"] == label for vertice in self.grafo_lista):
            print("Já existe um vértice com essa label")
            return False
        else:
            self.grafo_lista.append({"label" : label})
            print("Vértice inserido com sucesso")
            return True

    def imprimeGrafo(self) -> None: 
        if self.grafo_lista:
            print()
            for i in range(len(self.grafo_lista)):
                print(f'Grafo na posição {i+1}, label: {self.grafo_lista[i]["label"]}')
        else:
            print("Grafo Lista ainda não possui vértices!")


    def inserirAresta(self, label_origem : str, label_destino : str, peso : int = 1, ) -> bool:
        if not any(vertice["label"] == label_origem for vertice in self.grafo_lista):
            print("O Vértice origem não existe.")
            return False
    
        if not any(vertice["label"] == label_destino for vertice in self.grafo_lista):
            print("O Vértice destino não existe.")
            return False
        
        if self.ponderado:       #Tratativa para arestas ponderadas
            zero = 0
            if self.direcionado: #Tratativa para grafo direcionado
                zero = 0
            else:                #Tratativa para grafo não direcionado
                zero = 0
        else:                    #Tratativa para arestas não ponderadas
            
            if self.direcionado: #Tratativa para grafo direcionado
                zero = 0
            else:                #Tratativa para grafo não direcionado
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
        grafo_matriz = [[]]

grafo_lista = GrafoLista(ponderado=False, direcionado=False)
grafo_lista.inserirVertice("A")
grafo_lista.inserirVertice("B")
grafo_lista.inserirVertice("A")
grafo_lista.imprimeGrafo()