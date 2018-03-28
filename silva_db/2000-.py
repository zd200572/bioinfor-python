fin = open('buccae-1147.fasta')
fout = open('buccae-1147_2000-.fasta', 'w')
phylum = ''
bacteria = ''
genus = ''
genusdict = {}
i = 0
j = 0
leng = 0
flag = 0
sequence = ''
for line in fin:
	if line.startswith('>'):
		#print(leng)
		if leng < 2000:
			fout.write(bacteria)
			fout.write(sequence)
			#print(bacteria, sequence)
			#break
			bacteria = line
			sequence = ''
			leng = 0
			i += 1
		else:
			bacteria = line
			sequence = ''
			leng = 0
	else:
		sequence = sequence + line
		leng += len(line)
print(i) #1515109
fout.close()
