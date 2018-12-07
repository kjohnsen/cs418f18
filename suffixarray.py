import operator

def sa_from_string(string):
    suffix_index_dict = {}
    for i in range(len(string)):
        suffix = string[i:]
        suffix_index_dict[suffix] = i
    return [v for (k, v) in sorted(suffix_index_dict.items(), key=operator.itemgetter(0))]


if __name__ == '__main__':
    fh = open('input.txt', 'r')
    string = fh.readline().strip()
    fh.close()
    sa = sa_from_string(string)
    sa = [str(x) for x in sa]
    ofh = open('output.txt', 'w')
    result = ', '.join(sa)
    print(result)
    ofh.write(result)