import unittest
import os
import shutil

from check_img import CheckImg

def m_copy():
	tocopy = [
		'./save_test/tps_img.JPG',
		'./save_test/tps_img.xml',
		'./save_test/oui.jpg',
		'./save_test/tps_without_xml.JPG'
	]
	[ shutil.copy( i,'./test' ) for i in tocopy ]

class CLabelImg(unittest.TestCase):
	def test_badinputdir(self,):
		with self.assertRaises(FileNotFoundError):
			CheckImg('NotExists','NotExists')
		with self.assertRaises(FileNotFoundError):
			CheckImg('NotExists','./test')
		with self.assertRaises(FileNotFoundError):
			CheckImg('./test','NotExists')
		m_copy()

	def test_getdata(self,):
		c=CheckImg('./test','./test')
		self.assertEqual(len(c.xmlname),1)
		self.assertEqual(len(c.img_list),3)
		m_copy()

	def test_getdatabaddir(self,):
		c=CheckImg('__pycache__','__pycache__')
		self.assertEqual(len(c.xmlname),0)
		self.assertEqual(len(c.img_list),0)
		m_copy()

	def test_run(self,):
		c=CheckImg('./test','./test')
		c.run()
		n_file = len(os.listdir('./test'))
		self.assertEqual(n_file,0)
		m_copy()

if __name__ == "__main__":
	unittest.main()