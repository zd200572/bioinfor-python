fin = open('D:\\all_snp.csv')
di = {}
chromesome = '1'
no = 0
for line in fin:
	#print(line.strip().split('\t')[1])
	#print(chromesome)
	if line.strip().split('\t')[1] == chromesome:
		no += 1
	else:
		di[chromesome] = no
		#print(no)
		no = 0
		chromesome = line.strip().split('\t')[1]
		#break
print(di)

			