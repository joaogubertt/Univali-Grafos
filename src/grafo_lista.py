from src.grafos import Grafos
import heapq, random
import itertools
import time
import time
from collections import defaultdict


RED = "\033[91m"  # Vermelho
GREEN = "\033[92m"  # Verde
PURPLE = "\033[95m" #Roxo
RESET = "\033[0m"  #Reseta cor 

class GrafoLista(Grafos):
    def __init__(self, direcionado=False, ponderado=False):
        super().__init__(direcionado, ponderado)
        self.grafo_lista = []  # Lista de vértices
        self.arestas = []       # Lista de arestas
        self.tipo_representacao = 'lista'
        self.heuristicas = {}  # dicionário de heurísticas
        self.lista_adjacencia = {}

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
            #print("Vértice inserido com sucesso.")
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
            #print(f"{GREEN}Aresta inserida com sucesso. {RESET}")
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

    def definirHeuristica(self, heuristicas: dict) -> None:
        """
        Define as heurísticas para os vértices do grafo.
        Parâmetro:
            heuristicas: dict {label: valor_heuristica}
        """
        for label, valor in heuristicas.items():
            if not any(v["label"] == label for v in self.grafo_lista):
                print(f"{RED}Vértice {label} não existe no grafo!{RESET}")
                continue
            self.heuristicas[label] = valor
        print(f"{GREEN}Heurísticas definidas com sucesso.{RESET}")

    def heuristica(self, indice: int) -> float:
        """
        Retorna a heurística associada ao vértice pelo índice.
        """
        label = self.labelVertice(indice)
        return self.heuristicas.get(label, float('inf'))  # se não existir, retorna infinito

    def gerarHeuristicaAleatoria(self, minimo=1, maximo=10) -> None:
        """
        Gera heurísticas aleatórias para todos os vértices.
        """
        for vertice in self.grafo_lista:
            self.heuristicas[vertice["label"]] = random.randint(minimo, maximo)
        print(f"{GREEN}Heurísticas aleatórias geradas com sucesso.{RESET}")

    def dsatur(self):
        if not self.grafo_lista:
            return {}

        num_vertices = len(self.grafo_lista)
        cores = [0] * num_vertices  # Inicializa todas as cores com 0 (não None)
        print("passou 1")
        graus = [len(self.retornarVizinhos(i)) for i in range(num_vertices)]
        print("passou 2")
        # Ordena vértices por grau decrescente
        vertices_ordenados = sorted(range(num_vertices), key=lambda x: -graus[x])
        
        for v in vertices_ordenados:
            vizinhos = self.retornarVizinhos(v)
            cores_vizinhos = set()
            
            for vizinho in vizinhos:
                vizinho_idx = next(i for i, vert in enumerate(self.grafo_lista) if vert['label'] == vizinho)
                #print("adicionou")
                cores_vizinhos.add(cores[vizinho_idx])
            
            # Encontra a menor cor disponível
            cor = 0
            while cor in cores_vizinhos:
                cor += 1
            cores[v] = cor
        
        return {self.grafo_lista[i]['label']: cores[i] for i in range(num_vertices)}


    def coloracao_forca_bruta(grafo):
        """Implementação do método de força bruta para coloração de grafos"""
        inicio = time.time()
        vertices = [v['label'] for v in grafo.grafo_lista]
        num_vertices = len(vertices)
        
        if num_vertices == 0:
            return (0, {}, 0.0)
        
        # Converte arestas para índices
        arestas_indices = []
        for aresta in grafo.arestas:
            origem = next(i for i, v in enumerate(grafo.grafo_lista) if v['label'] == aresta['origem'])
            destino = next(i for i, v in enumerate(grafo.grafo_lista) if v['label'] == aresta['destino'])
            arestas_indices.append((origem, destino))
            if not grafo.direcionado:
                arestas_indices.append((destino, origem))
        
        # Testa combinações de cores
        for k in range(1, num_vertices + 1):
            for coloracao in itertools.product(range(k), repeat=num_vertices):
                valido = True
                for origem, destino in arestas_indices:
                    if coloracao[origem] == coloracao[destino]:
                        valido = False
                        break
                if valido:
                    tempo = time.time() - inicio
                    coloracao_dict = {vertices[i]: coloracao[i] for i in range(num_vertices)}
                    return (k, coloracao_dict, tempo)
        
        tempo = time.time() - inicio
        return (num_vertices, {v: i for i, v in enumerate(vertices)}, tempo)
        


    def welsh_powell(self):
        """
        Implementação da heurística Welsh-Powell para coloração de grafos.
        Ordena os vértices por grau decrescente e atribui cores de forma gulosa.
        
        Retorna:
            tuple: (num_cores, coloracao, tempo_execucao)
        """
        inicio = time.time()
        
        # Se não há vértices, retorna vazio
        if not self.grafo_lista:
            return (0, {}, 0)
        
        # 1. Preparação das estruturas de dados
        labels = [v['label'] for v in self.grafo_lista]
        label_to_index = {label: i for i, label in enumerate(labels)}
        num_vertices = len(self.grafo_lista)
        print("passou 1")
        # 2. Calcula o grau de cada vértice
        graus = []
        for i in range(num_vertices):
            vizinhos = self.retornarVizinhos(i)
            graus.append((i, len(vizinhos)))  # (índice, grau)
        print("passou 2")
        # 3. Ordena vértices por grau decrescente
        graus.sort(key=lambda x: -x[1])
        vertices_ordenados = [x[0] for x in graus]  # Lista de índices ordenados
        
        # 4. Inicialização das estruturas para coloração
        cores = [None] * num_vertices
        cor_atual = 0
        
        # 5. Processamento dos vértices na ordem estabelecida
        while None in cores:
            for v in vertices_ordenados:
                if cores[v] is not None:
                    continue  # Vértice já colorido
                    
                # Verifica se a cor atual pode ser usada 
                pode_usar_cor = True
                vizinhos = self.retornarVizinhos(v)
                
                for vizinho in vizinhos:
                    vizinho_idx = label_to_index[vizinho]
                    if cores[vizinho_idx] == cor_atual:
                        pode_usar_cor = False
                        break
                        
                if pode_usar_cor:
                    cores[v] = cor_atual
                    
            cor_atual += 1
        
        # 6. Prepara o resultado
        fim = time.time()
        tempo_execucao = fim - inicio
        
        coloracao = {labels[i]: cores[i] for i in range(num_vertices)}
        
        return (cor_atual, coloracao, tempo_execucao)
    

    def dfs(self, origem, destino, caminho, visitados, grafo_residual):
        visitados.add(origem)
        if origem == destino:
            return True

        for aresta in grafo_residual.arestas:
            if aresta["origem"] == origem and aresta["peso"] > 0:
                vizinho = aresta["destino"]
                if vizinho not in visitados:
                    caminho[vizinho] = origem
                    if self.dfs(vizinho, destino, caminho, visitados, grafo_residual):
                        return True
        return False

    def copiar_grafo(self):
        novo_grafo = GrafoLista()
        novo_grafo.ponderado = self.ponderado
        novo_grafo.direcionado = True  # Fluxo é sempre direcionado

        for v in self.grafo_lista:
            novo_grafo.inserirVertice(v["label"])

        for a in self.arestas:
            origem = a["origem"]
            destino = a["destino"]
            peso = a.get("peso", 1)
            novo_grafo.inserirAresta(origem, destino, peso)

        return novo_grafo

    def ford_fulkerson(self, origem, destino):
        grafo_residual = self.copiar_grafo()
        fluxo_maximo = 0

        while True:
            visitados = set()
            caminho = {}

            if not self.dfs(origem, destino, caminho, visitados, grafo_residual):
                break

            # Determina o fluxo possível no caminho aumentante
            fluxo_caminho = float('inf')
            v = destino
            while v != origem:
                u = caminho[v]
                for aresta in grafo_residual.arestas:
                    if aresta["origem"] == u and aresta["destino"] == v:
                        fluxo_caminho = min(fluxo_caminho, aresta["peso"])
                        break
                v = u

            # Atualiza capacidades no grafo residual
            v = destino
            while v != origem:
                u = caminho[v]
                for aresta in grafo_residual.arestas:
                    if aresta["origem"] == u and aresta["destino"] == v:
                        aresta["peso"] -= fluxo_caminho
                        break

                # Adiciona ou atualiza a aresta reversa
                reversa_existente = False
                for aresta in grafo_residual.arestas:
                    if aresta["origem"] == v and aresta["destino"] == u:
                        aresta["peso"] += fluxo_caminho
                        reversa_existente = True
                        break
                if not reversa_existente:
                    grafo_residual.inserirAresta(v, u, fluxo_caminho)

                v = u

            fluxo_maximo += fluxo_caminho

        return fluxo_maximo
    
    def busca_local(self, origem, destino):
        print("\n=== Iniciando Busca Local ===")
        fluxo_original = self.ford_fulkerson(origem, destino)
        melhor_fluxo = fluxo_original
        passos = 0

        # Cópia da configuração original das arestas
        melhor_arestas = list(self.arestas)

        melhoria = True

        while melhoria:
            melhoria = False
            for i in range(len(melhor_arestas)):
                # Copia as arestas atuais
                vizinho_arestas = list(melhor_arestas)

                aresta = vizinho_arestas[i]

                # Evita self-loop
                if aresta["origem"] == aresta["destino"]:
                    continue

                # Inverte a aresta
                aresta_invertida = {
                    "origem": aresta["destino"],
                    "destino": aresta["origem"],
                    "peso": aresta["peso"]
                }

                # Verifica se já existe essa aresta invertida
                if any(a["origem"] == aresta_invertida["origem"] and a["destino"] == aresta_invertida["destino"] for a in vizinho_arestas):
                    continue

                # Substitui a aresta pela invertida
                vizinho_arestas[i] = aresta_invertida

                # Testa fluxo máximo nesse vizinho
                self.arestas = vizinho_arestas
                fluxo_vizinho = self.ford_fulkerson(origem, destino)
                passos += 1

                # Se melhorou, salva e continua
                if fluxo_vizinho > melhor_fluxo:
                    print(f"Passo {passos}: melhoria encontrada! Fluxo = {fluxo_vizinho}")
                    melhor_fluxo = fluxo_vizinho
                    melhor_arestas = list(vizinho_arestas)
                    melhoria = True
                    break  # Reinicia a busca a partir dessa configuração melhorada

            self.arestas = melhor_arestas  # atualiza para a melhor até aqui

        print(f"\nFluxo original: {fluxo_original}")
        print(f"Fluxo após busca local: {melhor_fluxo}")
        print(f"Número de passos: {passos}")


