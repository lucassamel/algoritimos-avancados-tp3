import heap

n, m = int(input().split())

H = []

for j in range(m):
    # b = peso da aresta
    a, b, c = int(input().split())
    heapq.heappush(H, (c, a, b))

# Conjuntoos
C = [[] * n for i in range(n)]

for i in range(n):
    C[i].append(i)

S = []

for i in range(n):
    S.append(i)

cont = 0
custo = 0

while cont < n - 1:
    c, a, b = heapq.heappop(H)

    if S[a] != S[b]:
        custo = custo + c

        p = S[a]
        q = S[b]

        # Troca o indice
        if q < p:
            p, q = q, p

        for j in C[q]:
            S[j] = p

        C[p].extend(C[q])
        C[q] = []
        cont = cont + 1

        
print(custo)