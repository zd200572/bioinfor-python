dic = {}
with open('ASA-24v1-0-Consort_20022506_A1.csv') as f:
	for line in f:
		chromesome = line.strip().split(',')[9]
		#print(chromesome)
		#break
		if chromesome in dic.keys():
			dic[chromesome] += 1
		else:
			dic[chromesome] = 1
fout = open('1.csv', 'w')
for chromesome in dic.keys():
	#print(chromesome, dic[chromesome])
	fout.write(str(chromesome) + '\t' + str(dic[chromesome]) + '\n')

fout.close()