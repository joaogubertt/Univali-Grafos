# Arquivos de Grafos para Teste

Abaixo estão quatro grafos em arquivos `.txt`, criados para fins de teste com diferentes configurações:

---

## 📄 grafo1.txt

- **Número de vértices**: 3  
- **Número de arestas**: 2  
- **Direcionado**: Não  
- **Ponderado**: Não  
- **Arestas**:  
  - (0 — 1)  
  - (1 — 2)  

---

## 📄 grafo2.txt

- **Número de vértices**: 4  
- **Número de arestas**: 4  
- **Direcionado**: Sim  
- **Ponderado**: Sim  
- **Arestas com pesos**:  
  - 0 → 1 (peso 3)  
  - 1 → 2 (peso 2)  
  - 2 → 3 (peso 4)  
  - 3 → 0 (peso 5)

---

## 📄 grafo3.txt

- **Número de vértices**: 5  
- **Número de arestas**: 5  
- **Direcionado**: Não  
- **Ponderado**: Sim  
- **Arestas com pesos**:  
  - (0 — 1, peso 2)  
  - (0 — 2, peso 4)  
  - (1 — 3, peso 3)  
  - (3 — 4, peso 1)  
  - (2 — 4, peso 5)

---

## 📄 grafo4.txt

- **Número de vértices**: 6  
- **Número de arestas**: 7  
- **Direcionado**: Não  
- **Ponderado**: Não  
- **Arestas**:  
  - (0 — 1)  
  - (0 — 2)  
  - (1 — 3)  
  - (1 — 4)  
  - (2 — 4)  
  - (3 — 5)  
  - (4 — 5)

---

# 🔍 Resultados das Buscas em Largura (BFS) e Profundidade (DFS)

---

## 📄 grafo1.txt

- **Ordem de visita BFS**:
  - Vértice 0 → 0 → 1 → 2  
  - Vértice 1 → 1 → 0 → 2  
  - Vértice 2 → 2 → 1 → 0  

- **Ordem de visita DFS**:
  - Vértice 0 → 0 → 1 → 2  
  - Vértice 1 → 1 → 0 → 2  
  - Vértice 2 → 2 → 1 → 0  

---

## 📄 grafo2.txt

- **Ordem de visita BFS**:
  - Vértice 0 → 0 → 1 → 2 → 3  
  - Vértice 1 → 1 → 2 → 3 → 0  
  - Vértice 2 → 2 → 3 → 0 → 1  
  - Vértice 3 → 3 → 0 → 1 → 2  

- **Ordem de visita DFS**:
  - Vértice 0 → 0 → 1 → 2 → 3  
  - Vértice 1 → 1 → 2 → 3 → 0  
  - Vértice 2 → 2 → 3 → 0 → 1  
  - Vértice 3 → 3 → 0 → 1 → 2  

---

## 📄 grafo3.txt

- **Ordem de visita BFS**:
  - Vértice 0 → 0 → 1 → 2 → 3 → 4  
  - Vértice 1 → 1 → 0 → 3 → 2 → 4  
  - Vértice 2 → 2 → 0 → 4 → 1 → 3  
  - Vértice 3 → 3 → 1 → 4 → 0 → 2  
  - Vértice 4 → 4 → 3 → 2 → 1 → 0  

- **Ordem de visita DFS**:
  - Vértice 0 → 0 → 1 → 3 → 4 → 2  
  - Vértice 1 → 1 → 0 → 2 → 4 → 3  
  - Vértice 2 → 2 → 0 → 1 → 3 → 4  
  - Vértice 3 → 3 → 1 → 0 → 2 → 4  
  - Vértice 4 → 4 → 3 → 1 → 0 → 2  

---

## 📄 grafo4.txt

- **Ordem de visita BFS**:
  - Vértice 0 → 0 → 1 → 2 → 3 → 4 → 5  
  - Vértice 1 → 1 → 0 → 3 → 4 → 2 → 5  
  - Vértice 2 → 2 → 0 → 4 → 1 → 5 → 3  
  - Vértice 3 → 3 → 1 → 5 → 0 → 4 → 2  
  - Vértice 4 → 4 → 1 → 2 → 5 → 0 → 3  
  - Vértice 5 → 5 → 3 → 4 → 1 → 0 → 2  

- **Ordem de visita DFS**:
  - Vértice 0 → 0 → 1 → 3 → 5 → 4 → 2  
  - Vértice 1 → 1 → 0 → 2 → 4 → 5 → 3  
  - Vértice 2 → 2 → 0 → 1 → 3 → 5 → 4  
  - Vértice 3 → 3 → 1 → 0 → 2 → 4 → 5  
  - Vértice 4 → 4 → 1 → 0 → 2 → 3 → 5  
  - Vértice 5 → 5 → 3 → 1 → 0 → 2 → 4  

---
