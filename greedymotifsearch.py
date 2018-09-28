from profileprobablekmer import profile_most_probable_kmer

with open('input.txt', 'r') as fh:
    k, t = [int(x) for x in fh.readline().strip().split(' '))]
    sequences = fh.read().splitlines()


def greedy_motif_search(sequences, k, t)
    best_motifs = [seq[0:k] for seq in sequences]
    for i in range(len(sequences[0]) - k + 1):
        motifs = []
        motifs.append(sequences[0][i:i+k])
        for j in range(1, t):
            profile = profile_from_motifs(motifs)
            motifs.append(profile_most_probable_kmer(sequences[j], k, profile))

    return best_motifs