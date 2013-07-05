import csv

def main():
	"""docstring for fname"""
	print "CSV file Analyzer"

	try:
		csvfile = open("test.csv",'rb')
	except IOError:
		print "Open CSV file error"
	csvdata = csv.reader(csvfile)
	
	i = 0
	for row in csvdata:
		if i == 10:
			break
		i = i + 1
		print row

	csvfile.close()
	print "ended"


if __name__ == "__main__":
    main()
