from collections import Counter

with open('input.txt') as fh:
    genome = fh.readline()

def skew(dna):
    output = [0]
    for i in range(1, len(dna)+1):
        if dna[i-1] == 'G':
            increment = 1
        elif dna[i-1] == 'C':
            increment = -1
        else:
            increment = 0
        output.append(output[i-1] + increment)
    return output

genome_skew = skew(genome)
min_skew = min(genome_skew)

result = []
for i in range(len(genome_skew)):
    if genome_skew[i] == min_skew:
        result.append(str(i))

print(' '.join(result))