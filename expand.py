import os


# The file expander takes a parent direcotry and a number,
# indicating the number of folders to be opened, before returning 
# the contents of that folder. In this case, the default delimiter
# is adapted to the Ubuntu environment, and not the Windows one,
# where paths are delimited with a '\'. 

def file_expander(parent, n=3, delimiter="/"):
	for i in range(n):
		if i == n-1:
			files = []
			for parent_path in parent:
				files.extend([f"{parent_path}{delimiter}{k}" for k in os.listdir(parent_path) if not os.path.isdir(f"{parent_path}{delimiter}{k}")])

			return files
		else: 
			parent = expand(parent, delimiter)
			
# The expand method allows permits a recursive function above, where
# we get to parse a directory to be opened and then return the folders
# of that directory, before moving on with the loop.
# this is why it is important that the parameter directory is of type list. 
def expand(f, delimiter="/"):
	l = []
	for each in f:
		files_in_d =  [ k for k in os.listdir(each) if os.path.isdir(f"{each}{delimiter}{k}")]
		
		for i in files_in_d:
			l.append(f"{each}{delimiter}{i}")	
	return l

if __name__ == '__main__':
	# Demonstrating the use of the method. 
	# note 
	#  
	k = file_expander([r"C:\Users\Ali Rassolie\OneDrive\prwork\python\packages"], delimiter="\\")
	print('\n'.join(k))
