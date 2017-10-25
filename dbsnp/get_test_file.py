fin = open('D:\\all_snp.csv')
fout = open('D:\\1all_snp.csv','w')
i = 0
for line in fin:
	if i < 1:
		fout.write(line + '\n')
		i += 1
fout.close()
