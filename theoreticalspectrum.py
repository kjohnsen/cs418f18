from aamass import aa_mass


def peptide_mass(pep):
    mass = 0
    for aa in pep:
        mass += aa_mass[aa]
    return mass

def theoretical_spectrum(pep):
    cyclic_peptide = pep + pep
    t_spec = [0, peptide_mass(pep)]
    for i in range(1, len(pep)):  # subpeptide lengths
        for j in range(len(pep)):  # starting location
            t_spec.append(peptide_mass(cyclic_peptide[j:j+i]))
    t_spec.sort()
    return t_spec


if __name__ == '__main__':
    fh = open('input.txt', 'r')
    pep = fh.readline().strip()
    t_spec = theoretical_spectrum(pep)
    print(' '.join([str(mass) for mass in t_spec]))
