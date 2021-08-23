import numpy as np
import matplotlib.pyplot as plt


f=open('IDDD.txt')
current=[]
initial_current=32.400
line=0
for item in f.readlines():
	line=line+1
	if item.strip() is not None:
		try:
			current.append(float(item)/32.400)
		except ValueError:
			print("on line",line)
		

f.close()

fluence_unit=63.662*100/60 ##63.662Gy/min= 106.1 Rad/sec rad/s
fluence=[fluence_unit*(i-1)*15/1000 for i, element in enumerate(current)]

f = plt.figure()
plt.ylabel('Digital Current')
plt.xlabel('Dose[kRad]')
plt.title('ABCStar chip current vs Dose')
plt.scatter(fluence, current,label="un-irradiated ABCstar 28C")
plt.legend(loc="upper right")
plt.show()
f.savefig("TID.pdf", bbox_inches='tight')
# 