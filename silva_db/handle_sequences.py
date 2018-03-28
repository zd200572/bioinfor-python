fin = open('current_Bacteria_unaligned')
fout = open('Prevotella-silva.fasta', 'w')
phylum = ''
#dict = set()
i = 1
flag = 0
for line in fin:
	if line.startswith('>'):
		flag = 0
		#phylum = line.strip().split(';')[-2]
		if 'Prevotella' in line:
		#if phylum == 'Akkermansia':
			flag = 1
			fout.write(line)
			#print(line, i)
			i += 1
		#break
		#dict.add(phylum)
		
	elif flag == 1:
		fout.write(line)
#print(dict)
print(i)
fout.close()
