from hammingdistance import hamming_distance

with open('input.txt', 'r') as fh:
    k = int(fh.readline().strip())
    patterns = fh.read().splitlines()


def all_kmers(k):
    if k == 1:
        return ['A', 'C', 'G', 'T']
    else:
        result = []
        root_kmers = all_kmers(k-1)
        for kmer in root_kmers:
            for nuc in ['A', 'C', 'G', 'T']:
                result.append(kmer + nuc)
        return result


def min_hamming_distance(pattern, sequence):
    distance = float('inf')
    k = len(pattern)
    for i in range(len(sequence)-k+1):
        other_pattern = sequence[i:i+k]
        temp_distance = hamming_distance(pattern, other_pattern)
        if temp_distance < distance:
            distance = temp_distance
    return distance

def d(pattern, sequences):
    result = 0
    for seq in sequences:
        result += min_hamming_distance(pattern, seq)
    return result

def median_string(k, sequences):
    distance = float('inf')
    for kmer in all_kmers(k):
        temp_distance = d(kmer, sequences)
        if temp_distance < distance:
            distance = temp_distance
            result = kmer
    return result


print(median_string(k, patterns))