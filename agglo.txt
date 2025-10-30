import math

points = [(1, 1), (2, 1), (5, 4), (6, 4)]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

clusters = [[p] for p in points]

while len(clusters) > 1:
    min_dist = 999
    pair = (0, 1)
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            for p1 in clusters[i]:
                for p2 in clusters[j]:
                    d = distance(p1, p2)
                    if d < min_dist:
                        min_dist = d
                        pair = (i, j)
    c1, c2 = pair
    clusters[c1].extend(clusters[c2])
    clusters.pop(c2)
    print("Merged:", clusters)
