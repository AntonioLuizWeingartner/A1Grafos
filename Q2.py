"""
Questão 2: busca
"""

from grafo import Grafo






def main():
    caminho_arquivo : str = input("Insira o nome do arquivo de grafos: ")
    vertice_inicial : int = int(input("Insira o vértice inicial: "))
    g : Grafo = Grafo()
    g.ler(caminho_arquivo)

if __name__ == "__main__":
    main()


