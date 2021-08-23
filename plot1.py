import numpy as np
import matplotlib.pyplot as plt



y_axis=['IDDA','VDDD','VDDA','VD_RAW','VA_RAW','VD_REG','VA_REG','GND','GNDD','GNDA','NTC0','NTC1','TESTRES']##13
f=open('output.txt')
data=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
if len(y_axis)!=len(data):
	print("label and data not same.exit")
	exit()

line=0
for item in f.readlines():
	line=line+1
	if item.strip() is not None:
		line_=item.strip().split()
		try:
			for index in range(0,13):
				data[index].append(float(line_[index+1]))
		except ValueError:
			print("on line",line)
		

f.close()
print('data size:',len(data))

fluence_unit=63.662*100/60 ##63.662Gy/min= 106.1 Rad/sec rad/s
fluence=[fluence_unit*(i-1)*15/1000 for i, element in enumerate(data[0])]

ylabel=['IDDA','VDDD','VDDA','VD_RAW','VA_RAW','VD_REG','VA_REG','','GNDD','GNDA','NTC0','NTC1','TESTRES']
title =['IDDA vs Dose','VDDD vs Dose','VDDA vs Dose','VD_RAW vs Dose','VA_RAW vs Dose','VD_REG vs Dose','VA_REG vs Dose','','GNDD vs Dose','GNDA vs Dose',
        'NTC0 vs Dose','NTC1 vs Dose','TESTRES vs Dose']

print('length:',len(fluence))
def plotGraph(Y,YLabel,Title):
	fig=plt.figure()
	plt.ylabel(YLabel)
	plt.xlabel('Dose[kRad]')
	plt.title('ABCStar chip'+Title)
	plt.scatter(fluence[:100], Y,label="un-irradiated ABCstar 28C")
	plt.legend(loc="upper right")

	return fig

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('TIDstudy.pdf')
####plot_lib=[]
for i in range(0,13):
	print(i)
	if i==7:
		continue
	if  i==2:
		plot_local=plotGraph(data[i][:100],ylabel[i],title[i])
	else:	
		plot_local=plotGraph(data[i][:100],ylabel[i],title[i])
	#plot_lib.append(plot_local)
	pp.savefig(plot_local)

pp.close()

'''
axs[0, 0].scatter(fluence, data[0])
axs[0, 0].set_ylabel('IDDA')
axs[0, 0].set_title('IDDA vs Dose')
axs[0, 0].set_ylim([ min(data[0]),max(data[0])])

axs[0, 1].scatter(fluence, data[1])
axs[0, 1].set_ylabel('VDDD')
axs[0, 1].set_title('VDDD vs Dose')
axs[0, 1].set_ylim([ min(data[1]),max(data[1])])

axs[0, 2].scatter(fluence, data[2])
axs[0, 2].set_ylabel('VDDA')
axs[0, 2].set_title('VDDA vs Dose')
axs[0, 2].set_ylim([ min(data[2]),max(data[2])])

axs[1, 0].scatter(fluence, data[3])
axs[1, 0].set_ylabel('VD_RAW')
axs[1, 0].set_title('VD_RAW vs Dose')
axs[1, 0].set_ylim([ min(data[3]),max(data[3])])

axs[1, 1].scatter(fluence, data[4])
axs[1, 1].set_ylabel('VA_RAW')
axs[1, 1].set_title('VA_RAW vs Dose')
axs[1, 1].set_ylim([ min(data[4]),max(data[4])])

axs[1, 2].scatter(fluence, data[5])
axs[1, 2].set_ylabel('VD_REG')
axs[1, 2].set_title('VD_REG vs Dose')
axs[1, 2].set_ylim([ min(data[5]),max(data[5])])

axs[2, 0].scatter(fluence, data[6])
axs[2, 0].set_ylabel('VA_REG')
axs[2, 0].set_title('VA_REG vs Dose')
axs[2, 0].set_ylim([ min(data[6]),max(data[6])])

axs[2, 1].scatter(fluence, data[8])
axs[2, 1].set_ylabel('GNDD')
axs[2, 1].set_title('GNDD vs Dose')
axs[2, 1].set_ylim([ min(data[8]),max(data[8])])

axs[2, 2].scatter(fluence, data[10])
axs[2, 2].set_ylabel('NTC0')
axs[2, 2].set_title('NTC0 vs Dose')
axs[2, 2].set_ylim([ min(data[10]),max(data[10])])


axs[3, 0].scatter(fluence, data[11])
axs[3, 0].set_ylabel('NTC1')
axs[3, 0].set_title('NTC1 vs Dose')
axs[3, 0].set_ylim([ min(data[11]),max(data[11])])

axs[3, 1].scatter(fluence, data[12])
axs[3, 1].set_ylabel('TESTRES')
axs[3, 1].set_title('TESTRES vs Dose')
axs[3, 1].set_ylim([ min(data[12]),max(data[12])])

axs[3, 2].scatter(fluence, data[9])
axs[3, 2].set_ylabel('GNDA')
axs[3, 2].set_title('GNDA vs Dose')
axs[3, 2].set_ylim([ min(data[9]),max(data[9])])

'''
'''
fig.tight_layout()
fig.subplots_adjust(top=0.88)

plt.show()
'''