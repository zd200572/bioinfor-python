# generate a random nucleotide
import random
random.choice('ACGT')


# generate a random sequence
seq = ''
for _ in range(10):
    seq += random.choice('ACGT')
print(seq)

# another way to generate a random sequence
seq = ''.join([random.choice('ACGT') for _ in range(10)])
print(seq)


