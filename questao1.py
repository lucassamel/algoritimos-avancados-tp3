import math

Q = int(input("Insira a quantidade de comandos: "))

heap = []
nos= 0

def ordena_heap(nos, heap):
    while True:
        if nos == 1:
            break
        a = nos // 2
        if heap[a - 1] >= heap[nos - 1]:
            break
        else:
            heap[a - 1], heap[nos - 1] = heap[nos - 1], heap[a - 1]
            nos = a
    return heap

def exibe_heap(nos, heap):
    nivel = int(math.log(nos,2))
    a = 0
    for i in range(nivel):
        for j in range(2 ** i):
            print(f'{heap[a]}')
            a += 1
        print("")
    for i in range(nos - a):
        print(f'{heap[a]}')
        a += 1
    print('')


for i in range(Q):
    print("Escolha um dos comandos:")
    print('"1" – Adicionar um elemento v ao heap')
    print('“2” – Excluir o elemento v do heap')
    print('“3” – Imprimir o mínimo de todos os elementos do heap')
    comando = input()
    if comando == "1":
       elemento = int(input("Insira um elemento no heap: "))
       heap.append(elemento)
       nos += 1
       heap = ordena_heap(nos,heap)
    elif comando == "2":
        delete = int(input("Exclua um elemento do heap: "))
        for i in heap:
            if i == delete:
                heap.remove(i)
        heap = ordena_heap(nos, heap)
    elif comando == "3":
        print(heap)

print(heap)