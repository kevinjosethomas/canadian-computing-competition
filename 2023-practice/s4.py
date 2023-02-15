# Animal Farm - 0/15

num = int(input())
pens = []
edges = {}

for _ in range(num):
    pen = list(map(int, input().split()))
    penedges = pen[1 : pen[0] + 1]
    formated_edges = []
    edgevalues = pen[pen[0] + 1 :]

    for i, edge in enumerate(penedges):
        edge = tuple(sorted((edge, penedges[i + 1 if i + 1 < len(penedges) else 0])))
        formated_edges.append(edge)
        edges[edge] = edgevalues[i]

    pens.append((pen[0], formated_edges, edgevalues))

cost = 0
removed_edges = []

for i, pen in enumerate(pens[:-1]):

    found = False
    while not found:
        cheapest = min(pen[2])
        index = pen[2].index(cheapest)
        edge = pen[1][index]

        if edge in removed_edges:
            pens[i][1].pop(index)
            pens[i][2].pop(index)
            continue
        found = True

    removed_edges.append(edge)
    cost += cheapest

print(cost)
