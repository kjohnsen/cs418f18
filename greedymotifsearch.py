from profileprobablekmer import profile_most_probable_kmer
from hammingdistance import hamming_distance

with open('input.txt', 'r') as fh:
    k, t = [int(x) for x in fh.readline().strip().split(' ')]
    sequences = fh.read().splitlines()

def profile_from_motifs(motifs):
    t = len(motifs)
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        profile['A'].append(column.count('A') / t)
        profile['C'].append(column.count('C') / t)
        profile['G'].append(column.count('G') / t)
        profile['T'].append(column.count('T') / t)
    return profile

def most_common(lst):
    return max(set(lst), key=lst.count)

def consensus_motif(motifs):
    result = ''
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        result += most_common(column)
    return result

def score_motifs(motifs):
    consensus = consensus_motif(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(consensus, motif)
    return score

def greedy_motif_search(sequences, k, t):
    best_motifs = [seq[0:k] for seq in sequences]
    for i in range(len(sequences[0]) - k + 1):
        motifs = []
        motifs.append(sequences[0][i:i+k])
        for j in range(1, t):
            profile = profile_from_motifs(motifs)
            print(profile)
            motifs.append(profile_most_probable_kmer(sequences[j], k, profile))
        score = score_motifs(motifs)
        if score < best_score:
            best_motifs = motifs
    return best_motifs

print(greedy_motif_search(sequences, k, t))