from graph import Graph
from kmercomp import kmer_composition


def prefix(kmer):
    return kmer[:-1]


def suffix(kmer):
    return kmer[1:]


def debruijn_graph(k, seq):
    graph = Graph()
    for kmer in kmer_composition(k, seq):
        graph.add_edge(prefix(kmer), suffix(kmer))
    return graph


def debruijn_from_kmers(kmers):
    graph = Graph()
    for kmer in kmers:
        graph.add_edge(prefix(kmer), suffix(kmer))
    return graph



if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        kmers = fh.read().splitlines()
        og = debruijn_from_kmers(kmers)
    print(og)
