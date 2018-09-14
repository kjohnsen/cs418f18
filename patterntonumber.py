with open('input.txt', 'r') as fh:
    pattern = fh.readline().strip()

SYMBOL_TO_NUMBER = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}
def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4*pattern_to_number(prefix) + SYMBOL_TO_NUMBER[symbol]

print(pattern_to_number(pattern))