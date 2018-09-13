from collections import Counter

with open('input.txt') as fh:
    genome = fh.readline()

define skew(dna):
    output = [0]
    for i in range(1, len(dna)):
        if dna[i] == 'G':
            increment = 1
        if dna[i] == 'C':
            increment = -1
        output[i] = output[i-1] + increment

min_skew = float('inf')

for i in range(len(genome)):

