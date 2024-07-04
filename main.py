#1)Grau de um determinado vértice/nó
#2) Grau de todos os vértices/nós
#3) Grau máximo e mínimo de um grafo
#4) Verificação de vizinhança entre dois nós/vértices
#5) Verificação se o grafo criado é simples ou multigrafo
#6) Verificação se existe um caminho entre dois nós/vértices
#7) Verificar se o caminho entre dois vértices/nós é um ciclo
#8) A partir de um nó/vértice dado verificar todos os vértices vizinhos
#9) Verificação se o grafo criado é “conexo” ou “não conexo”
#10) Verificar e mostrar a existência (ou não) de vértices isolados
from grafo import Grafo
from vertice import Vertice
import os
import platform

def limpar_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')



def menu():
    contador_grafo = 1
    grafo = Grafo()
    while True:
        print(""" 
---------------------------------------------------------|---------------------------------------------------------------|
            OPERAÇÕES GRAFO E VÉRTICE:                   |                  OPERAÇÕES VISUALIZAÇÃO                       |
---------------------------------------------------------|---------------------------------------------------------------|
1) Adicionar vértice                                     |4) visualizar lista de adjacência                              |
2) Reinicia grafo                                        |5) visualizar matriz de adjacência                             |
3) criar aresta                                          |6) visualizar vertices                                         |
                                                         |7) visualizar arestas                                          |
                                                         |                                                               |
---------------------------------------------------------|---------------------------------------------------------------|
            OPERAÇÕES GERAIS:                            |                  OPERAÇÕES GERAIS:                            |
---------------------------------------------------------|---------------------------------------------------------------|
8) Grau de um determinado vértice                        |13) Verificação se existe um caminho entre dois vértices       |
9) Grau de todos os vértices/nós                         |14) Verificar se o caminho entre dois vértices é um ciclo      |
10) Grau máximo e mínimo de um grafo                     |15) A partir de um vértice dado verificar vértices vizinhos    |
11) Verificação de vizinhança entre dois vértices        |16) Verificação se o grafo criado é “conexo” ou “não conexo"   |              
12) Verificação se o grafo criado é simples ou multigrafo|17) Verificar/mostrar a existência ou não de vértices isolados |
---------------------------------------------------------|---------------------------------------------------------------|""")

        opcao = input("Digite a opção desejada (0 para sair): ")

        if opcao == "0":
            break

        elif opcao == "1":
            limpar_terminal()
            grafo.add_vertice(contador_grafo)
            print(f"Vértice {contador_grafo} adicionado com sucesso")
            contador_grafo += 1
            

        elif opcao == "2":
            limpar_terminal()
            contador_grafo = grafo.reiniciar_grafo()
            print("Grafo reiniciado!")

        elif opcao == "3":
            limpar_terminal()
            origem = int(input("Digite o valor do vértice de origem (exemplo: 1):"))
            destino = int(input("Digite o valor do vértice de destino (exemplo: 2): "))
            peso = int(input("Digite o peso da aresta: "))
            bool = grafo.add_aresta(origem, destino, peso)
            if bool:
                print(f"Aresta entre {origem} e {destino} adicionada com sucesso")
            else:
                print("Vértices não encontrados")

        elif opcao == "4":
            limpar_terminal()
            lista_adjacencia = grafo.lista_adjacencia()
            print("Lista de adjacência (Origem: [(Destino,peso)]):")
            if lista_adjacencia:
                for vertice, vizinhos in lista_adjacencia.items():
                    print(f"{vertice}: {vizinhos}")
            else:
                print("Grafo vazio")

        elif opcao == "5":
            limpar_terminal()
            matriz_adjacencia = grafo.matriz_adjacencia()
            print("Matriz adjacência:")
            if matriz_adjacencia:
                for row in matriz_adjacencia:
                    print(row)
                print()
            else:
                print("Grafo vazio")

        elif opcao == "6":
            limpar_terminal()
            grafo.get_vertices()
            print("Vertices:")
            if grafo.vertices:
                for vertice in grafo.vertices:
                    print(vertice.valor)
            else:
                print("Nenhum vértice no grafo.")
            
        elif opcao == "7":
            limpar_terminal()
            arestas = grafo.get_arestas()
            
            print("Arestas: (Origem, Destino, Peso)")
            if arestas:
                for aresta in arestas:
                    print(f"({aresta[0]}, {aresta[1].valor}, {aresta[2]})")
            else:
                print("Nenhuma aresta no grafo.")
             
        elif opcao == "8":
            limpar_terminal()
            valor = int(input("Digite o valor do vértice (exemplo: 1): "))
            vertice = grafo.get_vertice(valor)

            if vertice:
                print(f"Grau do vértice {valor}: {vertice.get_grau()}")
            else:
                print(f"Vértice {valor} não encontrado.")
            
        elif opcao == "9":
            limpar_terminal()
            vertices_grau = grafo.get_grau_vertices()
            print("Grau dos vértices:")
            if vertices_grau:
                for vertice, grau in vertices_grau.items():
                    print(f"Vértice {vertice}: {grau}")
            else:
                print("Nenhum vértice no grafo.")

        elif opcao == "10":
            limpar_terminal()
            max_min_graus = grafo.get_min_max_grau()
            print("Grau máximo e mínimo:")
            if max_min_graus:
                print(f"Grau máximo: {max_min_graus[0]}")
                print(f"Grau mínimo: {max_min_graus[1]}")
            else:
                print("Nenhum vértice no grafo.")
        
        elif opcao == "11":
            limpar_terminal()
            v1 = int(input("Digite o valor do vértice de origem (exemplo: 1): "))
            v2 = int(input("Digite o valor do vértice de destino (exemplo: 2):"))
            are_vizinhos = grafo.are_vizinhos(v1, v2)

            if are_vizinhos == 1:
                print(f"Os vértices {v1} e {v2} SÃO vizinhos")
            elif are_vizinhos == 0:
                print(f"Os vértices {v1} e {v2} NÃO são vizinhos")
            else:
                print("Vértices não encontrados")
        
        elif opcao == "12":
            limpar_terminal()
            is_multigrafo = grafo.is_multigrafo()
            print("Grafo é SIMPLES ou MULTIGRAFO:")
            if is_multigrafo == 1:
                print("Grafo é MULTIGRAFO")
            elif is_multigrafo == 0:
                print("Grafo é SIMPLES")
            elif is_multigrafo == -1:
                print("Grafo vazio")
            elif is_multigrafo == -2:
                print("Grafo não possui arestas")

        elif opcao == "13":
            limpar_terminal()
            v1 = int(input("Digite o valor do vértice de origem (exemplo: 1): "))
            v2 = int(input("Digite o valor do vértice de destino (exemplo: 2): "))
            existe = grafo.existe_caminho_entre_vertices(v1, v2)
            if existe == 1:
                print("Existe caminho entre os vértices")
            elif existe == 0:
                print("Não existe caminho entre os vértices")
            elif existe == -1:
                print("Vértices não encontrados")

        elif opcao == "14":
            limpar_terminal()
            v1 = int(input("Digite o valor do vértice de origem (exemplo: 1): "))
            v2 = int(input("Digite o valor do vértice de destino (exemplo: 2): "))
            is_ciclo = grafo.is_caminho_ciclo(v1,v2)
            if is_ciclo == 1:
                print("O caminho entre os vértices é um ciclo")
            elif is_ciclo == 0:
                print("O caminho entre os vértices NÃO é um ciclo")
            elif is_ciclo == -1:
                print("Vértices não encontrados")

        elif opcao == "15":
            limpar_terminal()
            v = int(input("Digite o valor do vértice (exemplo: 1): "))
            vizinhos = grafo.get_vizinhos_vertice(v)
            print(f"Vizinhos do vértice {v}: (Vizinho, Peso)")
            if len(vizinhos) > 0:
                for vizinho in vizinhos:
                    print(f"({vizinho[0].valor}, {vizinho[1]})")
            elif vizinhos is None:
                print("Vértice não encontrado")
            else:
                print("Vértice não possui vizinhos")
        
        elif opcao == "16":
            limpar_terminal()
            is_conexo = grafo.is_conexo()
            if is_conexo == 1:
                print("Grafo é conexo")
            elif is_conexo == 0:
                print("Grafo não é conexo")
            else:
                print("Grafo vazio")


        elif opcao == "17":
            limpar_terminal()
            vertices_isolados = grafo.get_vertices_isolados()
            print("Vértices isolados:")
            if vertices_isolados:
                for vertice in vertices_isolados:
                    print(vertice)
            else:
                print("Nenhum vértice isolado")
            
            
                
                
        
        
menu()