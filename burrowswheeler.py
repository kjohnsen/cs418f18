from collections import Counter


def bwt(text):
    cyc_rots = []
    for i in range(len(text)):
        cyc_rots.append(text[i:] + text[:i])
    cyc_rots.sort()
    first_col = [x[0] for x in cyc_rots]
    last_col = [x[-1] for x in cyc_rots]
    return first_col, last_col

def last_to_first(first, last):
    starts = {}
    for i in range(len(first)):
        char = first[i]
        if char not in starts.keys():
            starts[char] = i
    counter = Counter()
    result = []
    for i in range(len(last)):
        char = last[i]
        first_pos = starts[char] + counter[char]
        result.append(first_pos)
        counter[char] += 1
    return result




if __name__ == '__main__':
    # fh = open('input.txt', 'r')
    # text = fh.readline().strip()
    # print(bwt(text))
    print(last_to_first('$AACCGT', 'T$GACCA'))
