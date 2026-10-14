GRAPH = {
    "A": ["B", "C", "U"], "B": ["E", "G"], "C": ["G", "I", "J"],
    "U": ["K", "Y"], "E": ["G", "M"], "G": ["M"], "I": ["M"],
    "J": ["K"], "K": ["J"], "Y": ["M"], "M": [],
}
H = {"A": 7, "B": 5, "C": 3, "U": 4, "E": 2, "G": 3,
     "I": 6, "J": 4, "K": 1, "Y": 2, "M": 0}

current, goal = "A", "M"
path = [current]

while current != goal:
    best = min(GRAPH[current], key=lambda n: H[n])
    print(f"{current} (h={H[current]}) -> {best} (h={H[best]})")
    if H[best] > H[current] or best in path:
        break
    current = best
    path.append(current)

print("Path:", " -> ".join(path))