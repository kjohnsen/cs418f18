with open('input.txt') as fh:
    dna1 = fh.readline().strip()
    dna2 = fh.readline().strip()

def hamming_distance(dna1, dna2):
    result = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            result += 1
    return(result)

# print(hamming_distance(dna1, dna2))

