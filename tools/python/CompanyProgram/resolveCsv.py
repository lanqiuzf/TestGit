# coding=gbk

import csv

name = '����һ��.csv'
filename = 'E:/����1@@@@@@@@@@@@@/���/' + name
data = []
value = []
with open(filename) as f:
	reader = csv.reader(f)
	for row in reader:
		if 'Ua' in row[0]:
			row[0] = row[0].replace('Ua', 'A���ѹUa')
			data.append(row)
		elif 'Ub' in row[0]:
			row[0] = row[0].replace('Ub', 'B���ѹUb')
			data.append(row)
		elif 'Uc' in row[0]:
			row[0] = row[0].replace('Uc', 'C���ѹUc')
			data.append(row)
		elif 'Ia' in row[0]:
			row[0] = row[0].replace('Ia', 'A�����Ia')
			data.append(row)
		elif 'Ib' in row[0]:
			row[0] = row[0].replace('Ib', 'B�����Ib')
			data.append(row)
		elif 'Ic' in row[0]:
			row[0] = row[0].replace('Ic', 'C�����Ic')
			data.append(row)
		elif 'Pa' in row[0]:
			row[0] = row[0].replace('Pa', 'A���й�����Pa')
			data.append(row)
		elif 'Pb' in row[0]:
			row[0] = row[0].replace('Pb', 'B���й�����Pb')
			data.append(row)
		elif 'Pc' in row[0]:
			row[0] = row[0].replace('Pc', 'C���й�����Pc')
			data.append(row)
		elif 'Ptotal' in row[0]:
			row[0] = row[0].replace('Ptotal', '�������й�����Ptotal')
			data.append(row)
		elif 'Qa' in row[0]:
			row[0] = row[0].replace('Qa', 'A���޹�����Pa')
			data.append(row)
		elif 'Qb' in row[0]:
			row[0] = row[0].replace('Qb', 'B���޹�����Pb')
			data.append(row)
		elif 'Qc' in row[0]:
			row[0] = row[0].replace('Qc', 'C���޹�����Pc')
			data.append(row)
		elif 'Qtotal' in row[0]:
			row[0] = row[0].replace('Qtotal', '�������޹�����Qtotal')
			data.append(row)
		elif 'PFa' in row[0]:
			row[0] = row[0].replace('PFa', 'A�๦������PFa')
			data.append(row)
		elif 'PFb' in row[0]:
			row[0] = row[0].replace('PFb', 'B�๦������PFb')
			data.append(row)
		elif 'PFc' in row[0]:
			row[0] = row[0].replace('PFc', 'C�๦������PFc')
			data.append(row)
		elif 'PFtotal' in row[0]:
			row[0] = row[0].replace('PFtotal', '�����ܹ�������cos')
			data.append(row)
		elif 'Sa' in row[0]:
			row[0] = row[0].replace('Sa', 'A�����ڹ���Sa')
			data.append(row)
		elif 'Sb' in row[0]:
			row[0] = row[0].replace('Sb', 'B�����ڹ���Sb')
			data.append(row)
		elif 'Sc' in row[0]:
			row[0] = row[0].replace('Sc', 'C�����ڹ���Sc')
			data.append(row)
		elif 'Stotal' in row[0]:
			row[0] = row[0].replace('Stotal', '���������ڹ���Stotal')
			data.append(row)
		elif '���й����ܸ��ֽ�' in row[0]:
			row[0] = row[0].replace('���й����ܸ��ֽ�', '�����ܵ����')
			data.append(row)
		else:
			data.append(row)
	for row in data:
		if 'A���ѹUab' in row[0]:
			row[0] = row[0].replace('A���ѹUab', 'AB���ѹUab')
			value.append(row)
		elif 'B���ѹUbc' in row[0]:
			row[0] = row[0].replace('B���ѹUbc', 'BC���ѹUbc')
			value.append(row)
		elif 'C���ѹUca' in row[0]:
			row[0] = row[0].replace('C���ѹUca', 'CA���ѹUca')
			value.append(row)
		else:
			value.append(row)
f.close()

file = open('E:/����1@@@@@@@@@@@@@/���/' + name + '��.csv','w', newline='')
writer = csv.writer(file)
for row in value:
	writer.writerow(row)
file.close()
