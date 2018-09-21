with open('input.txt', 'r') as fh:
    string = fh.readline().strip()
    d = int(fh.readline().strip())

def d_neighborhood(string, d):
    result = set()
    result.add(string)
    for j in range(d):
        new_result = set()
        for string in result:
            for i in range(len(string)):
                for nuc in ['A', 'C', 'G', 'T']:
                    new_string = string[0:i] + nuc + string[i+1:]
                    new_result.add(new_string)
        result.update(new_result)
    return(result)


result = d_neighborhood(string, d)
with open('output.txt', 'w') as fh:
    for kmer in result:
        fh.write(kmer + '\n')