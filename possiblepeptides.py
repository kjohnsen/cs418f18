from aamass import aa_mass

def num_possible_peptides_for_mass(mass):
    aa_masses = list(aa_mass.values())
    count_array = []
    for i in range(mass + 1):
        possible_peptides_count = 0
        if i <= 186:
            if aa_masses.__contains__(i):
                possible_peptides_count += 1
        for am in aa_masses:
            if i - am >= 0:
                if i < 200 and i > 186: print(count_array)
                possible_peptides_count += count_array[i - am]
                if i < 200 and i > 186: print(possible_peptides_count)
        count_array.append(possible_peptides_count)
    return count_array[-1]





if __name__ == '__main__':
    fh = open('input.txt', 'r')
    mass = int(fh.readline().strip())
    print(num_possible_peptides_for_mass(mass))
