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

