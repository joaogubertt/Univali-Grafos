import time
from src.grafo_funcs import Grafo
from src.grafos import Grafos  # se a função carregar_grafo_arquivo estiver aqui

def main():
    # Testes com Prim
    print("==== Teste PRIM com grafo_prim.txt ====")
    grafo_prim1 = Grafo(ponderado=True, direcionado=False)
    
    if Grafos.carregar_grafo_arquivo(grafo_prim1, "data/grafos/testes T5/grafo_prim.txt"):
        inicio = time.time()
        arestas_prim1, custo_prim1, tempo_prim1 = grafo_prim1.prim("0")
        fim = time.time()
        print(f"\nCusto total da Árvore Geradora Mínima (Prim): {custo_prim1}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos\n")

    print("==== Teste PRIM com grafo_prim_grande.txt ====")
    grafo_prim2 = Grafo(ponderado=True, direcionado=False)
    
    if Grafos.carregar_grafo_arquivo(grafo_prim2, "data/grafos/testes T5/grafo_prim_grande.txt"):
        inicio = time.time()
        arestas_prim2, custo_prim2, tempo_prim2 = grafo_prim2.prim("0")
        fim = time.time()
        print(f"\nCusto total da Árvore Geradora Mínima (Prim): {custo_prim2}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos\n")

    # Testes com Kruskal
    print("\n==== Teste KRUSKAL com grafo_prim.txt ====")
    grafo_kruskal1 = Grafo(ponderado=True, direcionado=False)
    
    if Grafos.carregar_grafo_arquivo(grafo_kruskal1, "data/grafos/testes T5/grafo_prim.txt"):
        inicio = time.time()
        arestas_kruskal1, custo_kruskal1, tempo_kruskal1 = grafo_kruskal1.kruskal()
        fim = time.time()
        print(f"\nCusto total da Árvore Geradora Mínima (Kruskal): {custo_kruskal1}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos\n")

    print("==== Teste KRUSKAL com grafo_prim_grande.txt ====")
    grafo_kruskal2 = Grafo(ponderado=True, direcionado=False)
    
    if Grafos.carregar_grafo_arquivo(grafo_kruskal2, "data/grafos/testes T5/grafo_prim_grande.txt"):
        inicio = time.time()
        arestas_kruskal2, custo_kruskal2, tempo_kruskal2 = grafo_kruskal2.kruskal()
        fim = time.time()
        print(f"\nCusto total da Árvore Geradora Mínima (Kruskal): {custo_kruskal2}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos\n")

    # Comparação dos resultados
    print("\n==== Comparação dos Algoritmos ====")
    if 'custo_prim1' in locals() and 'custo_kruskal1' in locals():
        print(f"Grafo pequeno - Prim: {custo_prim1} | Kruskal: {custo_kruskal1}")
        print(f"Tempo Prim: {tempo_prim1:.6f} vs Kruskal: {tempo_kruskal1:.6f}")
    
    if 'custo_prim2' in locals() and 'custo_kruskal2' in locals():
        print(f"\nGrafo grande - Prim: {custo_prim2} | Kruskal: {custo_kruskal2}")
        print(f"Tempo Prim: {tempo_prim2:.6f} vs Kruskal: {tempo_kruskal2:.6f}")

if __name__ == "__main__":
    main()