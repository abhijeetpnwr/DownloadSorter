# Motive of project is to write a script  to automatically sort my downloads as per my coventions

import os

allFiles = os.listdir("/home/abhijeet/Downloads")

imageformats=["jpg","bmp","png","gif","svg"]
textformats=["txt","fasta","out","txt~","vcf"]
pdfs=["pdf","epub"]
exes=["exe","tar","bz2","bz","a","bat","lib","zip","dll","deb","so","run"]
officedocs=["xlsx","xls","doc","docx","ppt"]
Web=["js","css","html","jsp","xml","c","java","sh","py","pl","CPP","csv","json","h","H","jar","PL","pm"]
videos=["mpeg","3gp","mp4","avi","flv","mov","srt","mkv"]
songs=["mp3","wav","mpa"]

folderMap={"Image":imageformats,"TextFile":textformats,"PDF":pdfs,"Software_Compressed":exes,"Documents":officedocs,"Programming":Web,"Video":videos,"songs":songs}



foldernamemap={"imageformats":"Photos","textformats":"Textfiles","pdfs":"Ebooks_pdfs","Docs":"docs"}


for file in allFiles:


	namelist = file.split(".")


	
	if len(namelist)>1:
		extension = namelist[len(namelist)-1]

		extensionfound = False

		for keys in folderMap:

			if extension in folderMap[keys]:
				print "",file," is :",keys,"\n"
				extensionfound=True

		if extensionfound==False:
			print "No file type found for ",file
		
	else:
		print "Not defined :",file,"\n"