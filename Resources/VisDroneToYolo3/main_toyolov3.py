import os,sys
import cv2

def findInDir(pathdir,ext):
	return [ os.path.join(root, file)\
		for root, dirs, files in os.walk(pathdir)\
			for file in files\
				if file.endswith(ext) ]

class ConvertLabel:
	def __init__(self,path):
		self.path = path
		self.l_txt = self._getfilenames()
		self.l_img = self._processipath()
		self.p_ffile = './pic_train_data.txt'
		self.ffile = open(self.p_ffile,'w')
		self.cattokeep = {
			'1':'0',
			'2':'1',
			'3':'2',
			'4':'3',
			'5':'4',
			'6':'5',
			'7':'6',
			'8':'7',
			'9':'8',
			'10':'9',
		}

	def __del__(self,):
		self.ffile.close()

	def _getfilenames(self,):
		return findInDir(self.path,'.txt')

	def _processipath(self,):
		return { i:os.path.abspath( i.split('.txt')[0]+'.jpg' )\
			for i in self.l_txt }

	def _writer(self,towrite):
		self.ffile.write(towrite)

	@staticmethod
	def _show(p_img,it_m_data):
		img = cv2.imread(p_img)
		for m_data in it_m_data:
			img = cv2.rectangle(img,(m_data[0],m_data[1]),(m_data[2],m_data[3]),(0,255,0),2)
		cv2.imshow('Oui',img)
		cv2.waitKey(0)

	@staticmethod
	def build(p_file,box):
		return p_file+' '\
			+' '.join([ ','.join([ j for j in i ]) for i in box ])\
			+'\n'

	def parse(self,m_file):
		t_file = open(m_file,'r')
		t_data = t_file.readlines()
		t_file.close()
		t_data = [ i.split('\n')[0] for i in t_data]
		towrite = []
		for i in t_data:
			toget = i.split(',')
			left,top,width,height,obj = toget[0],toget[1],toget[2],toget[3],toget[5]
			if obj not in self.cattokeep.keys():
				continue
			towrite.append([ str(int(left)),str(int(top)),str(int(left)+int(width)),str(int(top)+int(height)),self.cattokeep[obj] ])
		self._writer(self.build(self.l_img[m_file],towrite))

	def run(self,):
		for i in self.l_txt:
			self.parse(i)

def main():
	if len(sys.argv)!=2:
		print('Error: Incorrect number of arguments')
		return
	ConvertLabel(sys.argv[1]).run()

if __name__ == "__main__":
	main()