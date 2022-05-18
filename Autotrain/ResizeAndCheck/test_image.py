import unittest
import os

from image import resize

class CConvImgTest(unittest.TestCase):
	def test_resize(self,):
		resize(
			'./test/tps_img.JPG',
			'./test/tps_xml.xml',
			(300,300),
			'./out/',
			save_box_images=True
		)

	def test_bad(self,):
		with self.assertRaises(AttributeError):
			resize(
				'./test/bad.JPG',
				'./test/bad.xml',
				(900,900),
				'./out',
				save_box_images=True
			)

if __name__ == "__main__":
	unittest.main()