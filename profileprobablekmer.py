# with open('input.txt', 'r') as fh:
#     text = fh.readline().strip()
#     k = int(fh.readline().strip())
#     profile = {}
#     profile['A'] = [float(x) for x in fh.readline().strip().split(' ')]
#     profile['C'] = [float(x) for x in fh.readline().strip().split(' ')]
#     profile['G'] = [float(x) for x in fh.readline().strip().split(' ')]
#     profile['T'] = [float(x) for x in fh.readline().strip().split(' ')]

def kmer_prob(kmer, profile):
    prob = 1
    for i in range(len(kmer)):
        curr_prob = profile[kmer[i]][i]
        prob = prob * curr_prob
    return prob

def profile_most_probable_kmer(text, k, profile):
    winner_prob = -1
    winner = ''
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = kmer_prob(kmer, profile)
        if prob > winner_prob:
            winner_prob = prob
            winner = kmer
    return winner

# print(profile_most_probable_kmer(text, k, profile))
