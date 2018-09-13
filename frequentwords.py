from collections import Counter

with open('input.txt') as fh:
    dna = fh.readline()
    k = int(fh.readline())

kmercounts = Counter()
for i in range(len(dna) - k + 1):
    kmer = dna[i:i+k]
    kmercounts[kmer] += 1

max_count = kmercounts.most_common(1)[0][1]
print(max_count)
winners = []
for kmer_count in kmercounts.most_common():
    if kmer_count[1] == max_count:
        winners.append(kmer_count[0])

print(' '.join(winners))