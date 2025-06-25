from collections import defaultdict, deque

# Step 1: Read triplets
with open("F:\keylog.txt") as f:
    attempts = [line.strip() for line in f if line.strip()]

# Step 2: Build graph
graph = defaultdict(set)
in_degree = defaultdict(int)

digits = set(''.join(attempts))
for d in digits:
    in_degree[d] = 0  # Ensure all digits are initialized

for attempt in attempts:
    a, b, c = attempt
    # Create edges: a -> b, b -> c
    if b not in graph[a]:
        graph[a].add(b)
        in_degree[b] += 1
    if c not in graph[b]:
        graph[b].add(c)
        in_degree[c] += 1

# Step 3: Topological sort using Kahn's algorithm
queue = deque([node for node in in_degree if in_degree[node] == 0])
result = []

while queue:
    node = sorted(queue)[0]  # Sort for consistent lex order if needed
    queue.remove(node)
    result.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# Step 4: Output result
print("Shortest possible passcode is:", ''.join(result))