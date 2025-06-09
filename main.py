from src.grafos import Grafos
from src.grafo_matriz import GrafoMatriz
from src.grafo_lista import GrafoLista
from src.grafos import Grafos
from src.grafo_matriz import GrafoMatriz
from src.grafo_lista import GrafoLista
 
def m1():

    print("""
          
░█▀▀█ ░█▀▀█ ▀█▀ ░█▀▄▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█▄▄█ ░█▄▄▀ ░█─ ░█░█░█ ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█─── ░█─░█ ▄█▄ ░█──░█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_01 = GrafoLista(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo_teste_01, "data/grafos/testes M2/grafo_teste_01.txt")
    Grafos.carregar_grafo_arquivo(grafo_teste_01, "data/grafos/testes M2/grafo_teste_01.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_01.busca_em_largura("0")
    grafo_teste_01.busca_em_largura("1")
    grafo_teste_01.busca_em_largura("2")
    print("-")
    grafo_teste_01.busca_em_profundidade("0")
    grafo_teste_01.busca_em_profundidade("1")
    grafo_teste_01.busca_em_profundidade("2")
    print("-")
    grafo_teste_01.dijkstra("0")
    print("-")
    grafo_teste_01.dijkstra("0")

    print("\n")

    print("""

░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ░█─░█ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─▀▀▀▄▄ ░█▀▀▀ ░█─▄▄ ░█─░█ ░█░█░█ ░█─░█ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█▄▄▄█ ░█▄▄▄ ░█▄▄█ ─▀▄▄▀ ░█──▀█ ░█▄▄▀ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_02 = GrafoLista(direcionado=True, ponderado=True)
    Grafos.carregar_grafo_arquivo(grafo_teste_02, "data/grafos/testes M2/grafo_teste_02.txt")
    Grafos.carregar_grafo_arquivo(grafo_teste_02, "data/grafos/testes M2/grafo_teste_02.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_02.busca_em_largura("0")
    grafo_teste_02.busca_em_largura("1")
    grafo_teste_02.busca_em_largura("2")
    grafo_teste_02.busca_em_largura("3")
    print("-")
    grafo_teste_02.busca_em_profundidade("0")
    grafo_teste_02.busca_em_profundidade("1")
    grafo_teste_02.busca_em_profundidade("2")
    grafo_teste_02.busca_em_profundidade("3")
    print("-")
    grafo_teste_02.dijkstra("0")
    grafo_teste_02.dijkstra("1")
    grafo_teste_02.dijkstra("2")
    grafo_teste_02.dijkstra("3")
    grafo_teste_02.dijkstra("4")
    print("-")
    grafo_teste_02.dijkstra("0")
    grafo_teste_02.dijkstra("1")
    grafo_teste_02.dijkstra("2")
    grafo_teste_02.dijkstra("3")
    grafo_teste_02.dijkstra("4")

    print("\n")

    print("""
          
▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─░█── ░█▀▀▀ ░█▄▄▀ ░█─── ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
─░█── ░█▄▄▄ ░█─░█ ░█▄▄█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_03 = GrafoMatriz(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo_teste_03, "data/grafos/testes M2/grafo_teste_03.txt")
    Grafos.carregar_grafo_arquivo(grafo_teste_03, "data/grafos/testes M2/grafo_teste_03.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_03.busca_em_largura("0")
    grafo_teste_03.busca_em_largura("1")
    grafo_teste_03.busca_em_largura("2")
    grafo_teste_03.busca_em_largura("3")
    grafo_teste_03.busca_em_largura("4")
    print("-")
    grafo_teste_03.busca_em_profundidade("0")
    grafo_teste_03.busca_em_profundidade("1")
    grafo_teste_03.busca_em_profundidade("2")
    grafo_teste_03.busca_em_profundidade("3")
    grafo_teste_03.busca_em_profundidade("4")
    print("-")
    grafo_teste_03.dijkstra("0")
    grafo_teste_03.dijkstra("1")
    grafo_teste_03.dijkstra("2")
    grafo_teste_03.dijkstra("3")
    grafo_teste_03.dijkstra("4")
    
    print("-")
    grafo_teste_03.dijkstra("0")
    grafo_teste_03.dijkstra("1")
    grafo_teste_03.dijkstra("2")
    grafo_teste_03.dijkstra("3")
    grafo_teste_03.dijkstra("4")
    

    print("\n")

    print("""
          

░█▀▀█ ░█─░█ ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█─░█ ░█─░█ ░█▄▄█ ░█▄▄▀ ─░█── ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
─▀▀█▄ ─▀▄▄▀ ░█─░█ ░█─░█ ─░█── ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_04 = GrafoLista(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo_teste_04, "data/grafos/testes M2/grafo_teste_04.txt")
    Grafos.carregar_grafo_arquivo(grafo_teste_04, "data/grafos/testes M2/grafo_teste_04.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_04.busca_em_largura("0")
    grafo_teste_04.busca_em_largura("1")
    grafo_teste_04.busca_em_largura("2")
    grafo_teste_04.busca_em_largura("3")
    grafo_teste_04.busca_em_largura("4")
    print("-")
    grafo_teste_04.busca_em_profundidade("0")
    grafo_teste_04.busca_em_profundidade("1")
    grafo_teste_04.busca_em_profundidade("2")
    grafo_teste_04.busca_em_profundidade("3")
    grafo_teste_04.busca_em_profundidade("4")
    print("-")
    grafo_teste_04.dijkstra("0")
    grafo_teste_04.dijkstra("1")
    grafo_teste_04.dijkstra("2")
    grafo_teste_04.dijkstra("3")
    grafo_teste_04.dijkstra("4")
    print("-")
    grafo_teste_04.dijkstra("0")
    grafo_teste_04.dijkstra("1")
    grafo_teste_04.dijkstra("2")
    grafo_teste_04.dijkstra("3")
    grafo_teste_04.dijkstra("4")

    print("\n")

import time

RED = "\033[91m"
RESET = "\033[0m"

def main():
    print("="*50)
    print("TESTE DE COLORAÇÃO DE GRAFOS".center(50))
    print("="*50)
    
    grafo = GrafoLista(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo, "data/grafos/testes M3/r1000-234-234.txt")
    
    """(# Adiciona vértices (um grafo com 7 vértices)
    vertices = [f"V{i}" for i in range(7)]
    for v in vertices:
        grafo.inserirVertice(v)
    
    # Adiciona arestas (grafo planar)
    arestas = [
        ("V0", "V1"), ("V0", "V2"), ("V0", "V3"),
        ("V1", "V2"), ("V1", "V4"),
        ("V2", "V3"), ("V2", "V5"),
        ("V3", "V5"), ("V3", "V6"),
        ("V4", "V5"), 
        ("V5", "V6")
    ]
    
    for origem, destino in arestas:
        grafo.inserirAresta(origem, destino)"""
    
    print("\nGrafo criado com sucesso!")
    
    # Execução dos algoritmos
    print("\n" + "="*50)
    print("EXECUTANDO ALGORITMOS".center(50))
    print("="*50)
    
        # Welsh-Powell
    inicio_wp = time.time()
    num_cores_wp, coloracao_wp, _ = grafo.welsh_powell()
    tempo_wp = time.time() - inicio_wp
    
    # DSATUR com tratamento seguro
    inicio_ds = time.time()
    coloracao_ds = grafo.gerarHeuristicaAleatoria()
    tempo_ds = time.time() - inicio_ds
    
    # Força Bruta (apenas para grafos pequenos)
    num_cores_fb = -1
    coloracao_fb = {}
    tempo_fb = 0.0
    
    if len(grafo.grafo_lista) <= 15:  # Limite para força bruta
        inicio_fb = time.time()
        num_cores_fb, coloracao_fb, tempo_fb = grafo.coloracao_forca_bruta()
    else:
        print(f"\n{RED}Aviso: Força bruta não será executado para grafos com mais de 15 vértices{RESET}")
    
    # Calcula número de cores para DSATUR
    if coloracao_ds:
        try:
            num_cores_ds = max(coloracao_ds.values()) + 1
        except ValueError:
            print(f"{RED}Erro: DSATUR retornou coloração vazia{RESET}")
            num_cores_ds = 0
        except TypeError:
            print(f"{RED}Erro: Valores de cor inválidos no DSATUR{RESET}")
            num_cores_ds = -1
    else:
        print(f"{RED}Erro: DSATUR não retornou coloração{RESET}")
        num_cores_ds = -1
    
    # Exibição dos resultados
    print("\n" + "="*50)
    print("RESULTADOS".center(50))
    print("="*50)
    
    print(f"\n{'Método':<15} | {'Cores':<6} | {'Tempo (s)':<10} | Coloração")
    print("-"*60)
    
    # Mostra força bruta apenas se foi executado
    if num_cores_fb != -1:
        print(f"{'Força Bruta':<15} | {num_cores_fb:<6} | {tempo_fb:<10.6f} | {coloracao_fb}")
    
    print(f"{'Welsh-Powell':<15} | {num_cores_wp:<6} | {tempo_wp:<10.6f} | {coloracao_wp}")
    print(f"{'DSATUR':<15} | {num_cores_ds:<6} | {tempo_ds:<10.6f} | {coloracao_ds}")
    
if __name__ == "__main__":
    main()

    '''teste1 = GrafoLista(direcionado=False, ponderado=True)
    Grafos.carregar_grafo_arquivo(teste1, "data/grafos/testes M2/slides.txt")

    teste1.busca_em_largura("4")
    teste1.busca_em_profundidade("4")
    teste1.dijkstra("4")'''