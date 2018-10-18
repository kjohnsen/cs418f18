from graph import Graph


def random_cycle(graph, potential_starts=[]) -> []:
    cycle = []
    for start in graph.nodes.keys():
        if len(potential_starts) == 0:
            break
        elif start in potential_starts:
            break  # grab node with unexplored edges
    cycle.append(start)

    next = graph.explore_an_edge(start)
    cycle.append(next)
    while next != start:
        next = graph.explore_an_edge(next)
        cycle.append(next)

    return cycle


def eulerian_cycle(graph) -> []:
    cycle = []
    original_edge_count = graph.edge_count()
    while len(cycle) < original_edge_count + 1:
        this_cycle = random_cycle(graph, cycle)
        if len(cycle) == 0:
            cycle = this_cycle
        else:
            insertion_idx = cycle.index(this_cycle[0])
            cycle[insertion_idx:insertion_idx] = this_cycle[:-1]  # leave off last node to avoid repetition ABA <- BCB = ABCBA
    return cycle



def print_cycle(cycle):
    print('->'.join(cycle))


if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        adj_list = fh.read()
    nodes = Graph.nodes_from_adj_list(adj_list)
    ec = eulerian_cycle(Graph(nodes))
    print_cycle(ec)
