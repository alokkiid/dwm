import math
points = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4)]
centroids = [(2, 10), (5, 8)]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

for iteration in range(3):
    print("\nIteration:", iteration+1)
    cluster1, cluster2 = [], []
    for p in points:
        d1 = distance(p, centroids[0])
        d2 = distance(p, centroids[1])
        if d1 < d2:
            cluster1.append(p)
        else:
            cluster2.append(p)
    new_c1 = (sum(p[0] for p in cluster1)/len(cluster1), sum(p[1] for p in cluster1)/len(cluster1))
    new_c2 = (sum(p[0] for p in cluster2)/len(cluster2), sum(p[1] for p in cluster2)/len(cluster2))
    centroids = [new_c1, new_c2]
    print("Cluster 1:", cluster1)
    print("Cluster 2:", cluster2)
    print("New Centroids:", centroids)
