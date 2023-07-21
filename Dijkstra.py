infinity = float("inf")


def make_graph():
    return {
        'A': [(4, 'B'), (1, 'C'), (6, 'D')],
        'B': [(1, 'E'), (6, 'C'), (4, 'F')],
        'C': [(6, 'F'), (8, 'D')],
        'D': [8, 'G'],
        'E': [(3, 'F')],
        'F': [(5, 'H'), (2, 'G')],
        'G': [(1, 'H'), (3, 'I')],
        'H': [(2, 'I')],
    }


def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = list(G.keys())

    for node in unvisited:
        shortest_paths[node] = infinity

    shortest_paths[start] = 0

    while unvisited:
        min_node = None

        for node in unvisited:
            if min_node is None:
                min_node = node
            elif shortest_paths[node] < shortest_paths[min_node]:
                min_node = node

        for edge in G[min_node]:
            cost = edge[0]
            to_node = edge[1]

            if cost + shortest_paths[min_node] < shortest_paths[to_node]:
                shortest_paths[to_node] = cost + shortest_paths[min_node]

        unvisited.remove(min_node)

    return shortest_paths


def main():
    G = make_graph()
    start = 'A'

    shortest_paths = dijkstras(G, start)
    # shortest_paths_using_heap = dijkstras_heap(G, start)

    print(f'Shortest path from {start}: {shortest_paths}')
    # print(f'Shortest path from {start} using heap: {shortest_paths_using_heap}')


main()
