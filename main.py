a = int(input())
sp = []
for i in range(a):
    ch = int(input())
    sp.append(ch)
b = int(input())
sl = {}
kol = []
kol1 = []
for j in range(b):
    ch1 = input()
    sl[ch1[0]] = ch1[-1]
    kol.append(ch1)


print(sp)
t = 0

for el in range(1, len(sp) + 1):
    if str(el) in sl:
       kol1.append()


def find_minimum_development_time(n, times, dependencies):
    indegree = [0] * n
    graph = [[] for _ in range(n)]

    for a, b in dependencies:
        graph[a].append(b)
        indegree[b] += 1


    zero_indegree = []
    for i in range(n):
        if indegree[i] == 0:
            zero_indegree.append(i)


    total_time = [0] * n
    for u in zero_indegree:
        total_time[u] = times[u]


    while zero_indegree:
        node = zero_indegree.pop(0)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            total_time[neighbor] = max(total_time[neighbor], total_time[node] + times[neighbor])

            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)


    if any(indegree[i] > 0 for i in range(n)):
        return "IMPOSSIBLE"

    return max(total_time)



n = int(input())
times = []
for _ in range(n):
    times.append(int(input()))

m = int(input())
dependencies = []
for _ in range(m):
    a, b = map(int, input().split())
    dependencies.append((a - 1, b - 1))


result = find_minimum_development_time(n, times, dependencies)
print(result)
