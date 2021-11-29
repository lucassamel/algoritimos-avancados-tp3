
Q = input("Insira a quantidade de comandos: ")

heap = []

for i in range(Q):
    print("Escolha um dos comandos:")
    print('"1 v" – Adicionar um elemento v ao heap')
    print('“2 v” – Excluir o elemento v do heap')
    print('“3” – Imprimir o mínimo de todos os elementos do heap')
    comando = input()
    if comando == "1 v":
       elemento = input("Insira um elemento no heap: ")
       heap.append(elemento)
    elif comando == "2 v":
        input("Exclua um elemento do heap: ")
    elif comando == "3":
        print(heap)