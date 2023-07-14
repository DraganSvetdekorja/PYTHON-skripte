import os
for files in os.listdir("C:/Users/LENOVO/Pictures/SVETDEKORJA"):
    print(files)
	
print('next function')
print('\n')


#list only files with extension pdf and exe in directory and subdirectory	
rootdir = 'C:/Users/LENOVO/Pictures/SVETDEKORJA'
ext = ('.pdf','.jpg')	
for subdir, dirs, files in os.walk(rootdir):
#files = for subdir, dirs in os.walk(rootdir):
#for files in os.listdir("C:/Users/LENOVO/Pictures/SVETDEKORJA"):
	for file in files:
		if file.endswith(ext):
			print(os.path.join(subdir, file))
		else:
			continue			
	