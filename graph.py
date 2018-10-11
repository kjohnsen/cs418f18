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
        self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)

    def __repr__(self):
        string = str(self.value)
        i = 1
        for n in self.neighbors:
            if i == 1:
                string += ' -> ' + str(n.value)
                continue
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
    def __init__(self):
        self.nodes = CustomDefaultdict(Node)

    def __repr__(self):
        lines = []
        for n in self.nodes.values():
            if len(n.neighbors) > 0:
                lines.append(str(n))
        return '\n'.join(lines)

    def add_edge(self, val1, val2):
        self.nodes[val1].add_neighbor(self.nodes[val2])
