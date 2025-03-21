from src.functions import Grafos, GrafoMatriz, GrafoLista

print("______________________________________________")
print("\nINICIANDO TESTES DA CLASSE GRAFOLISTA\n")
print("----------\n")
    
# Criando um grafo não-direcionado e ponderado
grafoL = GrafoLista(direcionado=False, ponderado=True)
    
# Inserindo vértices
grafoL.inserirVertice("A")
grafoL.inserirVertice("B")
grafoL.inserirVertice("C")
grafoL.inserirVertice("D")
print("Vértices inseridos com sucesso!\n")
    
# Inserindo arestas
grafoL.inserirAresta("A", "B", 5)  # A - B
grafoL.inserirAresta("B", "C", 3)  # B - C
grafoL.inserirAresta("C", "D", 2)  # C - D
grafoL.inserirAresta("D", "A", 4)  # D - A
print("Arestas inseridas com sucesso!\n")

# Imprimindo representação do grafo
grafoL.imprimeGrafo()
print("")
    
# Verificando existência de arestas
print(f"Existe aresta entre A e B? {grafoL.existeAresta(0, 1)}")
print(f"Existe aresta entre B e D? {grafoL.existeAresta(1, 3)}")
print("")
    
# Verificando pesos das arestas
print(f"Peso da aresta A - B: {grafoL.pesoAresta(0, 1)}")
print(f"Peso da aresta C - D: {grafoL.pesoAresta(2, 3)}")
print("\n")
    
# Retornando vizinhos
print(f"Vizinhos de A: {grafoL.retornarVizinhos(0)}")
print(f"Vizinhos de B: {grafoL.retornarVizinhos(1)}")
print("")
    
# Removendo uma aresta
grafoL.removerAresta(0)
print("Aresta entre A e B removida!\n")
    
# Imprimindo representação do grafo após remoção
grafoL.imprimeGrafo()


print("______________________________________________")
print("\nINICIANDO TESTES DA CLASSE GRAFOMATRIZ\n")
print("----------\n")
    
# Criando um grafo não-direcionado e ponderado
grafoM = GrafoMatriz(direcionado=False, ponderado=True)
    
# Inserindo vértices
grafoM.inserir_vertice("A")
grafoM.inserir_vertice("B")
grafoM.inserir_vertice("C")
grafoM.inserir_vertice("D")
print("Vértices inseridos com sucesso!\n")
    
# Inserindo arestas
grafoM.inserir_aresta(0, 1, 5)  # A - B
grafoM.inserir_aresta(1, 2, 3)  # B - C
grafoM.inserir_aresta(2, 3, 2)  # C - D
grafoM.inserir_aresta(3, 0, 4)  # D - A
print("Arestas inseridas com sucesso!\n")

# Imprimindo matriz de adjacência
print("\nMatriz de Adjacência:\n")
grafoM.imprimir_matriz()
print("")
    
# Verificando existência de arestas
print(f"Existe aresta entre A e B? {grafoM.existe_aresta(0, 1)}")
print(f"Existe aresta entre B e D? {grafoM.existe_aresta(1, 3)}")
print("")
    
# Verificando pesos das arestas
print(f"Peso da aresta A - B: {grafoM.peso_aresta(0, 1)}")
print(f"Peso da aresta C - D: {grafoM.peso_aresta(2, 3)}")
print("\n")
    
# Retornando vizinhos
print(f"Vizinhos de A: {grafoM.retornar_vizinhos(0)}")
print(f"Vizinhos de B: {grafoM.retornar_vizinhos(1)}")
print("")
    
# Removendo uma aresta
grafoM.remover_aresta(0, 1)
print("Aresta entre A e B removida!\n")
    
# Imprimindo matriz após remoção
print("Matriz de Adjacência após remoção da aresta A-B:\n")
grafoM.imprimir_matriz()
print("")
    
# Imprimindo representação do grafo
grafoM.imprime_grafo()


