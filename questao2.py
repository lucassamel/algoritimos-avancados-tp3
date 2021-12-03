import heap

n, m = int(input().split())

H = []

for j in range(m):
    a, b, c = int(input().split())
    heapq.heappush(H, (c, a, b))

# Conjuntoos
C = [[] * n for i in range(n)]

for i in range(n):
    C[i].append(i)

S = []

for i in range(n):
    S.append(i)