"""
Questão 4: Dijkstra
"""

from grafo import Grafo
from queue import PriorityQueue


def dijkstra(g: Grafo, origem: int):

    # inicializacao
    cardinalidade_v = g.qtdVertices()
    # para as seguintes listas cada vertice e indexado a partir de 0
    # sendo que o vertice v tera indice v - 1
    distancia = []
    antecessor = []
    visitados = []

    # estimativa de menor caminho - limite superior
    emc = float("inf")

    # cria lista de vertices
    for i in range(cardinalidade_v):
        distancia.append(emc)
        antecessor.append(None)
        visitados.append(False)

    # define a distancia da origem como 0
    distancia[origem - 1] = 0

    while False in visitados:
        print()

        # encontra o primeiro vertice nao visitado
        for i in range(cardinalidade_v):
            if visitados[i] == False:
                u = i
                break

        # extrai a menor distancia a ser computada
        for i in range(cardinalidade_v):
            if visitados[i] == False and distancia[i] < distancia[u]:
                u = i

        visitados[u] = True

        for v in g.vizinhos(u + 1):
            # relaxamento
            if distancia[v - 1] > (distancia[u] + g.peso(u + 1, v)):
                distancia[v - 1] = distancia[u] + g.peso(u + 1, v)
                antecessor[v - 1] = u

    print(visitados)
    print(distancia)
    print(antecessor)


def main():
    caminho_arquivo: str = input("Insira o nome do arquivo de grafos: ")
    vertice_inicial: int = int(input("Insira o numero do vértice inicial: "))
    g: Grafo = Grafo()
    g.ler(caminho_arquivo)
    resultados = dijkstra(g, vertice_inicial)
    exibir_resultados(resultados)


if __name__ == "__main__":
    main()
