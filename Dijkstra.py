import matplotlib.pyplot as plt
import networkx as nx

infinity = float("inf")


def make_graph():
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
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
    graph = make_graph()
    G = nx.from_dict_of_lists(graph)
    start = 'A'

    shortest_paths = dijkstras(graph, start)
    weight = nx.get_edge_attributes(G, 'weight')
    pos = nx.get_node_attributes(G, 'pos')
    shortest_paths_tuple = tuple(shortest_paths.keys())
    sp = []
    for i in range(0, len(shortest_paths_tuple) - 1):
        sp.append((shortest_paths_tuple[i], shortest_paths_tuple[i + 1]))

    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
    nx.draw(G, pos, with_labels=weight)
    # painting every edge green
    nx.draw_networkx_edges(G, pos, edge_color="green")
    # painting specific edges red
    nx.draw_networkx_edges(G, pos, edgelist=sp, edge_color="red")
    plt.show()

    print(f'Shortest path from {start}: {shortest_paths}')


main()
