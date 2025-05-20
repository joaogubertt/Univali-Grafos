from src.grafos import Grafos
from src.grafo_matriz import GrafoMatriz
from src.grafo_lista import GrafoLista
 
def m2():

    print("""
          
░█▀▀█ ░█▀▀█ ▀█▀ ░█▀▄▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█▄▄█ ░█▄▄▀ ░█─ ░█░█░█ ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█─── ░█─░█ ▄█▄ ░█──░█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_01 = GrafoLista(direcionado=False, ponderado=False)
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

    print("\n")

    print("""

░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ░█─░█ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─▀▀▀▄▄ ░█▀▀▀ ░█─▄▄ ░█─░█ ░█░█░█ ░█─░█ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█▄▄▄█ ░█▄▄▄ ░█▄▄█ ─▀▄▄▀ ░█──▀█ ░█▄▄▀ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_02 = GrafoLista(direcionado=True, ponderado=True)
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

    print("\n")

    print("""
          
▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─░█── ░█▀▀▀ ░█▄▄▀ ░█─── ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
─░█── ░█▄▄▄ ░█─░█ ░█▄▄█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_03 = GrafoMatriz(direcionado=False, ponderado=False)
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
    

    print("\n")

    print("""
          

░█▀▀█ ░█─░█ ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█─░█ ░█─░█ ░█▄▄█ ░█▄▄▀ ─░█── ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
─▀▀█▄ ─▀▄▄▀ ░█─░█ ░█─░█ ─░█── ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_04 = GrafoLista(direcionado=False, ponderado=False)
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

    print("\n")

def main():
    g = GrafoLista(direcionado=True, ponderado=True)
    g.inserirVertice("A")
    g.inserirVertice("B")
    g.inserirVertice("C")

    # Definindo manualmente
    g.definirHeuristica({"A": 5, "B": 3, "C": 1})

    # Ou gerar aleatório
    g.gerarHeuristicaAleatoria()

    # Pegar heurística de um vértice (por índice)
    print(g.heuristica(0))  # heurística de A
    
if __name__ == "__main__":
    main()
    
    '''teste1 = GrafoLista(direcionado=False, ponderado=True)
    Grafos.carregar_grafo_arquivo(teste1, "data/grafos/testes M2/slides.txt")

    teste1.busca_em_largura("4")
    teste1.busca_em_profundidade("4")
    teste1.dijkstra("4")'''