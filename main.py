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
grafoM.inserirVertice("A")
grafoM.inserirVertice("B")
grafoM.inserirVertice("C")
grafoM.inserirVertice("D")
print("Vértices inseridos com sucesso!\n")
    
# Inserindo arestas
grafoM.inserirAresta(0, 1, 5)  # A - B
grafoM.inserirAresta(1, 2, 3)  # B - C
grafoM.inserirAresta(2, 3, 2)  # C - D
grafoM.inserirAresta(3, 0, 4)  # D - A
print("Arestas inseridas com sucesso!\n")

# Imprimindo matriz de adjacência
print("\nMatriz de Adjacência:\n")
grafoM.imprimeGrafo()
print("")
    
# Verificando existência de arestas
print(f"Existe aresta entre A e B? {grafoM.existeAresta(0, 1)}")
print(f"Existe aresta entre B e D? {grafoM.existeAresta(1, 3)}")
print("")
    
# Verificando pesos das arestas
print(f"Peso da aresta A - B: {grafoM.pesoAresta(0, 1)}")
print(f"Peso da aresta C - D: {grafoM.pesoAresta(2, 3)}")
print("\n")
    
# Retornando vizinhos
print(f"Vizinhos de A: {grafoM.retornarVizinhos(0)}")
print(f"Vizinhos de B: {grafoM.retornarVizinhos(1)}")
print("")
    
# Removendo uma aresta
grafoM.removerAresta(0, 1)
print("Aresta entre A e B removida!\n")
    
# Imprimindo matriz após remoção
print("Matriz de Adjacência após remoção da aresta A-B:\n")
grafoM.imprimeGrafo()
print("")
    
# Imprimindo representação do grafo
grafoM.imprimeGrafo()


