import os,sys
import cv2

def findInDir(pathdir,ext):
	return [ os.path.join(root, file)\
		for root, dirs, files in os.walk(pathdir)\
			for file in files\
				if file.endswith(ext) ]

class XmlWriter:
	def __init__(self,filename,imgfilename):
		self.xmlfilename = filename.split('.txt')[0]+'.xml'
		self.imgfilename = imgfilename
		self.xmlfile = open(self.xmlfilename,'w')

	def __del__(self,):
		self.xmlfile.close()

	@staticmethod
	def _getSize(path,m_type):
		t_img = cv2.imread(path)
		return t_img.shape[0]\
			if m_type == 'height' else t_img.shape[1]

	@staticmethod
	def _objBuilder(m_obj):
		return {
			'name':m_obj['classe'],
			'pose':'Unspecified',
			'truncated':0,
			'difficult':0,
			'bndbox': {
				'xmin':m_obj['xmin'],
				'ymin':m_obj['ymin'],
				'xmax':m_obj['xmax'],
				'ymax':m_obj['ymax'],
			}
		}

	def buildXml(self,data,root='annotation',level=1):
		base = ''.join(['\t' for _ in range(level-1)])+'<'+root+'>\n'
		for key,i in data.items():
			if type(i)==list:
				base+='\n'.join([ self.buildXml(data=it_list,root=key,level=level+1) for it_list in i ])+'\n'
			elif type(i)==dict:
				base+=self.buildXml( data=i,root=key,level=level+1 )+'\n'
			else:
				base+=''.join(['\t' for _ in range(level)])+'<'+key+'>'+str(i)+'</'+key+'>\n'
		base+=''.join(['\t' for _ in range(level-1)])+'</'+root+'>'
		return base

	def varbuilder(self,data):
		var_data = {}
		var_data['filename'] = os.path.basename(self.imgfilename)
		var_data['folder'] = self.imgfilename.split(var_data['filename'])[0]
		var_data['path'] = self.imgfilename
		var_data['source']={'database':'Unknow'}
		var_data['size'] = {
			'width':self._getSize(self.imgfilename,'width'),
			'height':self._getSize(self.imgfilename,'height'),
			'depth':3 }
		var_data['segmented'] = 0
		var_data['object'] = [ self._objBuilder(i) for i in data ]
		res = self.buildXml(var_data)
		self.xmlfile.write(res)

class ConvertLabel:
	def __init__(self,path):
		self.path = path
		self.l_txt = self._getfilenames()
		self.l_img = self._processipath()
		self.cattokeep = {
			'1':'people','2':'people',
			'3':'bike','7':'bike','10':'bike',
			'5':'car','4':'car',
			'6':'truck','9':'truck'
		}
		#people bike truck car

	def _getfilenames(self,):
		return findInDir(self.path,'.txt')

	def _processipath(self,):
		return { i:os.path.abspath( i.split('.txt')[0]+'.jpg' )\
			for i in self.l_txt }

	@staticmethod
	def _show(p_img,it_m_data):
		img = cv2.imread(p_img)
		for m_data in it_m_data:
			img = cv2.rectangle(img,
				(m_data[0],m_data[1]),
				(m_data[2],m_data[3]),
				(0,255,0),2)
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
			towrite.append({ 'xmin':str(int(left)),
				'ymin':str(int(top)),
				'xmax':str(int(left)+int(width)),
				'ymax':str(int(top)+int(height)),
				'classe':self.cattokeep[obj] })
		XmlWriter(m_file,self.l_img[m_file]).varbuilder(towrite)

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