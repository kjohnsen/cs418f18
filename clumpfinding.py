from collections import Counter

with open('input.txt') as fh:
    dna = fh.readline()
    k, L, t = [int(x) for x  in fh.readline().split(' ')]

print(k, L, t)

output = set()
for i in range(len(dna)-L+1):
    kmercounts = Counter()
    for j in range(i, i+L):
        kmer = dna[j:j+k]
        kmercounts[kmer] += 1
    for kmer_count in kmercounts.most_common():
        if kmer_count[1] >= t:
            output.add(kmer_count[0])
        else:
            break

print(' '.join(output))