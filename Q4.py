"""
Questão 4: Dijkstra
"""

from grafo import Grafo


def exibir_resultados(d, a, vertice_inicial):
    for u in range(len(a)):
        print(u + 1, end=": ")
        ant = []  # anteriores ao vertice u
        shortest_path(ant, a, vertice_inicial - 1, u)
        if d[u] == float("inf"):
            print(
                "Caminho Inexistente de %d para %d; d=inf" % (vertice_inicial, (u + 1))
            )
        else:
            print(*ant, sep=",", end="; ")
            print("d=%d" % d[u])


# similar ao algoritmo 14 das anotacoes para disciplina
def shortest_path(ant, a, u, v):
    if u == v:
        ant.append((u + 1))
    else:
        if a[v] != None:
            shortest_path(ant, a, u, a[v])
            ant.append((v + 1))


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

    return distancia, antecessor


def main():
    caminho_arquivo: str = input("Insira o nome do arquivo de grafos: ")
    vertice_inicial: int = int(input("Insira o numero do vértice inicial: "))
    g: Grafo = Grafo()
    g.ler(caminho_arquivo)
    d, a = dijkstra(g, vertice_inicial)
    exibir_resultados(d, a, vertice_inicial)


if __name__ == "__main__":
    main()
