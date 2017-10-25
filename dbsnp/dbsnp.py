fin = open('D:\\All_20170710.vcf')
fout = open('D:\\all_snp.csv', 'w')
i =0
for line in fin:
	if line[0] !='#':
		t = line.strip().split('\t')
		line = t[0] +'\t'+ t[2] + '\t' + t[3] + '\t' + t[4]
		i += 1
		#print(i, t)
		#print(str(i) + '\t' + line + '\n')
		fout.write(str(i) + '\t' + line + '\n')
		#break
print(i)
fout.close()

