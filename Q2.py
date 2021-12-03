"""
Questão 2: busca
"""

from grafo import Grafo
from typing import Set, List, Deque, Tuple, Dict
from collections import deque


def realizar_busca(g : Grafo, vertice_inicial : int) -> List[List[int]]:
    """
    Esse método retorna uma estrutura de dados com todos os vértices alcançaveis a partir de um vértice inicial.
    """
    vertices_expandidos : Set[int] = set() #conjunto de vertices que tiveram seus vizinhos adicionados a fila
    vertices_explorados : Set[int] = set() #conjunto de vertices que foram adicionados ao resultado
    resultados : Dict[int, List[int]] = dict()
    fila : Deque[Tuple[int, int]] = deque() #fila de tuplas: 0 - vertice, 1 - nivel
    fila.append((vertice_inicial, 0)) #adiciona o vertice inicial na fila

    while fila:
        dados_fila : Tuple[int, int] = fila.popleft()
        vertice_atual : int = dados_fila[0]
        nivel_atual : int = dados_fila[1]

        #se o vertice ainda não foi encontrado em nenhum nivel
        if vertice_atual not in vertices_explorados:
            if nivel_atual not in resultados:
                resultados[nivel_atual] = list()
            #adicione ele no nivel atual
            resultados[nivel_atual].append(vertice_atual)
            #adicione ele no conjunto de vertices que ja foram adicionados a algum nivel
            vertices_explorados.add(vertice_atual)

        vizinhos = g.vizinhos(vertice_atual)

        vertices_expandidos.add(vertice_atual)

        for vizinho in vizinhos:
            if vizinho not in vertices_expandidos:
                fila.append((vizinho, nivel_atual+1))
    
    return resultados
    
def exibir_resultados(resultados : Dict[int, List[int]]):
    for nivel in resultados:
        vertices = resultados[nivel]
        
        string_formatada = ""

        for vertice in vertices:
            string_formatada += "{},".format(vertice) 

        print("{}: {}".format(nivel, string_formatada[:-1]))

def main():
    caminho_arquivo : str = input("Insira o nome do arquivo de grafos: ")
    vertice_inicial : int = int(input("Insira o vértice inicial: "))
    g : Grafo = Grafo()
    g.ler(caminho_arquivo)
    resultados = realizar_busca(g, vertice_inicial)
    exibir_resultados(resultados)

if __name__ == "__main__":
    main()


