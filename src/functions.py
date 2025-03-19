TO_DO = '''
REVISAR FUNÇÕES DE REMOVER  - removerVertice
IMPLEMENTAR RETORNAR_VIZINHOS
AO IMPRIMIR GRAFO DEVE-SE MOSTRAR OS VIZINHOS e peso em caso de ponderado

grafomatriz
faltou label vertice e de imprime grafo,
confefrir dps

'''

RED = "\033[91m"  # Vermelho
GREEN = "\033[92m"  # Verde
PURPLE = "\033[95m" #Roxo
RESET = "\033[0m"  #Reseta cor

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

    def labelVertice(self, indice : int) -> str:
        try:
            return self.grafo_lista[indice].get("label")
        except IndexError as e:
            print(f"{RED} Indice nao existente. {RESET}") 

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
                print(f'Grafo na posição {i}, label: {self.grafo_lista[i]["label"]}')
            print()
        else:
            print("Grafo Lista ainda não possui vértices!")

    def inserirAresta(self, label_origem : str, label_destino : str, peso : float = 1.0 ) -> bool:
        if not any(vertice["label"] == label_origem for vertice in self.grafo_lista):
            print(f"{RED}O Vértice origem não existe. {RESET}")
            return False
    
        if not any(vertice["label"] == label_destino for vertice in self.grafo_lista):
            print(f"{RED}O Vértice destino não existe. {RESET}")
            return False
        
        if any((aresta["origem"] == label_origem) and (aresta["destino"] == label_destino) for aresta in self.arestas):
            print(f"{PURPLE}Aresta com origem e destino escolhidos já existem! {RESET}")
            return False
        else:
            if self.ponderado:              #Se o grafo for ponderado
                if self.direcionado:        #Se o grafo for direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                else:                       #Se o grafo for não direcionado
                    if label_origem == label_destino:
                        print(f"{RED}Impossível inserção de self-loop em não direcionada. {RESET}")
                        return False
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                    self.arestas.append({"origem": label_destino, "destino": label_origem, "peso": peso})
            else:                           #Se o grafo não for ponderado
                if self.direcionado:        #Se o grafo for direcionado
                    self.arestas.append({"origem": label_origem, "destino": label_destino})
                else:                       #Se o grafo for não direcionado
                    if label_origem == label_destino:
                        print(f"{RED}Impossível inserção direção self-loop em grafo não direcionado. {RESET}")
                        return False
                    self.arestas.append({"origem": label_origem, "destino": label_destino})
                    self.arestas.append({"origem": label_destino, "destino": label_origem})
            print(f"{GREEN}Aresta inserida com sucesso. {RESET}")
            return True

    def removerVertice(self, indice : int) -> bool:
        try:
            label_indice_a_ser_excluido = self.labelVertice(indice)
            for i, aresta in enumerate(self.arestas):
                if (aresta["origem"] == label_indice_a_ser_excluido or aresta["destino"] == label_indice_a_ser_excluido):
                    self.arestas.pop(i) 
                    #print(f"indice {i}, arestas:  {aresta}")
            self.grafo_lista.pop(indice)
            print(f"{GREEN}Vértice (e arestas associadas) com índice correspondente removida. {RESET}")
            return True
        except IndexError:
            print(f"{RED}Vértice com índice não existente. {RESET}")
            return False

    def removerAresta(self, indice : int) -> bool:
        '''
         indice : int Diz respeito ao índice do vértice das arestas
        '''
        try:
            if not self.direcionada:
                self.arestas.pop(indice)
                print(f"{GREEN}Aresta com índice {indice} removida. {RESET}")
                return True
            else:
                zero = 0 #Tem que ser levado em conta que ao remover uma aresta não direcional, se quebra as remvove as duas arestas criadas
        except IndexError:
            print(f"{RED}Aresta com índice não existente. {RESET}")
            return False

    def existeAresta(self, origem : int, destino : int) -> bool:
        '''
         indice : int Diz respeito ao índice do vértice das vértices
        '''
        try:
            label_origem = self.labelVertice(origem)
            label_destino = self.labelVertice(destino)
        except:
            return False
        
        if any((aresta["origem"] == label_origem) and (aresta["destino"] == label_destino) for aresta in self.arestas):
            #print("Aresta específicada existe")
            return True
        else:
            return False

    def pesoAresta(self, origem : int, destino :int) -> float:
        if self.ponderado == True:
            if self.existeAresta(origem, destino):
                try:
                    label_origem = self.labelVertice(origem)
                    label_destino = self.labelVertice(destino)
                except:
                    print("Aresta c/ origem e destinos informados não existe ")
                    return 0.0
                for aresta in self.arestas:
                    if aresta.get("origem") == label_origem and aresta.get("destino") == label_destino:
                        return  aresta.get("peso")
            
        else:
            print("grafo_lista não é ponderado")
            return 0.0

    def retornarVizinhos():
        zero = 0

class GrafoMatriz(Grafos):
    def __init__(self, direcionado=False, ponderado=False):
        super().__init__(direcionado, ponderado)
        self.grafo_matriz = []  # Matriz de adjacência inicialmente vazia

    def inserir_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo, expandindo a matriz de adjacência."""
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            self.grafo_matriz.append([0] * len(self.vertices))

            for linha in self.grafo_matriz:
                while len(linha) < len(self.vertices):
                    linha.append(0)
        else:
            print(f"Vértice '{vertice}' já existe no grafo.")

    def inserir_aresta(self, origem, destino, peso=1):
        """Adiciona uma aresta entre dois vértices considerando o tipo do grafo."""
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            valor = peso if self.ponderado else 1
            self.grafo_matriz[origem][destino] = valor

            if not self.direcionado:
                self.grafo_matriz[destino][origem] = valor
            return True
        else:
            print("Índices inválidos para inserção da aresta.")
            return False

    def remover_aresta(self, origem, destino):
        """Remove uma aresta do grafo, considerando se ele é direcionado ou não."""
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            self.grafo_matriz[origem][destino] = 0

            if not self.direcionado:
                self.grafo_matriz[destino][origem] = 0

            return True
        else:
            print("Índices inválidos para remoção da aresta.")
            return False

    def existe_aresta(self, origem, destino):
        """Verifica se existe uma aresta entre dois vértices."""
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            return self.grafo_matriz[origem][destino] != 0
        else:
            print("Índices inválidos para verificação da aresta.")
            return False

    def peso_aresta(self, origem, destino):
        """Retorna o peso da aresta entre dois vértices, ou -1 se a aresta não existir."""
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            peso = self.grafo_matriz[origem][destino]
            return peso if peso != 0 else -1
        else:
            print("Índices inválidos para consulta de peso.")
            return -1

    def retornar_vizinhos(self, vertice):
        """Retorna uma lista dos vizinhos do vértice dado."""
        if 0 <= vertice < len(self.vertices):
            vizinhos = [i for i in range(len(self.vertices)) if self.grafo_matriz[vertice][i] != 0]
            return vizinhos
        else:
            print("Índice de vértice inválido.")
            return []

    def imprimir_matriz(self):
        """Imprime a matriz de adjacência do grafo."""
        for linha in self.grafo_matriz:
            print(" ".join(map(str, linha)))


