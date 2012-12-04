import sys,os
from DocumentConverter import *

#new folder where the generated pdf files will be put
newfolder="/home/aoapcproblems"

#old pdf files of problems,I just read the folders' and files' name and path
aoapcfolder="/media/competition/aoapc"

#all problems of UVA onlinejudge
uvafolder="/media/competition/uva"

#map ,contains the path and file name of each .html files in uvafolder
maplist=[]
converter=DocumentConverter()


class FileInfo:

	def __init__(self,filename,filepath):
		self.filename=filename
		self.filepath=filepath

def traverseandconvert(srcpath,dstpath,count):

		for item in os.listdir(srcpath):
			subpath=os.path.join(srcpath,item)

		newpath=os.path.join(dstpath,item)

# find a folder,create a correspond folder in new folder
# then traverse recursively

		if os.path.isdir(subpath):
			if not os.path.lexists(newpath):
				os.makedirs(newpath)
			traverseandconvert(subpath,newpath,count+1)

# find a file,search file with the same name in the larger folder
# and convert it into pdf file,then put it into the new folder

		else:
			found=False
			root1,ext1=os.path.splitext(item)
			
			for listitem in maplist:
				root2,ext2=os.path.splitext(listitem.filename)
				if root1==root2 and ext2==".html":
					found=True
					originalfullpath=os.path.join(listitem.filepath,listitem.filename)
					if not os.path.lexists(newpath):
						converter.convert(originalfullpath,newpath)
def makeupindex():
	for root,dirs,files in os.walk(uvafolder):
		for filename in files:
			maplist.append(FileInfo(filename,root))

if __name__=="__main__":
	
	makeupindex()
	traverseandconvert(aoapcfolder,newfolder,0)

