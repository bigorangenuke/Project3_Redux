import numpy as np
import os

def listdumps():
	#List all files in the directory that do not contain an extension (should only be the dump files)
	f = [f for f in os.listdir('.') if os.path.isfile(f)]
	return [g for g in f if not '.' in g]

class dumpreader():
	def __init__(self,filename=None):
		if not filename:
			filename = 'config1_49_2groups_dump'


		self.filename = filename

		f = open(filename,'r')
		lines = f.readlines()
		f.close()
		#phi holds a list of numpy arrays
		self.phi = []
		tmp = None
		firstflag = True
		for i,line in enumerate(lines):
			line = line.strip()
			if i<=6:
				l = line.split(':')[-1]
				if i==0:
					self.filename = l
				elif i ==1:
					self.groups = int(l)
				elif i==2:
					self.m = int(l)
				elif i==3:
					self.n = int(l)
				elif i ==4:
					self.w = float(l)
				elif i ==5:
					self.h = float(l)
				elif i==6:
					self.k = float(l)
			else:
				if line[0]=="#":
					if not firstflag:
						self.phi.append(tmp)
					firstflag = False
					tmp = np.empty((self.m,self.n))
				else:
					l = line.split(',')
					ii = int(l[0])
					jj = int(l[1])
					tmp[ii,jj] = float(l[2])


if __name__=='__main__':
	d  = dumpreader()

	print(listdumps())


	print(d.phi[0])


	import matplotlib.pyplot as plt
	plt.imshow(d.phi[0])
	plt.show()