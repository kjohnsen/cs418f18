from hammingdistance import hamming_distance

with open('input.txt', 'r') as fh:
    pattern, text, d = fh.read().splitlines()
    d = int(d)

def approx_occurrences(pattern, text, d):
    result = []
    k = len(pattern)
    for i in range(len(text)-k+1):
        if hamming_distance(pattern, text[i:i+k]) <= d:
            result.append(i)
    return(result)

solution = [str(x) for x in approx_occurrences(pattern, text, d)]
print(' '.join(solution))