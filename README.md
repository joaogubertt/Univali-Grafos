# Univali-Grafos
É um projeto incremental onde vamos implementar a utilização de grafos, as especificações até agora foram as seguintes:

# Classe Grafos

## Implementação
A implementação desta estrutura de **grafos** está sendo feita em **Python**.

## Estrutura da Classe
A classe **Grafos** deve ser construída considerando duas características principais:
- **Direcionado ou não**: Define se as arestas têm uma direção específica ou se são bidirecionais.
- **Ponderado ou não**: Define se as arestas possuem pesos ou se são todas de peso unitário.

Essas escolhas influenciam diretamente na forma como as arestas são inseridas.

## Especializações da Classe Grafos
A classe Grafos terá duas implementações especializadas:
1. **GrafoMatriz**: Representação do grafo utilizando uma **matriz de adjacência**.
2. **GrafoLista**: Representação do grafo utilizando uma **lista de adjacência** com uma estrutura auxiliar chamada **Aresta**.

---

## 📌 Funções Implementadas

### 🔹 `bool inserirVertice(string label)`
Adiciona um novo vértice ao grafo, sem nenhuma aresta associada.  
- O vértice deve ser adicionado à estrutura de armazenamento de vértices.
- Se for um **GrafoMatriz**, deve-se alocar espaço na matriz.
- Se for um **GrafoLista**, um novo nó deve ser criado na lista de adjacência.

### 🔹 `bool removerVertice(int indice)`
Remove um vértice do grafo:
- No **GrafoMatriz**, elimina a linha e a coluna correspondente na matriz.
- No **GrafoLista**, remove todas as referências ao vértice na lista de adjacência.
- Todas as arestas associadas ao vértice são removidas.

### 🔹 `string labelVertice(int indice)`
Retorna o **rótulo** de um vértice baseado no seu índice.

### 🔹 `void imprimeGrafo()`
Imprime a estrutura do grafo no console.  
- A saída deve ser similar à representação dos slides (sem a grade da matriz).

### 🔹 `bool inserirAresta(int origem, int destino, int peso = 1)`
Adiciona uma aresta entre dois vértices.  
- Se o grafo for **ponderado**, o peso deve ser armazenado corretamente.
- Se o grafo for **direcionado**, a aresta será adicionada apenas na direção especificada.
- Se o grafo for **não direcionado**, uma aresta de retorno também deve ser inserida.

### 🔹 `bool removerAresta(int origem, int destino)`
Remove uma aresta entre dois vértices.  
- Se o grafo for **não direcionado**, a aresta de retorno também deve ser removida.

### 🔹 `bool existeAresta(int origem, int destino)`
Verifica se existe uma aresta entre dois vértices.  
- A implementação varia entre matriz de adjacência e lista de adjacência.

### 🔹 `float pesoAresta(int origem, int destino)`
Retorna o **peso** de uma aresta.  
- A implementação varia entre matriz de adjacência e lista de adjacência.

### 🔹 `vector<int> retornarVizinhos(int vertice)`
Retorna todos os **vizinhos** de um vértice.  
- Essencial para os algoritmos de busca e travessia do grafo.

---

### 📌 Observações
- O tratamento de **direção** e **peso** das arestas deve ser levado em conta em todas as funções.
- A estrutura do código deve ser modular e permitir fácil extensão para novos algoritmos de grafos.
