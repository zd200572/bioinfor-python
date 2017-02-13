complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

complement['A']

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
print(reverseComplement('ACCATTG'))
