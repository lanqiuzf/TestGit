# encoding: utf-8

import csv
import xlwt

path = ''
csvName = []
mode = 0

def createCSV():
	firstData = []
	realData = []
	fileName = []
	name = input('文件名：(如果要停止转换请输入exit)')
	flag = 1
	while name != 'exit':
		try:
			with open(path + name + '.csv') as readFile:
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
			flag = 1
		except IOError:
			print('你输入了错误的文件名，该文件未找到')
			flag = 0

		if flag == 1:
			writeFile = open(path + name + "改.csv", "w", newline = '')
			writer = csv.writer(writeFile)
			for row in realData:
				writer.writerow(row)
			writeFile.close()
			print(name+".csv转换完成")
			fileName.append(name)
			name = input("请继续输入文件名：")
		else:
			name = input("请继续输入文件名：")
	return fileName

def DataToXlsByList(fileName):
	originData = []
	rowValue = []
	yxIndex = 0
	ycIndex = 0
	ymIndex = 0
	ykIndex = 0
	ytIndex = 0
	yxList = []
	ycList = []
	ymList = []
	ykList = []
	ytList = []
	for csvName in fileName:
		with open(path + csvName + ".csv") as readFile:
			reader = csv.reader(readFile)
			for row in reader:
				originData.append(row)
			for i in range(0, len(originData)):
				rowValue = originData[i]
				if '[遥信量]' == rowValue[0]:
					yxIndex = i
				elif '[遥测量]' == rowValue[0]:
					ycIndex = i
				elif '[遥脉量]' == rowValue[0]:
					ymIndex = i
				elif '[遥控量]' == rowValue[0]:
					ykIndex = i
				elif '[遥调量]' == rowValue[0]:
					ytIndex = i
			for i in range(yxIndex + 1, ycIndex):
				yxList.append(originData[i])
			for i in range(ycIndex + 1, ymIndex):
				ycList.append(originData[i])
			for i in range(ymIndex + 1, ykIndex):
				ymList.append(originData[i])
			for i in range(ykIndex + 1, ytIndex):
				ykList.append(originData[i])
			for i in range(ytIndex + 1, len(originData)):
				ytList.append(originData[i])
		readFile.close()

		#生成xls文件
		value = []
		xls = xlwt.Workbook(csvName + '.xls')
		sheetYK = xls.add_sheet('yk')
		sheetYC = xls.add_sheet('yc')
		sheetYT = xls.add_sheet('yt')
		sheetYX = xls.add_sheet('yx')
		sheetYM = xls.add_sheet('ym')
		index = 0
		name = ''
		coeff = 0
		base = 0
		for i in range(0, len(ykList)):
			value = ykList[i]
			index = value[0].split('=')[0]
			name = value[0].split('=')[1]
			sheetYK.write(i, 0, int(index))
			sheetYK.write(i, 1, name)

		for i in range(0, len(ycList)):
			value = ycList[i]
			index = value[0].split('=')[0]
			name = value[0].split('=')[1]
			coeff = value[1]
			sheetYC.write(i, 0, int(index))
			sheetYC.write(i, 1, name)
			sheetYC.write(i, 2, float(coeff))
			sheetYC.write(i, 3, float(base))

		for i in range(0, len(ytList)):
			value = ytList[i]
			index = value[0].split('=')[0]
			name = value[0].split('=')[1]
			sheetYT.write(i, 0, int(index))
			sheetYT.write(i, 1, name)

		for i in range(0, len(yxList)):
			value = yxList[i]
			index = value[0].split('=')[0]
			name = value[0].split('=')[1]
			sheetYX.write(i, 0, int(index))
			sheetYX.write(i, 1, name)

		for i in range(0, len(ymList)):
			value = ymList[i]
			index = value[0].split('=')[0]
			name = value[0].split('=')[1]
			coeff = value[1]
			sheetYM.write(i, 0, int(index))
			sheetYM.write(i, 1, name)
			sheetYM.write(i, 2, float(coeff))
			sheetYM.write(i, 3, float(base))
		xls.save(path + csvName+'.xls')

def DataToXlsByName():
	csvName = input("文件名：(如果要停止转换请输入exit)")
	flag = 1
	originData = []
	rowValue = []
	yxIndex = 0
	ycIndex = 0
	ymIndex = 0
	ykIndex = 0
	ytIndex = 0
	yxList = []
	ycList = []
	ymList = []
	ykList = []
	ytList = []
	while csvName != 'exit':
		try:
			with open(path + csvName + ".csv") as readFile:
				reader = csv.reader(readFile)
				for row in reader:
					originData.append(row)
				for i in range(0, len(originData)):
					rowValue = originData[i]
					if '[遥信量]' == rowValue[0]:
						yxIndex = i
					elif '[遥测量]' == rowValue[0]:
						ycIndex = i
					elif '[遥脉量]' == rowValue[0]:
						ymIndex = i
					elif '[遥控量]' == rowValue[0]:
						ykIndex = i
					elif '[遥调量]' == rowValue[0]:
						ytIndex = i
				for i in range(yxIndex + 1, ycIndex):
					yxList.append(originData[i])
				for i in range(ycIndex + 1, ymIndex):
					ycList.append(originData[i])
				for i in range(ymIndex + 1, ykIndex):
					ymList.append(originData[i])
				for i in range(ykIndex + 1, ytIndex):
					ykList.append(originData[i])
				for i in range(ytIndex + 1, len(originData)):
					ytList.append(originData[i])
				readFile.close()
				flag = 1
		except IOError:
			print('你输入了错误的文件名，该文件未找到')
			flag = 0

		if flag == 1:
			#生成xls文件
			value = []
			xls = xlwt.Workbook(csvName + '.xls')
			sheetYK = xls.add_sheet('yk')
			sheetYC = xls.add_sheet('yc')
			sheetYT = xls.add_sheet('yt')
			sheetYX = xls.add_sheet('yx')
			sheetYM = xls.add_sheet('ym')
			index = 0
			name = ''
			coeff = 0
			base = 0
			for i in range(0, len(ykList)):
				value = ykList[i]
				index = value[0].split('=')[0]
				name = value[0].split('=')[1]
				sheetYK.write(i, 0, int(index))
				sheetYK.write(i, 1, name)

			for i in range(0, len(ycList)):
				value = ycList[i]
				index = value[0].split('=')[0]
				name = value[0].split('=')[1]
				coeff = value[1]
				sheetYC.write(i, 0, int(index))
				sheetYC.write(i, 1, name)
				sheetYC.write(i, 2, float(coeff))
				sheetYC.write(i, 3, float(base))

			for i in range(0, len(ytList)):
				value = ytList[i]
				index = value[0].split('=')[0]
				name = value[0].split('=')[1]
				sheetYT.write(i, 0, int(index))
				sheetYT.write(i, 1, name)

			for i in range(0, len(yxList)):
				value = yxList[i]
				index = value[0].split('=')[0]
				name = value[0].split('=')[1]
				sheetYX.write(i, 0, int(index))
				sheetYX.write(i, 1, name)

			for i in range(0, len(ymList)):
				value = ymList[i]
				index = value[0].split('=')[0]
				name = value[0].split('=')[1]
				coeff = value[1]
				sheetYM.write(i, 0, int(index))
				sheetYM.write(i, 1, name)
				sheetYM.write(i, 2, float(coeff))
				sheetYM.write(i, 3, float(base))
			xls.save(path + csvName+'.xls')
			print('生成' + path + csvName+'.xls成功！！！')
			csvName = input('请继续输入文件名：')
		else: 
			csvName = input('请继续输入文件名：')

if __name__ == '__main__':
	path = input('请输入你进行操作的文件所在文件夹路径:')
	mode = input('请选择模式:\n1.生成"改.csv"和点表;\n2.只生成点表;')
	if int(mode) == 1:
		csvName = createCSV()
		DataToXlsByList(csvName)
	elif int(mode) == 2:
		DataToXlsByName()
