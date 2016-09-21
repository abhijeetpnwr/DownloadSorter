# Motive of project is to write a script  to automatically sort my downloads as per my coventions

import os

allFiles = os.listdir("/home/abhijeet/Downloads")

imageformats=["jpg","bmp","png","gif"]
textformats=["txt","fasta","out"]
pdfs=["pdf"]
exes=["exe","tar","bz2","bz","a","bat","lib","zip","dll"]
officedocs=["xlsx","xls","doc","docx","ppt"]
Web=["js","css","html","jsp","xml","c","java","py","pl","CPP","csv","json","h","H","jar","PL","pm"]
videos=["mpeg","3gp","mp4","avi","flv","mov","srt"]
songs=["mp3","wav","mpa"]

folderMap={"Image":imageformats,"TextFile":textformats,"PDF":pdfs,"Software_Compressed":exes,"Documents":officedocs,"Programming":Web,"Video":videos,"songs":songs}



foldernamemap={"imageformats":"Photos","textformats":"Textfiles","pdfs":"Ebooks_pdfs","Docs":"docs"}


for file in allFiles:
	namelist = file.split(".")
	
	if len(namelist)>1:
		extension = namelist[len(namelist)-1]

		for keys in folderMap:

			if extension in folderMap[keys]:
				print "",file," is :",keys,"\n"
		
	else:
		print "Not defined :",file,"\n"