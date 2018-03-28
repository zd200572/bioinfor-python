fin = open('Bacteroides-ncbi-strain.fasta')
fout = open('Bacteroides-ncbi-strain-.fasta', 'w')
phylum = ''
dic = {}
i = 1

flag = 0
for line in fin:
	if line.startswith('>'):
		flag = 0
		if ']' in line or '-like'  in line :
			flag = 1
			fout.write(line)
			continue
		phylum = line.strip().split('Bacteroides ')[1].split(' ')[0]
		#print(phylum)
		#break
		if phylum not in dic.keys():
		#if phylum == 'Akkermansia':
			flag = 1
			fout.write(line)
			#print(line, i)
			i += 1
			j = 1
			#break
			dic[phylum] = ''
		elif phylum  in dic.keys() and j < 10:
			flag = 1
			fout.write(line)
			j += 1
	elif flag == 1:
		fout.write(line)
#print(dict)
print(i)
fout.close()
