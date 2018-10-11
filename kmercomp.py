
def kmer_composition(k, seq):
    kmers = set()
    for i in range(len(seq) - k + 1):
        kmers.add(seq[i:i+k])
    return kmers

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        k = int(fh.readline().strip())
        seq = fh.readline().strip()
    kmers = kmer_composition(k, seq)
    print('\n'.join(kmers))