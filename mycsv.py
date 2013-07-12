import csv
import string

def main():
	"""docstring for fname"""
	print "CSV file Analyzer"

	try:
		csvfile = open("test.csv",'rb')
	except IOError:
		print "Open CSV file error"
	csvdata = csv.reader(csvfile)
	
	i = 0
	datalist = []
	print "Header:"
	for row in csvdata:
		if i >= 9:
			datalist.append(row)
		else:
			print row
		i = i + 1

	i = 1;
	value = []
	for valueline in datalist:
		value.append(string.atoi(valueline[1]))
		i = i + 1
		#print valueline[1]
	print "real data:"
	print datalist[1]
	print "max: " + max(datalist[:][2])
	print "total: " + str(len(datalist))
	print value[0]
	print value[1]
	csvfile.close()
	print "ended"


if __name__ == "__main__":
    main()
