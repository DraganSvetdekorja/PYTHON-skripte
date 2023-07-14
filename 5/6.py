import os
import tinify
from __future__ import print_function

tinify.key =   # Fill your developer key here

for files in os.listdir("C:/Users/LENOVO/Pictures/SVETDEKORJA"):
    print(files)
	
print('next function')
print('\n')


#list only files with extension pdf and exe in directory and subdirectory	
rootdir = 'C:/Users/LENOVO/Pictures/SVETDEKORJA/Katalogi slike'
#C:\Users\LENOVO\Pictures\SVETDEKORJA\Katalogi slike
ext = ('.pdf','.jpg')	
basewidth = 1000

#files = [f for f in os.listdir(.) if os.path.isfile(f) and f.endswith(exts)]
#for subdir, dirs, files in os.walk(rootdir):
for subdir, dirs, files in os.walk(rootdir) if files.endswith(ext):
#files = for subdir, dirs in os.walk(rootdir):
#for files in os.listdir("C:/Users/LENOVO/Pictures/SVETDEKORJA"):
	for file in files:
		if file.endswith(ext):
			print(os.path.join(subdir, file))
			print(Optimizing %s % file)
			source = tinify.from_file(file)
			resized = source.resize(method=scale, width=basewidth)
			resized.to_file(optimized%s % f)
		else:
			continue			
	