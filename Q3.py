from collections import deque
from grafo import Grafo
from typing import List, Tuple, FrozenSet, Set


def computar_ciclo_euleriano(g : Grafo) -> Tuple[int, List[int]]:
    """
    As condições suficientes para a existência de um ciclo euleriano são: não existência de componentes desconexas
    e grau par em todos os vértices do grafo.
    """
    arestas_visitadas : Set[FrozenSet[int]] = set()
    
    v_inicial = selecionar_vertice_inicial(g)

    if v_inicial == -1:
        return (0, [])

    resultado = computar_ciclo_euleriano_auxiliar(g, v_inicial, arestas_visitadas)

    if len(resultado[1]) != g.qtdArestas()+1:
        return (0, [])
    else:
        return resultado


def selecionar_vertice_inicial(g : Grafo) -> int:
    """
    Essa função deve retornar o vértice inicial que deverá ser utilizado na busca.
    vertices com grau 0 devem ser ignorados.
    Se um vértice com grau impar for encontrado então o algoritmo deve retornar -1 sinalizando que não existe ciclo euleriano.
    """
    for i in range(1, g.qtdVertices()):
        if g.grau(i) > 0 and (g.grau(i) % 2) == 0:
            return i
        else:
            if (g.grau(i) % 2) != 0:
                return -1

    
def computar_ciclo_euleriano_auxiliar(g : Grafo,
                                      vertice_inicial : int,
                                      arestas_visitadas : Set[FrozenSet[int]]) -> Tuple[int, List[int]]:
    ciclo : List[int] = list()
    v_atual : int = vertice_inicial
    target : int = vertice_inicial

    condicao : bool = True

    while condicao:
        
        vizinhos : List[int] = g.vizinhos(v_atual)

        todas_arestas_visitadas = True
        for vizinho in vizinhos:
            aresta : Set[int] = set()
            aresta.add(v_atual)
            aresta.add(vizinho)
            aresta = frozenset(aresta)

            todas_arestas_visitadas = todas_arestas_visitadas and aresta in arestas_visitadas        

            #se todas as arestas ja foram visitadas, então não há possibilidade de existir um ciclo euleriano
            if todas_arestas_visitadas is False:
                arestas_visitadas.add(aresta)
                ciclo.append(v_atual)
                v_atual = vizinho
                break

        if todas_arestas_visitadas:
            return (0, [])

        condicao = v_atual != target
    ciclo.append(ciclo[0])
    #percorrer cada vertice do ciclo procurando por uma aresta que não esteja conectada
    for vertice in ciclo:
        vizinhos : List[int] = g.vizinhos(vertice)

        for vizinho in vizinhos:
            aresta : Set[int] = set()
            aresta.add(vertice)
            aresta.add(vizinho)
            aresta = frozenset(aresta)

            if aresta not in arestas_visitadas:
                #não é ciclo euleriano, computar novamente.
                resultado_adicional = computar_ciclo_euleriano_auxiliar(g, vertice, arestas_visitadas)

                if resultado_adicional[0] == 0:
                    return (0, [])
                
                #linha 16 do algoritmo que esta na apostila
                idx = ciclo.index(vertice)
                ciclo.pop(idx)

                k = 0
                for v in resultado_adicional[1]:
                    ciclo.insert(idx+k, v)
                    k += 1
                    
    return (1, ciclo)

def exibir_resultados(resultado:  Tuple[int, List[int]]):
    print(resultado[0])
    string_formatada = ""
    for v in resultado[1]:
        string_formatada += "{},".format(v)

    print(string_formatada[:-1])

def main():
    g = Grafo()
    g.ler(input("Insira o nome do arquivo: "))
    exibir_resultados(computar_ciclo_euleriano(g))

if __name__ == "__main__":
    main()