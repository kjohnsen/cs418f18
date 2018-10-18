from collections import defaultdict

class CustomDefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory:
            dict.__setitem__(self, key, self.default_factory(key))
            return self[key]
        else:
            defaultdict.__missing__(self, key)


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def remove_neighbor(self, node):
        self.neighbors.remove(node)

    def pop_a_neighbor(self):
        for node in self.neighbors: break
        self.remove_neighbor(node)
        return node

    def edge_count(self):
        return len(self.neighbors)

    def __repr__(self):
        string = str(self.value)
        i = 1
        for n in self.neighbors:
            if i == 1:
                string += ' -> ' + str(n.value)
            else:
                string += ',' + str(n.value)
            i += 1
        return string

    def __eq__(self, other):
        return self.value.__eq__(other.value)

    def __ne__(self, other):
        return not self.value.__eq__(other.value)

    def __hash__(self):
        return hash(self.value)


class Graph:
    def __init__(self, nodes=CustomDefaultdict(Node)):
        self.nodes = nodes

    def __repr__(self):
        lines = []
        for n in self.nodes.values():
            if len(n.neighbors) > 0:
                lines.append(str(n))
        return '\n'.join(lines)

    def add_edge(self, val1, val2):
        self.nodes[val1].add_neighbor(self.nodes[val2])

    def remove_edge(self, val1, val2):
        self.nodes[val1].remove_neighbor(self.nodes[val2])
        if self.nodes[val1].edge_count() == 0:
            del self.nodes[val1]

    def explore_an_edge(self, value) -> str:
        node = self.nodes[value].pop_a_neighbor()
        if self.nodes[value].edge_count() == 0:
            del self.nodes[value]
        return node.value


    def edge_count(self):
        total = 0
        for node in self.nodes.values():
            total += node.edge_count()
        return total

    @classmethod
    def nodes_from_adj_list(cls, adj_list: str):
        str_nodes = adj_list.splitlines()
        nodes = CustomDefaultdict(Node)
        for str_node in str_nodes:
            kmer, jmers = str_node.split(' -> ')
            for jmer in jmers.split(','):
                nodes[kmer].add_neighbor(nodes[jmer])
        return nodes

