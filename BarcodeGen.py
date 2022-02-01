from pdf417 import encode, render_image, render_svg
import io

class BarcodeGen():
	#OWN CLASS - BarcodeGen
	def generateBarcode(self, text):
		codes = encode(text, columns=7, security_level=4)
		image = render_image(codes, scale=4, ratio=3, fg_color="black", bg_color="#FFFFFF")
		image.show()

	def generateBarcodeForWeb(self, text):
		codes = encode(text, columns=7, security_level=4)
		image = render_image(codes, scale=4, ratio=3, fg_color="black", bg_color="#FFFFFF")
		return image
