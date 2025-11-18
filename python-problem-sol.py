def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

n, m = map(int, input().split())

employees = []
knows_any = False


for _ in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    langs = data[1:]
    employees.append(langs)
    if k > 0:
        knows_any = True


if not knows_any:
    print(n)
    exit()


graph = [[] for _ in range(m + 1)]

for langs in employees:
    for i in range(1, len(langs)):
        a = langs[i - 1]
        b = langs[i]
        graph[a].append(b)
        graph[b].append(a)


visited = [False] * (m + 1)
components = 0

for langs in employees:
    if len(langs) > 0:
        first_lang = langs[0]
        if not visited[first_lang]:
            components += 1
            dfs(first_lang)

print(components - 1)