from euleriancycle import eulerian_cycle
from graph import Graph
from collections import Counter


def find_source_and_sink(graph):
    degree = Counter
    for node in graph.nodes.values():
        for neighbor in node.neighbors:
            degree[node.value] += 1
            degree[neighbor.value] -= 1
    pass


def eulerian_path(graph):
    source, sink = find_source_and_sink(graph)

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        adj_list = fh.read()
    nodes = Graph.nodes_from_adj_list(adj_list)
    ep = eulerian_path(Graph(nodes))
    print('->'.join(ec))
