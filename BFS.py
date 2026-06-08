from collections import deque

# Ejemplo de grafo representado como un diccionario de adyacencia
# los agentes son como grafos, entonces el flujo lógico es un grafo dirigido y el flujo de movimientos debe ser validado para evitar ciclos infinitos o caminos sin salida.
grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

inicio = "A"
fin = "F"

cola = deque([(inicio, [inicio])])
visitados = set()

while cola:
    nodo, camino = cola.popleft()

    if nodo == fin:
        print("Camino más corto:")
        print(" -> ".join(camino))
        break

    if nodo not in visitados:
        visitados.add(nodo)

        for vecino in grafo[nodo]:
            cola.append((vecino, camino + [vecino]))