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
        
        if any((aresta["origem"] == label_origem) and (aresta["destino"] == label_destino) for aresta in self.arestas):
            print("Aresta com origem e destino escolhidos já existem!")
            return False
        else:
            if self.ponderado:              #Se o grafo for ponderado
                if self.direcionado:        #Se o grafo for direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                else:                       #Se o grafo for não direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                    self.arestas.append({"origem": label_destino, "destino": label_origem, "peso": peso})
            else:                           #Se o grafo não for ponderado
                if self.direcionado:        #Se o grafo for direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino})
                else:                       #Se o grafo for não direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino})
                    self.arestas.append({"origem": label_destino, "destino": label_origem})
            return True

    def removerVertice(self, indice : int) -> bool:
        if len(grafo_lista) < indice:
            print("Vértice não existe nesse índice! OBS: indexado a partir de 0")
            return False

    def removerAresta():
        zero = 0

    def existeAresta(self, origem : int, destino : int):
        if any((aresta["origem"] == origem) and (aresta["destino"] == destino) for aresta in self.arestas):
            print("Aresta com origem e destino escolhidos existem!")
            return True
        else:
            print("Aresta com origem e destino escolhidos não existem!")

    def pesoAresta():
        zero = 0

    def retornarVizinhos():#self, int vertice (Achop que é o indice do vertice, seria massa se desse pra colocar o )
        zero = 0
        
class GrafoMatriz(Grafos):
    def _init__(self, direcionado, ponderado):
        super().__init__(direcionado, ponderado)
        grafo_matriz = [[]]

grafo_lista = GrafoLista(ponderado=False, direcionado=True)
grafo_lista.inserirVertice("A")
grafo_lista.inserirVertice("B")
grafo_lista.inserirAresta("A", "B")
grafo_lista.imprimeGrafo()
grafo_lista.existeAresta("A", "B")
grafo_lista.existeAresta("B", "A")