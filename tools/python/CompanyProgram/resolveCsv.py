# coding=gbk

import csv

name = '铸造一厂.csv'
filename = 'E:/常发1@@@@@@@@@@@@@/点表/' + name
data = []
value = []
with open(filename) as f:
	reader = csv.reader(f)
	for row in reader:
		if 'Ua' in row[0]:
			row[0] = row[0].replace('Ua', 'A相电压Ua')
			data.append(row)
		elif 'Ub' in row[0]:
			row[0] = row[0].replace('Ub', 'B相电压Ub')
			data.append(row)
		elif 'Uc' in row[0]:
			row[0] = row[0].replace('Uc', 'C相电压Uc')
			data.append(row)
		elif 'Ia' in row[0]:
			row[0] = row[0].replace('Ia', 'A相电流Ia')
			data.append(row)
		elif 'Ib' in row[0]:
			row[0] = row[0].replace('Ib', 'B相电流Ib')
			data.append(row)
		elif 'Ic' in row[0]:
			row[0] = row[0].replace('Ic', 'C相电流Ic')
			data.append(row)
		elif 'Pa' in row[0]:
			row[0] = row[0].replace('Pa', 'A相有功功率Pa')
			data.append(row)
		elif 'Pb' in row[0]:
			row[0] = row[0].replace('Pb', 'B相有功功率Pb')
			data.append(row)
		elif 'Pc' in row[0]:
			row[0] = row[0].replace('Pc', 'C相有功功率Pc')
			data.append(row)
		elif 'Ptotal' in row[0]:
			row[0] = row[0].replace('Ptotal', '三相总有功功率Ptotal')
			data.append(row)
		elif 'Qa' in row[0]:
			row[0] = row[0].replace('Qa', 'A相无功功率Pa')
			data.append(row)
		elif 'Qb' in row[0]:
			row[0] = row[0].replace('Qb', 'B相无功功率Pb')
			data.append(row)
		elif 'Qc' in row[0]:
			row[0] = row[0].replace('Qc', 'C相无功功率Pc')
			data.append(row)
		elif 'Qtotal' in row[0]:
			row[0] = row[0].replace('Qtotal', '三相总无功功率Qtotal')
			data.append(row)
		elif 'PFa' in row[0]:
			row[0] = row[0].replace('PFa', 'A相功率因数PFa')
			data.append(row)
		elif 'PFb' in row[0]:
			row[0] = row[0].replace('PFb', 'B相功率因数PFb')
			data.append(row)
		elif 'PFc' in row[0]:
			row[0] = row[0].replace('PFc', 'C相功率因数PFc')
			data.append(row)
		elif 'PFtotal' in row[0]:
			row[0] = row[0].replace('PFtotal', '三相总功率因数cos')
			data.append(row)
		elif 'Sa' in row[0]:
			row[0] = row[0].replace('Sa', 'A相视在功率Sa')
			data.append(row)
		elif 'Sb' in row[0]:
			row[0] = row[0].replace('Sb', 'B相视在功率Sb')
			data.append(row)
		elif 'Sc' in row[0]:
			row[0] = row[0].replace('Sc', 'C相视在功率Sc')
			data.append(row)
		elif 'Stotal' in row[0]:
			row[0] = row[0].replace('Stotal', '三相总视在功率Stotal')
			data.append(row)
		elif '总有功电能高字节' in row[0]:
			row[0] = row[0].replace('总有功电能高字节', '三相总电度量')
			data.append(row)
		else:
			data.append(row)
	for row in data:
		if 'A相电压Uab' in row[0]:
			row[0] = row[0].replace('A相电压Uab', 'AB相电压Uab')
			value.append(row)
		elif 'B相电压Ubc' in row[0]:
			row[0] = row[0].replace('B相电压Ubc', 'BC相电压Ubc')
			value.append(row)
		elif 'C相电压Uca' in row[0]:
			row[0] = row[0].replace('C相电压Uca', 'CA相电压Uca')
			value.append(row)
		else:
			value.append(row)
f.close()

file = open('E:/常发1@@@@@@@@@@@@@/点表/' + name + '改.csv','w', newline='')
writer = csv.writer(file)
for row in value:
	writer.writerow(row)
file.close()
