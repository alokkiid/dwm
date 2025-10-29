graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

ranks = {page: 1 for page in graph}
damping = 0.85

for _ in range(10):
    new_ranks = {}
    for page in graph:
        rank_sum = 0
        for other in graph:
            if page in graph[other]:
                rank_sum += ranks[other] / len(graph[other])
        new_ranks[page] = (1 - damping) + damping * rank_sum
    ranks = new_ranks

for page, rank in ranks.items():
    print(f"{page}: {round(rank, 3)}")
