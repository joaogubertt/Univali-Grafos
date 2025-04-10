from src.grafos import Grafos, GrafoMatriz, GrafoLista
 
def main():

    print("""
░█▀▀█ ░█▀▀█ ▀█▀ ░█▀▄▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█▄▄█ ░█▄▄▀ ░█─ ░█░█░█ ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█─── ░█─░█ ▄█▄ ░█──░█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_01 = GrafoLista(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo_teste_01, "data/grafos/grafo_teste_01.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_01.busca_em_largura("0")
    grafo_teste_01.busca_em_largura("1")
    grafo_teste_01.busca_em_largura("2")

    print("\n\n")

    print("""

░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ░█─░█ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─▀▀▀▄▄ ░█▀▀▀ ░█─▄▄ ░█─░█ ░█░█░█ ░█─░█ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
░█▄▄▄█ ░█▄▄▄ ░█▄▄█ ─▀▄▄▀ ░█──▀█ ░█▄▄▀ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_02 = GrafoLista(direcionado=True, ponderado=True)
    Grafos.carregar_grafo_arquivo(grafo_teste_02, "data/grafos/grafo_teste_02.txt")
    print("______________________________")

    print("\nBuscas:\n")
    grafo_teste_02.busca_em_largura("0")
    grafo_teste_02.busca_em_largura("1")
    grafo_teste_02.busca_em_largura("2")
    grafo_teste_02.busca_em_largura("3")

    print("\n\n")

    print("""


▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
─░█── ░█▀▀▀ ░█▄▄▀ ░█─── ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ 　 ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▀▀▀ ░█──░█ 
─░█── ░█▄▄▄ ░█─░█ ░█▄▄█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄█""")
    
    print("______________________________\n")
    grafo_teste_03 = GrafoMatriz(direcionado=False, ponderado=False)
    Grafos.carregar_grafo_arquivo(grafo_teste_03, "data/grafos/grafo_teste_03.txt")
    print("______________________________")

    grafo_teste_03.imprimeGrafo()
    print("\nBuscas:\n")
    grafo_teste_03.busca_em_largura("0")
    grafo_teste_03.busca_em_largura("1")
    grafo_teste_03.busca_em_largura("2")
    grafo_teste_03.busca_em_largura("3")
    grafo_teste_03.busca_em_largura("4")

    print("\n\n")
    
if __name__ == "__main__":
    main()