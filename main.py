from src.functions import Grafos, GrafoMatriz, GrafoLista

# Teste
grafo = GrafoMatriz(direcionado=False, ponderado=True)
grafo.inserir_vertice("A")
grafo.inserir_vertice("B")
grafo.inserir_vertice("C")

grafo.inserir_aresta(0, 1, 5)  # Adiciona uma aresta entre A e B com peso 5
grafo.inserir_aresta(1, 2, 3)  # Adiciona uma aresta entre B e C com peso 3

print("\nMatriz de adjacência:")
grafo.imprimir_matriz()

# Testando a função retornar_vizinhos
print("\nVizinhos do vértice A:", grafo.retornar_vizinhos(0))  # Deve retornar [1]
print("Vizinhos do vértice B:", grafo.retornar_vizinhos(1))  # Deve retornar [0, 2]
print("Vizinhos do vértice C:", grafo.retornar_vizinhos(2))  # Deve retornar [1]





"""grafo_lista = GrafoLista(ponderado=True, direcionado=True)
grafo_lista.labelVertice(1)
grafo_lista.inserirVertice("A")
grafo_lista.inserirVertice("B")
grafo_lista.inserirVertice("C")
grafo_lista.inserirAresta("A", "A", 2.0) #0
grafo_lista.inserirAresta("A", "B", 2.0) #1
grafo_lista.inserirAresta("C", "A", 5.2) #2
grafo_lista.inserirAresta("C", "B", 1.25) #2
print(grafo_lista.arestas)
grafo_lista.imprimeGrafo()
grafo_lista.removerVertice(0)
grafo_lista.imprimeGrafo()"""


# res = grafo_lista.pesoAresta(0, 1)
# print(f'Resultado: vai de {grafo_lista.grafo_lista[0]["label"]} a {grafo_lista.grafo_lista[1]["label"]} peso = {res} ')
# res = grafo_lista.pesoAresta(2, 0)
# print(f'Resultado: vai de {grafo_lista.grafo_lista[2]["label"]} a {grafo_lista.grafo_lista[0]["label"]} peso = {res}')
# res = grafo_lista.pesoAresta(0, 2)
# print(f'Resultado: vai de {grafo_lista.grafo_lista[0]["label"]} a {grafo_lista.grafo_lista[2]["label"]} peso = {res}')