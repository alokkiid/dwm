from itertools import combinations

transactions = [
    {'A', 'B', 'C'},
    {'A', 'C'},
    {'A', 'D'},
    {'B', 'E'},
    {'A', 'B', 'E'}
]

min_support = 2

items = set()
for t in transactions:
    items |= t
candidates = [{i} for i in items]

def support_count(itemset):
    return sum(1 for t in transactions if itemset <= t)

frequent = []
k = 1

while candidates:
    print(f"\nFrequent Itemsets of size {k}:")
    next_candidates = []
    for c in candidates:
        count = support_count(c)
        if count >= min_support:
            print(c, "=>", count)
            frequent.append(c)
            next_candidates.extend([c | {i} for i in items if i not in c])
    candidates = []
    for c in next_candidates:
        if c not in candidates and len(c) == k + 1:
            candidates.append(c)
    k += 1
