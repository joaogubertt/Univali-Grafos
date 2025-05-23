from src.grafos import Grafos
import heapq

RED = "\033[91m"  # Vermelho
GREEN = "\033[92m"  # Verde
PURPLE = "\033[95m" #Roxo
RESET = "\033[0m"  #Reseta cor 


class GrafoMatriz(Grafos):
    def __init__(self, direcionado=False, ponderado=False):
        super().__init__(direcionado, ponderado)
        self.grafo_matriz = []  # Matriz de adjacência
        self.tipo_representacao = 'matriz'

    def labelVertice(self, indice: int) -> str:
        if 0 <= indice < len(self.vertices):
            return self.vertices[indice]
        else:
            print(f"{RED}Índice de vértice inválido.{RESET}")
            return None

    def inserirVertice(self, label: str) -> bool:
        if label in self.vertices:
            print(f"Vértice '{label}' já existe no grafo.")
            return False
        else:
            self.vertices.append(label)
            # Adiciona uma nova linha para o novo vértice
            self.grafo_matriz.append([0] * len(self.vertices))
            # Atualiza as linhas existentes para incluir a nova coluna
            for linha in self.grafo_matriz[:-1]:
                linha.append(0)
            print(f"{GREEN}Vértice '{label}' inserido com sucesso.{RESET}")
            return True

    def imprimeGrafo(self) -> None:
        if not self.vertices:
            print("Grafo Matriz ainda não possui vértices!")
            return

        print("\nRepresentação do Grafo (Matriz de Adjacência):\n")
        # Cabeçalho com os rótulos dos vértices
        print("    " + " ".join(f"{v:4}" for v in self.vertices))
        for i, linha in enumerate(self.grafo_matriz):
            print(f"{self.vertices[i]:4}", end="")
            for valor in linha:
                print(f"{valor:4}", end="")
            print()
        print()

    def inserirAresta(self, origem, destino, peso: float = 1.0) -> bool:
        # Verifica se os parâmetros são índices ou labels
        if isinstance(origem, str) and isinstance(destino, str):
            try:
                origem_idx = self.vertices.index(origem)
                destino_idx = self.vertices.index(destino)
            except ValueError:
                print(f"{RED}Vértice de origem ou destino não encontrado.{RESET}")
                return False
        else:
            origem_idx = origem
            destino_idx = destino

        if 0 <= origem_idx < len(self.vertices) and 0 <= destino_idx < len(self.vertices):
            valor = peso if self.ponderado else 1
            self.grafo_matriz[origem_idx][destino_idx] = valor

            if not self.direcionado:
                self.grafo_matriz[destino_idx][origem_idx] = valor

            print(f"{GREEN}Aresta entre '{self.vertices[origem_idx]}' e '{self.vertices[destino_idx]}' inserida com sucesso.{RESET}")
            return True
        else:
            print(f"{RED}Índices de vértices inválidos.{RESET}")
            return False

    def removerVertice(self, indice: int) -> bool:
        if 0 <= indice < len(self.vertices):
            # Remove a linha correspondente ao vértice
            self.grafo_matriz.pop(indice)
            # Remove a coluna correspondente ao vértice em cada linha restante
            for linha in self.grafo_matriz:
                linha.pop(indice)
            # Remove o rótulo do vértice
            vertice_removido = self.vertices.pop(indice)
            print(f"{GREEN}Vértice '{vertice_removido}' e todas as suas arestas foram removidos.{RESET}")
            return True
        else:
            print(f"{RED}Índice de vértice inválido.{RESET}")
            return False

    def removerAresta(self, *args) -> bool:
        if len(args) == 1:  # Para compatibilidade com o main original (não faz sentido para matriz)
            print(f"{RED}Para GrafoMatriz, removerAresta precisa de origem e destino{RESET}")
            return False
            
        elif len(args) == 2:  # Nova interface com origem e destino
            origem, destino = args
            
            if isinstance(origem, str) and isinstance(destino, str):
                try:
                    origem_idx = self.vertices.index(origem)
                    destino_idx = self.vertices.index(destino)
                except ValueError:
                    print(f"{RED}Vértice de origem ou destino não encontrado.{RESET}")
                    return False
            else:
                origem_idx = origem
                destino_idx = destino

            if 0 <= origem_idx < len(self.vertices) and 0 <= destino_idx < len(self.vertices):
                self.grafo_matriz[origem_idx][destino_idx] = 0
                if not self.direcionado:
                    self.grafo_matriz[destino_idx][origem_idx] = 0
                return True
            else:
                print(f"{RED}Índices de vértices inválidos.{RESET}")
                return False
        else:
            print(f"{RED}Número inválido de argumentos para removerAresta{RESET}")
            return False

    def existeAresta(self, origem: int, destino: int) -> bool:
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            return self.grafo_matriz[origem][destino] != 0
        else:
            print(f"{RED}Índices de vértices inválidos.{RESET}")
            return False

    def pesoAresta(self, origem: int, destino: int) -> float:
        if 0 <= origem < len(self.vertices) and 0 <= destino < len(self.vertices):
            return self.grafo_matriz[origem][destino] if self.ponderado else 1.0
        else:
            print(f"{RED}Índices de vértices inválidos.{RESET}")
            return 0.0

    def retornarVizinhos(self, vertice: int) -> list:
        if 0 <= vertice < len(self.vertices):
            vizinhos = []
            for i in range(len(self.vertices)):
                if self.grafo_matriz[vertice][i] != 0:
                    vizinhos.append(self.vertices[i])
            return vizinhos
        else:
            print(f"{RED}Índice de vértice inválido.{RESET}")
            return []
    
    def busca_em_largura(self, vertice_origem):
        from collections import deque

        if vertice_origem not in self.vertices:
            print(f"Vértice {vertice_origem} não encontrado no grafo.")
            return

        visitados = set()
        fila = deque()

        index_origem = self.vertices.index(vertice_origem)
        fila.append(index_origem)
        visitados.add(index_origem)

        sequencia_bfs = []

        while fila:
            atual_idx = fila.popleft()
            sequencia_bfs.append(self.vertices[atual_idx])

            for i in range(len(self.vertices)):
                if self.grafo_matriz[atual_idx][i] != 0 and i not in visitados:
                    visitados.add(i)
                    fila.append(i)

        print(f"Vértice {vertice_origem} - Sequência de visita BFS:", " → ".join(sequencia_bfs))

    def busca_em_profundidade(self, vertice_origem):
        if vertice_origem not in self.vertices:
            print(f"Vértice {vertice_origem} não está no grafo.")
            return

        visitados = set()
        sequencia_dfs = []

        label_para_indice = {label: i for i, label in enumerate(self.vertices)}
        indice_para_label = {i: label for i, label in enumerate(self.vertices)}

        def dfs(indice):
            label = indice_para_label[indice]
            visitados.add(label)
            sequencia_dfs.append(label)

            for i, aresta in enumerate(self.grafo_matriz[indice]):
                if aresta != 0:
                    vizinho_label = indice_para_label[i]
                    if vizinho_label not in visitados:
                        dfs(i)

        dfs(label_para_indice[vertice_origem])
        print(f"Vértice {vertice_origem} - Sequência de visita DFS:", " → ".join(sequencia_dfs))

    def dijkstra(self, origem):
        if origem not in self.vertices:
            print(f"Vértice {origem} não encontrado no grafo.")
            return

        n = len(self.vertices)
        distancias = {v: float('inf') for v in self.vertices}
        origem_idx = self.vertices.index(origem)
        distancias[origem] = 0

        # Fila de prioridade: (distância, índice do vértice)
        fila = [(0, origem_idx)]
        visitados = set()
        anteriores = {v: None for v in self.vertices}

        while fila:
            dist_atual, idx_atual = heapq.heappop(fila)
            vertice_atual = self.vertices[idx_atual]

            if vertice_atual in visitados:
                continue
            visitados.add(vertice_atual)

            for vizinho_idx, peso in enumerate(self.grafo_matriz[idx_atual]):
                if peso > 0:  # existe aresta
                    vizinho = self.vertices[vizinho_idx]
                    nova_dist = dist_atual + peso
                    if nova_dist < distancias[vizinho]:
                        distancias[vizinho] = nova_dist
                        anteriores[vizinho] = vertice_atual
                        heapq.heappush(fila, (nova_dist, vizinho_idx))

        print(f"Menores distâncias a partir do vértice {origem}:")
        for v in self.vertices:
            if distancias[v] == float('inf'):
                print(f"{origem} → {v}: não alcançável")
            else:
                # Reconstrói caminho
                caminho = []
                atual = v
                while atual is not None:
                    caminho.append(atual)
                    atual = anteriores[atual]
                caminho.reverse()
                print(f"{origem} → {v}: distância = {distancias[v]}, caminho = {' → '.join(caminho)}")