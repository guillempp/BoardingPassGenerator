from BarcodeGen import BarcodeGen
import base64
import re

#MAIN CLASS
def main():
	#Object inits
	barcodeGen = BarcodeGen()


	# Some data to encode
	text = "SMITH/JOHN NTH243E JFKBCN DL267 012A 0029 0061237465837 DL 123456783"
	barcodeGen.generateBarcode(text)
	displayInfo(text)

def displayInfo(text):
	print("===================================================")
	tm = re.match('^([^\s]+)', text)
	print("Barcode Generated for: {}".format(tm.group()))
	print("===================================================")

if __name__ == '__main__':
	main()