"""
Questão 5: Floyd-Warshall

"""

from grafo import Grafo


def floyd_warshall(g):

    cardinalidade_v = g.qtdVertices()  # |V|

    d = inicializa_adj(g, cardinalidade_v)  # uma matriz bidimencional de distancias

    for k in range(cardinalidade_v):
        dk = d
        for u in range(cardinalidade_v):
            for v in range(cardinalidade_v):
                dk[u][v] = min(d[u][v], d[u][k] + d[k][v])
    return dk


def inicializa_adj(g, n):

    d = []
    for v in range(n):
        nv = g.vizinhos(v + 1)
        l = []
        for u in range(n):
            if (u + 1) in nv:
                l.append(g.peso(u + 1, v + 1))
            else:
                l.append(float("inf"))

        d.append(l)
    return d


def exibir_resultados(d):
    # itera sobre matriz
    for n in range(len(d)):
        print(n + 1, end=":")  # imprime indice

        for z in range(len(d) - 1):
            r = d[n][z]
            if r == float("inf"):
                print("inf", end=",")
            else:
                print(int(r), end=",")
        # para formatacao sem virgula no final
        r = d[n][len(d) - 1]
        if r == float("inf"):
            print("inf", end="")
        else:
            print(int(r), end="")
        print()


def main():
    caminho_arquivo: str = input("Insira o nome do arquivo de grafos: ")
    g: Grafo = Grafo()
    g.ler(caminho_arquivo)
    d = floyd_warshall(g)
    exibir_resultados(d)


if __name__ == "__main__":
    main()
