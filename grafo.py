"""
Questão 1: Representação
"""

from typing import Set, Dict, List, Tuple

class Grafo:

    """
    Essa classe representa um grafo ponderado não-dirigido.
    """

    def __init__(self):
        self.__qtd_vertices : int = 0 #Complexidade de espaço: O(1)
        self.__qtd_arestas : int = 0 #Complexidade de espaço: O(1)
        self.__grau : List[int] = list() #Complexidade de espaço: O(n)
        self.__rotulos: List[str] = list() #Complexidade de espaço: O(n*k) OBS: K = tamanho médio de um rotulo
        self.__vizinhos: List[List[int]] = list() #Complexidade de espaço: O(n^2)
        self.__arestas : Dict[Set[int], float] = dict() #Complexidade de espaço O(n^2)

    def qtdVertices(self):
        """
        Retorna o número de vértices presentes no grafo.
        Complexidade de tempo: O(1) sempre.
        """
        return self.__qtd_vertices

    def qtdArestas(self) -> int:
        """
        Retorna o número de arestas presentes no grafo.
        Complexidade de tempo: O(1) sempre.
        """
        return self.__qtd_arestas

    def grau(self, v : int) -> int:
        """
        Retorna o grau de um grafo.
        Complexidade de tempo: O(1) sempre.
        """
        return self.__grau[v-1]

    def rotulo(self, v : int) -> str:
        """
        Retorna o rótulo de um grafo.
        Complexidade de tempo: O(1) sempre.
        """
        return self.__rotulos[v-1]

    def vizinhos(self, v : int) -> List[int]:
        """
        Retorna uma lista com todos os vizinhos de um vértice
        Complexidade de tempo: O(1) sempre.
        """
        return self.__vizinhos[v-1]

    def haAresta(self, u : int, v : int) -> bool:
        """
        Retorna 'verdadeiro' se existir uma aresta entre u e v.
        Complexidade de tempo: caso médio O(1), pior caso O(n)
        """
        par_vertice : Set[int] = set()
        par_vertice.add(u)
        par_vertice.add(v)

        return frozenset(par_vertice) in self.__arestas
    
    def peso(self, u : int, v: int) -> float:
        """
        Retorna o peso de uma aresta se ela existir entre u e v.
        Caso contrário retorna infinito.
        Complexidade de tempo: O(1)
        """
        par_vertice : Set[int] = set()
        par_vertice.add(u)
        par_vertice.add(v)
        par_vertice = frozenset(par_vertice)

        if par_vertice in self.__arestas:
            return self.__arestas[par_vertice]
        else:
            return float('inf')
    
    def ler(self, caminho_arquivo : str):
        """
        Lê um arquivo e constrói um grafo a partir dele.
        Complexidade de tempo: O(n^2) no pior caso - n é o número de vértices do grafo
        """
        with open(caminho_arquivo) as arquivo:
            linhas : List[str] = arquivo.readlines()

            self.__qtd_vertices = int(linhas[0][10:])

            for i in range(1, self.__qtd_vertices + 1):
                dados_linha : Tuple[str, str] = linhas[i].split(" ", 1)
                self.__rotulos.append(dados_linha[1][:-2][1:])
                self.__grau.append(0)
                self.__vizinhos.append(list())

            qtd_linhas : int = len(linhas)
            self.__qtd_arestas = qtd_linhas - self.__qtd_vertices - 2

            for i in range(self.__qtd_vertices + 2, qtd_linhas):
                dados_linha : Tuple[str, str, str] = linhas[i].split(" ")
                par_vertice : Set[int] = set()
                v : int = int(dados_linha[0])
                u : int = int(dados_linha[1])
                par_vertice.add(v)
                par_vertice.add(u)
                self.__vizinhos[u-1].append(v)
                self.__vizinhos[v-1].append(u)
                self.__grau[u-1] += 1
                self.__grau[v-1] += 1

                self.__arestas[frozenset(par_vertice)] = float(dados_linha[2])

if __name__ == "__main__":
    grafo = Grafo()
    grafo.ler("facebook_santiago.net")