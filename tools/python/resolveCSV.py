#encoding:gbk

import csv

def createCSV():
	firstData = []
	realData = []
	fileName = []
	path = input("·������")
	name = input("�ļ�����(���Ҫֹͣת��������exit)")
	flag = 1
	while name != 'exit':
		try:
			with open(path + name + ".csv") as readFile:
				reader = csv.reader(readFile)
				for row in reader:
					if 'Ua' in row[0]:
						row[0] = row[0].replace('Ua', 'A���ѹUa')
						firstData.append(row)
					elif 'Ub' in row[0]:
						row[0] = row[0].replace('Ub', 'B���ѹUb')
						firstData.append(row)
					elif 'Uc' in row[0]:
						row[0] = row[0].replace('Uc', 'C���ѹUc')
						firstData.append(row)
					elif 'Ia' in row[0]:
						row[0] = row[0].replace('Ia', 'A�����Ia')
						firstData.append(row)
					elif 'Ib' in row[0]:
						row[0] = row[0].replace('Ib', 'B�����Ib')
						firstData.append(row)
					elif 'Ic' in row[0]:
						row[0] = row[0].replace('Ic', 'C�����Ic')
						firstData.append(row)
					elif 'Pa' in row[0]:
						row[0] = row[0].replace('Pa', 'A���й�����Pa')
						firstData.append(row)
					elif 'Pb' in row[0]:
						row[0] = row[0].replace('Pb', 'B���й�����Pb')
						firstData.append(row)
					elif 'Pc' in row[0]:
						row[0] = row[0].replace('Pc', 'C���й�����Pc')
						firstData.append(row)
					elif 'Ptotal' in row[0]:
						row[0] = row[0].replace('Ptotal', '�������й�����Ptotal')
						firstData.append(row)
					elif 'Qa' in row[0]:
						row[0] = row[0].replace('Qa', 'A���޹�����Qa')
						firstData.append(row)
					elif 'Qb' in row[0]:
						row[0] = row[0].replace('Qb', 'B���޹�����Qb')
						firstData.append(row)
					elif 'Qc' in row[0]:
						row[0] = row[0].replace('Qc', 'C���޹�����Qc')
						firstData.append(row)
					elif 'Qtotal' in row[0]:
						row[0] = row[0].replace('Qtotal', '�������޹�����Qtotal')
						firstData.append(row)
					elif 'PFa' in row[0]:
						row[0] = row[0].replace('PFa', 'A�๦������PFa')
						firstData.append(row)
					elif 'PFb' in row[0]:
						row[0] = row[0].replace('PFb', 'B�๦������PFb')
						firstData.append(row)
					elif 'PFc' in row[0]:
						row[0] = row[0].replace('PFc', 'C�๦������PFc')
						firstData.append(row)
					elif 'PFtotal' in row[0]:
						row[0] = row[0].replace('PFtotal', '�����ܹ�������PFtotal')
						firstData.append(row)
					elif 'Sa' in row[0]:
						row[0] = row[0].replace('Sa', 'A�����ڹ���Sa')
						firstData.append(row)
					elif 'Sb' in row[0]:
						row[0] = row[0].replace('Sb', 'B�����ڹ���Sb')
						firstData.append(row)
					elif 'Sc' in row[0]:
						row[0] = row[0].replace('Sc', 'C�����ڹ���Sc')
						firstData.append(row)
					elif 'Stotal' in row[0]:
						row[0] = row[0].replace('Stotal', '���������ڹ���Stotal')
						firstData.append(row)
					elif '���й����ܸ��ֽ�' in row[0]:
						row[0] = row[0].replace('���й����ܸ��ֽ�', '�����ܵ����')
						firstData.append(row)
					else:
						firstData.append(row)
				
				for value in firstData:
					if 'A���ѹUab' in value[0]:
						value[0] = value[0].replace('A���ѹUab', 'AB���ѹUab')
						realData.append(value)
					elif 'B���ѹUbc' in value[0]:
						value[0] = value[0].replace('B���ѹUbc', 'BC���ѹUbc')
						realData.append(value)
					elif 'C���ѹUca' in value[0]:
						value[0] = value[0].replace('C���ѹUca', 'CA���ѹUca')
						realData.append(value)
					else:
						realData.append(value)
			readFile.close()
		except IOError:
			print('�������˴�����ļ��������ļ�δ�ҵ�')
			flag = 0

		if flag == 1:
			writeFile = open(path + name + "��.csv", "w", newline = '')
			writer = csv.writer(writeFile)
			for row in realData:
				writer.writerow(row)
			writeFile.close()
			print(name+".csvת����ɣ�����")
			fileName.append(name+"��")
			name = input("����������ļ�����")
		else:
			name = input("����������ļ�����")
	return fileName

createCSV()
