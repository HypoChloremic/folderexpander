import os

def file_expander(parent, n=3, delimiter="/"):
	for i in range(n):
		if i == n-1:
			files = []
			for parent_path in parent:
				files.extend([f"{parent_path}{delimiter}{k}" for k in os.listdir(parent_path) if not os.path.isdir(f"{parent_path}{delimiter}{k}")])

			return files
		else: 
			parent = expand(parent, delimiter)
			

def expand(f, delimiter="/"):
	l = []
	for each in f:
		files_in_d =  [ k for k in os.listdir(each) if os.path.isdir(f"{each}{delimiter}{k}")]
		
		for i in files_in_d:
			l.append(f"{each}{delimiter}{i}")	
	return l

	


k = file_expander([os.path.abspath(r"C:\Users\Ali Rassolie\OneDrive\prwork\python\packages")], delimiter="\\")
print(k)
