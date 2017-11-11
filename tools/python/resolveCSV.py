#encoding:gbk

import csv

def createCSV():
	firstData = []
	realData = []
	fileName = []
	path = input("路径名：")
	name = input("文件名：(如果要停止转换请输入exit)")
	flag = 1
	while name != 'exit':
		try:
			with open(path + name + ".csv") as readFile:
				reader = csv.reader(readFile)
				for row in reader:
					if 'Ua' in row[0]:
						row[0] = row[0].replace('Ua', 'A相电压Ua')
						firstData.append(row)
					elif 'Ub' in row[0]:
						row[0] = row[0].replace('Ub', 'B相电压Ub')
						firstData.append(row)
					elif 'Uc' in row[0]:
						row[0] = row[0].replace('Uc', 'C相电压Uc')
						firstData.append(row)
					elif 'Ia' in row[0]:
						row[0] = row[0].replace('Ia', 'A相电流Ia')
						firstData.append(row)
					elif 'Ib' in row[0]:
						row[0] = row[0].replace('Ib', 'B相电流Ib')
						firstData.append(row)
					elif 'Ic' in row[0]:
						row[0] = row[0].replace('Ic', 'C相电流Ic')
						firstData.append(row)
					elif 'Pa' in row[0]:
						row[0] = row[0].replace('Pa', 'A相有功功率Pa')
						firstData.append(row)
					elif 'Pb' in row[0]:
						row[0] = row[0].replace('Pb', 'B相有功功率Pb')
						firstData.append(row)
					elif 'Pc' in row[0]:
						row[0] = row[0].replace('Pc', 'C相有功功率Pc')
						firstData.append(row)
					elif 'Ptotal' in row[0]:
						row[0] = row[0].replace('Ptotal', '三相总有功功率Ptotal')
						firstData.append(row)
					elif 'Qa' in row[0]:
						row[0] = row[0].replace('Qa', 'A相无功功率Qa')
						firstData.append(row)
					elif 'Qb' in row[0]:
						row[0] = row[0].replace('Qb', 'B相无功功率Qb')
						firstData.append(row)
					elif 'Qc' in row[0]:
						row[0] = row[0].replace('Qc', 'C相无功功率Qc')
						firstData.append(row)
					elif 'Qtotal' in row[0]:
						row[0] = row[0].replace('Qtotal', '三相总无功功率Qtotal')
						firstData.append(row)
					elif 'PFa' in row[0]:
						row[0] = row[0].replace('PFa', 'A相功率因数PFa')
						firstData.append(row)
					elif 'PFb' in row[0]:
						row[0] = row[0].replace('PFb', 'B相功率因数PFb')
						firstData.append(row)
					elif 'PFc' in row[0]:
						row[0] = row[0].replace('PFc', 'C相功率因数PFc')
						firstData.append(row)
					elif 'PFtotal' in row[0]:
						row[0] = row[0].replace('PFtotal', '三相总功率因数PFtotal')
						firstData.append(row)
					elif 'Sa' in row[0]:
						row[0] = row[0].replace('Sa', 'A相视在功率Sa')
						firstData.append(row)
					elif 'Sb' in row[0]:
						row[0] = row[0].replace('Sb', 'B相视在功率Sb')
						firstData.append(row)
					elif 'Sc' in row[0]:
						row[0] = row[0].replace('Sc', 'C相视在功率Sc')
						firstData.append(row)
					elif 'Stotal' in row[0]:
						row[0] = row[0].replace('Stotal', '三相总视在功率Stotal')
						firstData.append(row)
					elif '总有功电能高字节' in row[0]:
						row[0] = row[0].replace('总有功电能高字节', '三相总电度量')
						firstData.append(row)
					else:
						firstData.append(row)
				
				for value in firstData:
					if 'A相电压Uab' in value[0]:
						value[0] = value[0].replace('A相电压Uab', 'AB相电压Uab')
						realData.append(value)
					elif 'B相电压Ubc' in value[0]:
						value[0] = value[0].replace('B相电压Ubc', 'BC相电压Ubc')
						realData.append(value)
					elif 'C相电压Uca' in value[0]:
						value[0] = value[0].replace('C相电压Uca', 'CA相电压Uca')
						realData.append(value)
					else:
						realData.append(value)
			readFile.close()
		except IOError:
			print('你输入了错误的文件名，该文件未找到')
			flag = 0

		if flag == 1:
			writeFile = open(path + name + "改.csv", "w", newline = '')
			writer = csv.writer(writeFile)
			for row in realData:
				writer.writerow(row)
			writeFile.close()
			print(name+".csv转换完成！！！")
			fileName.append(name+"改")
			name = input("请继续输入文件名：")
		else:
			name = input("请继续输入文件名：")
	return fileName

createCSV()
