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
    def carregar_grafo_arquivo(grafo, caminho_arquivo: str, batch_size=1000) -> bool:
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                # Ler e validar cabeçalho
                primeira_linha = arquivo.readline().strip().split()
                if len(primeira_linha) < 4:
                    print(f"{RED}Formato de arquivo inválido. Primeira linha deve conter V A D P{RESET}")
                    return False

                V = int(primeira_linha[0])
                A = int(primeira_linha[1])
                D = int(primeira_linha[2])
                P = int(primeira_linha[3])

                # Validações
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

                # Adicionar vértices corretamente
                for i in range(V):
                    grafo.inserirVertice(str(i))

                # Processar arestas em lote
                batch = []
                contagem = 0

                for linha in arquivo:
                    linha_aresta = linha.strip().split()
                    if not linha_aresta:
                        continue

                    if P == 1:
                        if len(linha_aresta) < 3:
                            print(f"{RED}Formato de aresta inválido para grafo ponderado{RESET}")
                            return False
                        origem, destino, peso = linha_aresta[0], linha_aresta[1], float(linha_aresta[2])
                    else:
                        if len(linha_aresta) < 2:
                            print(f"{RED}Formato de aresta inválido para grafo não ponderado{RESET}")
                            return False
                        origem, destino = linha_aresta[0], linha_aresta[1]
                        peso = 1.0

                    batch.append((origem, destino, peso))
                    contagem += 1

                    if len(batch) >= batch_size:
                        for origem, destino, peso in batch:
                            grafo.inserirAresta(origem, destino, peso)
                        batch = []

                # Processar último lote
                if batch:
                    for origem, destino, peso in batch:
                        grafo.inserirAresta(origem, destino, peso)

                print(f"\n{GREEN}Grafo carregado com sucesso: {V} vértices, {contagem} arestas{RESET}")
                return True

        except FileNotFoundError:
            print(f"{RED}Arquivo não encontrado: {caminho_arquivo}{RESET}")
            return False
        except Exception as e:
            print(f"{RED}Erro ao carregar grafo: {str(e)}{RESET}")
            return False

    def processar_batch(grafo, batch, ponderado, direcionado):
        """Função auxiliar para processar um lote de arestas"""
        for aresta in batch:
            origem, destino, peso = aresta
            if ponderado:
                grafo.arestas.append({"origem": origem, "destino": destino, "peso": peso})
                if not direcionado:
                    grafo.arestas.append({"origem": destino, "destino": origem, "peso": peso})
            else:
                grafo.arestas.append({"origem": origem, "destino": destino})
                if not direcionado:
                    grafo.arestas.append({"origem": destino, "destino": origem})
