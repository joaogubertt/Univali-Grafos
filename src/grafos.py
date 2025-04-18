from collections import deque
import heapq

RED = "\033[91m"  # Vermelho
GREEN = "\033[92m"  # Verde
PURPLE = "\033[95m" #Roxo
RESET = "\033[0m"  #Reseta cor 

class Grafos:
    def __init__(self, direcionado=False, ponderado=False):
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.vertices = []

    def labelVertice(self, indice: int) -> str:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def inserirVertice(self, label: str) -> bool:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def imprimeGrafo(self) -> None:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def inserirAresta(self, origem, destino, peso: float = 1.0) -> bool:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def removerVertice(self, indice: int) -> bool:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def removerAresta(self, *args) -> bool:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def existeAresta(self, origem: int, destino: int) -> bool:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def pesoAresta(self, origem: int, destino: int) -> float:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")

    def retornarVizinhos(self, vertice: int) -> list:
        raise NotImplementedError("Método deve ser implementado nas classes filhas")
    
    def busca_em_largura(self, vertice_origem):
        raise NotImplementedError("Método deve ser implementado nas classes filhas")
    
    def busca_em_profundidade(self, vertice_origem):
        raise NotImplementedError("Método deve ser implementado nas classes filhas")    

    @staticmethod
    def carregar_grafo_arquivo(grafo, caminho_arquivo: str) -> bool:
        """
        Carrega um grafo a partir de um arquivo de texto no formato especificado.
        
        Parâmetros:
            grafo: Instância de GrafoLista ou GrafoMatriz
            caminho_arquivo: Caminho para o arquivo de texto
        
        Returns:
            bool: True se o carregamento foi bem-sucedido, False caso contrário
        """
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                primeira_linha = arquivo.readline().strip().split()
                if len(primeira_linha) < 4:
                    print(f"{RED}Formato de arquivo inválido. Primeira linha deve conter V A D P{RESET}")
                    return False
                    
                V = int(primeira_linha[0])  # Número de vértices
                A = int(primeira_linha[1])  # Número de arestas
                D = int(primeira_linha[2])  # Direcionado (1) ou não (0)
                P = int(primeira_linha[3])  # Ponderado (1) ou não (0)
                
                if D == 1 and not grafo.direcionado:
                    print(f"{RED}Arquivo indica grafo direcionado, mas grafo fornecido não é direcionado{RESET}")
                    return False
                if D == 0 and grafo.direcionado:
                    print(f"{RED}Arquivo indica grafo não direcionado, mas grafo fornecido é direcionado{RESET}")
                    return False
                if P == 1 and not grafo.ponderado:
                    print(f"{RED}Arquivo indica grafo ponderado, mas grafo fornecido não é ponderado{RESET}")
                    return False
                if P == 0 and grafo.ponderado:
                    print(f"{RED}Arquivo indica grafo não ponderado, mas grafo fornecido é ponderado{RESET}")
                    return False
                
                for i in range(V):
                    grafo.inserirVertice(str(i))
                
                for _ in range(A):
                    linha_aresta = arquivo.readline().strip().split()
                    if not linha_aresta:
                        continue 
                        
                    if P == 1:  # Grafo ponderado
                        if len(linha_aresta) < 3:
                            print(f"{RED}Formato de aresta inválido para grafo ponderado. Esperado: origem destino peso{RESET}")
                            return False
                        origem = linha_aresta[0]
                        destino = linha_aresta[1]
                        peso = float(linha_aresta[2])
                        grafo.inserirAresta(origem, destino, peso)
                    else:  # Grafo não ponderado
                        if len(linha_aresta) < 2:
                            print(f"{RED}Formato de aresta inválido para grafo não ponderado. Esperado: origem destino{RESET}")
                            return False
                        origem = linha_aresta[0]
                        destino = linha_aresta[1]
                        grafo.inserirAresta(origem, destino)
                
                print(f"\n{GREEN}Grafo carregado com sucesso a partir do arquivo: {caminho_arquivo}{RESET}")
                return True
                
        except FileNotFoundError:
            print(f"{RED}Arquivo não encontrado: {caminho_arquivo}{RESET}")
            return False
        except Exception as e:
            print(f"{RED}Erro ao carregar grafo do arquivo: {e}{RESET}")
            return False

class GrafoLista(Grafos):
    def __init__(self, direcionado=False, ponderado=False):
        super().__init__(direcionado, ponderado)
        self.grafo_lista = []  # Lista de vértices
        self.arestas = []       # Lista de arestas

    def labelVertice(self, indice: int) -> str:
        try:
            return self.grafo_lista[indice].get("label")
        except IndexError as e:
            print(f"{RED} Índice não existente. {RESET}")
            return None

    def inserirVertice(self, label: str) -> bool:
        if any(vertice["label"] == label for vertice in self.grafo_lista):
            print("Já existe um vértice com essa label")
            return False
        else:
            self.grafo_lista.append({"label": label})
            print("Vértice inserido com sucesso.")
            return True

    def imprimeGrafo(self) -> None:
        if not self.grafo_lista:
            print("Grafo Lista ainda não possui vértices!")
            return

        print("\nRepresentação do Grafo:")
        for i in range(len(self.grafo_lista)):
            vertice_label = self.grafo_lista[i]["label"]
            vizinhos = self.retornarVizinhos(i)
            print(f'Vértice {i} ("{vertice_label}")')

            if not vizinhos:
                print("  Não possui vizinhos.")
            else:
                for vizinho_label in vizinhos:
                    destino = self.grafo_lista.index(next(v for v in self.grafo_lista if v["label"] == vizinho_label))
                    if self.ponderado:
                        peso = self.pesoAresta(i, destino)
                        print(f'  -> Vértice "{vizinho_label}" (Peso da aresta: {peso})')
                    else:
                        print(f'  -> Vértice "{vizinho_label}"')
        print()

    def inserirAresta(self, origem, destino, peso: float = 1.0) -> bool:
        # Verifica se os parâmetros são índices ou labels
        if isinstance(origem, int) and isinstance(destino, int):
            label_origem = self.labelVertice(origem)
            label_destino = self.labelVertice(destino)
        else:
            label_origem = origem
            label_destino = destino

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
            if self.ponderado:
                if self.direcionado:
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                else:
                    if label_origem == label_destino:
                        print(f"{RED}Impossível inserção de self-loop em grafo não direcionado. {RESET}")
                        return False
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": peso})
                    self.arestas.append({"origem": label_destino, "destino": label_origem, "peso": peso})
            else:
                if self.direcionado:
                    self.arestas.append({"origem": label_origem, "destino": label_destino, "peso": 1})
                else:
                    if label_origem == label_destino:
                        print(f"{RED}Impossível inserção de self-loop em grafo não direcionado. {RESET}")
                        return False
                    self.arestas.append({"origem": label_origem, "destino": label_destino})
                    self.arestas.append({"origem": label_destino, "destino": label_origem})
            print(f"{GREEN}Aresta inserida com sucesso. {RESET}")
            return True

    def removerVertice(self, indice: int) -> bool:
        try:
            if indice < 0 or indice >= len(self.grafo_lista):
                print(f"{RED}Vértice com índice não existente. {RESET}")
                return False

            label_indice_a_ser_excluido = self.labelVertice(indice)
            
            # Remove todas as arestas associadas ao vértice
            i = len(self.arestas) - 1
            while i >= 0:
                if i >= len(self.arestas):
                    i -= 1
                    continue
                    
                aresta = self.arestas[i]
                if (aresta["origem"] == label_indice_a_ser_excluido or aresta["destino"] == label_indice_a_ser_excluido):
                    self.arestas.pop(i)
                i -= 1
            
            self.grafo_lista.pop(indice)
            print(f"{GREEN}Vértice (e arestas associadas) com índice correspondente removido. {RESET}")
            return True
        except IndexError as e:
            print(f"{RED}Erro ao acessar índice: {e} {RESET}")
            return False

    def removerAresta(self, *args) -> bool:
        if len(args) == 1:  # Para compatibilidade com o main original
            indice = args[0]
            if indice < 0 or indice >= len(self.arestas):
                print(f"{RED}Aresta com índice não existente. {RESET}")
                return False
                
            label_origem = self.arestas[indice]["origem"]
            label_destino = self.arestas[indice]["destino"]
            
            # Remove todas as arestas correspondentes (para grafos não direcionados)
            i = len(self.arestas) - 1
            while i >= 0:
                if (self.arestas[i]["origem"] == label_origem and self.arestas[i]["destino"] == label_destino) or \
                   (not self.direcionado and self.arestas[i]["origem"] == label_destino and self.arestas[i]["destino"] == label_origem):
                    self.arestas.pop(i)
                i -= 1
            return True
            
        elif len(args) == 2:  # Nova interface com origem e destino
            origem, destino = args
            if isinstance(origem, int) and isinstance(destino, int):
                label_origem = self.labelVertice(origem)
                label_destino = self.labelVertice(destino)
            else:
                label_origem = origem
                label_destino = destino
                
            # Remove todas as arestas correspondentes
            i = len(self.arestas) - 1
            while i >= 0:
                if (self.arestas[i]["origem"] == label_origem and self.arestas[i]["destino"] == label_destino) or \
                   (not self.direcionado and self.arestas[i]["origem"] == label_destino and self.arestas[i]["destino"] == label_origem):
                    self.arestas.pop(i)
                i -= 1
            return True
        else:
            print(f"{RED}Número inválido de argumentos para removerAresta{RESET}")
            return False

    def existeAresta(self, origem: int, destino: int) -> bool:
        try:
            label_origem = self.labelVertice(origem)
            label_destino = self.labelVertice(destino)
        except:
            return False

        return any((aresta["origem"] == label_origem) and (aresta["destino"] == label_destino) for aresta in self.arestas)

    def pesoAresta(self, origem: int, destino: int) -> float:
        if not self.ponderado:
            print("grafo_lista não é ponderado")
            return 0.0
            
        try:
            label_origem = self.labelVertice(origem)
            label_destino = self.labelVertice(destino)
        except:
            print("Aresta c/ origem e destinos informados não existe")
            return 0.0
            
        for aresta in self.arestas:
            if aresta.get("origem") == label_origem and aresta.get("destino") == label_destino:
                return aresta.get("peso", 0.0)
        return 0.0

    def retornarVizinhos(self, vertice: str) -> list:
        try:
            label_vertice = self.labelVertice(vertice)
            vizinhos = []
            for aresta in self.arestas:
                if aresta["origem"] == label_vertice:
                    label_vertice_destino_vizinho = aresta["destino"]
                    if label_vertice_destino_vizinho not in vizinhos:
                        vizinhos.append(label_vertice_destino_vizinho)
                if not self.direcionado and aresta["destino"] == label_vertice:
                    label_vertice_origem_vizinho = aresta["origem"]
                    if label_vertice_origem_vizinho not in vizinhos:
                        vizinhos.append(label_vertice_origem_vizinho)
            return sorted(vizinhos)
        except IndexError:
            print(f"{RED} Vértice com índice não existe para retornar vizinhos{RESET}")
            return []

    def busca_em_largura(self, vertice_origem):
        labels = [v['label'] for v in self.grafo_lista]
        if vertice_origem not in labels:
            print(f"Vértice {vertice_origem} não está no grafo.")
            return

        visitados = set()
        fila = [vertice_origem]
        sequencia_bfs = []

        while fila:
            atual = fila.pop(0)
            if atual not in visitados:
                visitados.add(atual)
                sequencia_bfs.append(atual)

                # Pega vizinhos
                vizinhos = []
                for aresta in self.arestas:
                    origem_a = aresta['origem']
                    destino_a = aresta['destino']

                    if origem_a == atual:
                        vizinhos.append(destino_a)
                    elif not self.direcionado and destino_a == atual:
                        vizinhos.append(origem_a)

                for vizinho in vizinhos:
                    if vizinho not in visitados and vizinho not in fila:
                        fila.append(vizinho)

        print(f"Vértice {vertice_origem} - Sequência de visita BFS:", " → ".join(sequencia_bfs))

    def busca_em_profundidade(self, vertice_origem):
        labels = [v['label'] for v in self.grafo_lista]
        if vertice_origem not in labels:
            print(f"Vértice {vertice_origem} não está no grafo.")
            return

        visitados = set()
        sequencia_dfs = []

        # Pilha para simular a recursão
        pilha = [vertice_origem]

        while pilha:
            atual = pilha.pop()
            if atual not in visitados:
                visitados.add(atual)
                sequencia_dfs.append(atual)

                # Pega vizinhos
                vizinhos = []
                for aresta in self.arestas:
                    origem_a = aresta['origem']
                    destino_a = aresta['destino']

                    if origem_a == atual:
                        vizinhos.append(destino_a)
                    elif not self.direcionado and destino_a == atual:
                        vizinhos.append(origem_a)

                # Adiciona vizinhos na pilha (na ordem reversa para manter comportamento recursivo padrão)
                for vizinho in reversed(vizinhos):
                    if vizinho not in visitados:
                        pilha.append(vizinho)

        print(f"Vértice {vertice_origem} - Sequência de visita DFS:", " → ".join(sequencia_dfs))


    def dijkstra(self, vertice_origem):
        # Verifica se o vértice existe no grafo
        labels = [v['label'] for v in self.grafo_lista]
        if vertice_origem not in labels:
            print(f"Vértice {vertice_origem} não está no grafo.")
            return

        # Inicializa as distâncias como infinito e o vértice de origem como 0
        distancias = {v['label']: float('inf') for v in self.grafo_lista}
        distancias[vertice_origem] = 0

        # Predecessores para reconstruir caminho
        anteriores = {v['label']: None for v in self.grafo_lista}

        # Fila de prioridade (min-heap) com (distância, vértice)
        fila = [(0, vertice_origem)]

        while fila:
            dist_atual, atual = heapq.heappop(fila)

            # Procura vizinhos do vértice atual
            for aresta in self.arestas:
                origem = aresta['origem']
                destino = aresta['destino']
                peso = aresta.get('peso', 1)  # Assume 1 se não tiver peso

                # Verifica conexão considerando se é direcionado ou não
                if origem == atual:
                    vizinho = destino
                elif not self.direcionado and destino == atual:
                    vizinho = origem
                else:
                    continue

                nova_distancia = dist_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        print(f"Distâncias mínimas a partir do vértice {vertice_origem}:")
        for v in distancias:
            print(f"{vertice_origem} → {v}: {distancias[v]}")


class GrafoMatriz(Grafos):
    def __init__(self, direcionado=False, ponderado=False):
        super().__init__(direcionado, ponderado)
        self.grafo_matriz = []  # Matriz de adjacência

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
