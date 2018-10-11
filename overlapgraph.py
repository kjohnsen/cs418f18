from graph import Graph


def prefix(kmer):
    return kmer[:-1]


def suffix(kmer):
    return kmer[1:]


def overlap_graph(kmers):
    graph = Graph()
    for kmer in kmers:
        for jmer in kmers:
            if suffix(kmer) == prefix(jmer):
                graph.add_edge(kmer, jmer)
    return graph


if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        kmers = fh.read().splitlines()
    og = overlap_graph(kmers)
    print(og)
