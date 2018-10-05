from __future__ import division
from profileprobablekmer import profile_most_probable_kmer
from hammingdistance import hamming_distance

with open('input.txt', 'r') as fh:
    k, t = [int(x) for x in fh.readline().strip().split(' ')]
    sequences = fh.read().splitlines()

def profile_from_motifs_pseudocounts(motifs):
    t = len(motifs)
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        profile['A'].append((1+column.count('A')) / (t+1))
        profile['C'].append((1+column.count('C')) / (t+1))
        profile['G'].append((1+column.count('G')) / (t+1))
        profile['T'].append((1+column.count('T')) / (t+1))
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

def greedy_motif_search_pseudocounts(sequences, k, t):
    print(sequences)
    best_motifs = [seq[0:k] for seq in sequences]
    best_score = score_motifs(best_motifs)
    for i in range(len(sequences[0]) - k + 1):
        motifs = [sequences[0][i:i + k]]
        for j in range(1, t):
            profile = profile_from_motifs_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(sequences[j], k, profile))
        score = score_motifs(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs

# print(consensus_motif(['ACA', 'ATG', 'TCA']))
# print(score_motifs(['ACA', 'ATG', 'TCA']))
if __name__ == '__main__':
    print('\n'.join(greedy_motif_search_pseudocounts(sequences, k, t)))
