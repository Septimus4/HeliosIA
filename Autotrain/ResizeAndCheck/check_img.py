import sys
import os
import numpy as np

def findInDir(pathdir,ext):
	return [ os.path.join(root, file) for root, dirs, files in os.walk(pathdir) for file in files if file.endswith(ext) ]

import cv2
import xml.etree.ElementTree as ET

class CheckImg:
	def __init__(self,p_img,p_label):
		if not os.path.exists(p_img) or not os.path.exists(p_label):
			print('Error: Input directory not found')
			raise FileNotFoundError
		self.p_img = p_img
		self.p_label = p_label
		self.fileexttofind=[ '.jpg','.jpeg','.png','.JPG' ]
		self.img_list=[]
		self.getData()

	def getData(self,):
		for i in self.fileexttofind:
			self.img_list+=findInDir(self.p_img,i)
		self.xmlname=findInDir(self.p_label,'.xml')

	def run(self,):
		count=0
		for i in self.img_list:
			try:
				t_img = cv2.imread(i)
				height,width = t_img.shape[0],t_img.shape[1]
			except AttributeError:
				print('Error: Invalid picture:',i)
				if os.path.exists(i):
					print('Delete',i)
					os.remove( i )
				match = [s for s in self.xmlname if os.path.basename(i).split('.')[0] in s]
				if len(match)>0 and os.path.exists(match[0]):
					print('Delete',match[0])
					os.remove(match[0])
				continue

			match = [s for s in self.xmlname if os.path.basename(i).split('.')[0] in s]
			if len(match)<=0:
				print('Error: No xml found',i)
				if os.path.exists(i) and (not 'boxes_images' in i):
					print('Delete',i)
					os.remove( i )
				continue
			root = ET.parse(match[0]).getroot()
			for obj in root.findall('object'):
				xmin=int(float(obj.find('./bndbox/xmin').text))
				ymin=int(float(obj.find('./bndbox/ymin').text))
				xmax=int(float(obj.find('./bndbox/xmax').text))
				ymax=int(float(obj.find('./bndbox/ymax').text))

				if xmin>width\
					or xmax>width\
					or ymax>height\
					or ymin>height\
					or ymin<0\
					or ymax<0\
					or xmin<0\
					or xmax<0:
					print('Error: Bounding box too large',i,match[0])
					if os.path.exists(i):
						print('Delete',i)
						os.remove( i )
					if os.path.exists(match[0]):
						print('Delete',match[0])
						os.remove( match[0] )
			count+=1
		print('Images checked:',count)

def main():
	if len(sys.argv)!=2:
		print('Error: Directory needed')
		return
	CheckImg(sys.argv[1],sys.argv[1]).run()

if __name__ == "__main__":
	main()