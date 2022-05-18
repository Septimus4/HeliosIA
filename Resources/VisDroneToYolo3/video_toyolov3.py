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
		self.p_ffile = './video_train_data.txt'
		self.ffile = open(self.p_ffile,'w')
		self.cattokeep = {
			'1':'0','2':'0',
			'3':'1','7':'1','10':'1',
			'5':'2','4':'2',
			'6':'3','9':'3'
		}
		#people bike truck car
	def __del__(self,):
		self.ffile.close()

	def _getfilenames(self,):
		return findInDir(self.path,'.txt')

	def _writer(self,towrite):
		self.ffile.write(towrite)

	@staticmethod
	def _show(p_img,it_m_data):
		img = cv2.imread(p_img)
		for m_data in it_m_data:
			img = cv2.rectangle(img,(int(m_data[0]),int(m_data[1])),(int(m_data[2]),int(m_data[3])),(0,255,0),2)
		cv2.imshow('Oui',img)
		cv2.waitKey(0)

	@staticmethod
	def build(data):
		rt=""
		for key,box in data.items():
			rt+=key+' '+' '.join([ ','.join([ j for j in i ]) for i in box ])+'\n'
		return rt

	def getPicName(self,idframe,txtpath):
		def buildfname(mid):
			rt = ""
			for _ in range(7-len(str(mid))):
				rt+='0'
			return rt+str(mid)
		nameofcapture = os.path.basename(txtpath).split('.txt')[0]
		t_path = os.path.dirname(os.path.abspath(txtpath))+'/../sequences/'+nameofcapture+'/'+buildfname(idframe)+'.jpg'
		return os.path.abspath(t_path)

	def parse(self,m_file):
		t_file = open(m_file,'r')
		t_data = t_file.readlines()
		t_file.close()
		t_data = [ i.split('\n')[0] for i in t_data]
		towrite = {}
		for i in t_data:
			toget = i.split(',')
			fname,left,top,width,height,obj = toget[0],toget[2],toget[3],toget[4],toget[5],toget[7]
			path_of_jpg = self.getPicName( fname,m_file )
			if obj not in self.cattokeep.keys():
				continue
			if path_of_jpg not in towrite.keys():
				towrite[path_of_jpg]=[]
			towrite[path_of_jpg].append([ str(int(left)),str(int(top)),str(int(left)+int(width)),str(int(top)+int(height)),self.cattokeep[obj] ])
		self._writer(self.build(towrite))

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