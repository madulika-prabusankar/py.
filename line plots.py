import matplotlib.pyplot as plt
import numpy as np
#plot1
x=np.array([4,7,3,6,9,8,2,1,5])
y=np.array([4,7,3,6,9,8,2,1,5])
plt.subplot(1,3,1)
plt.plot(x,y,marker='o',ls=':',c='y')
plt.title('sales')
#plot2
x=np.array([8,6,3,4,2,5,7,9,8])
y=np.array([4,5,3,6,9,8,4,1,5])
plt.subplot(1,3,2)
plt.plot(x,y,marker='h',ls='--',ms=12,mec='k',mfc='y',lw=10,c='m')
plt.title('employee')
#plot3
x1=np.array([2,8,7,6,5,2,3,4,1])
y1=np.array([19,3,4,5,16,2,7,13,6])
x2=np.array([4,5,3,6,9,8,4,1,5])
y2=np.array([2,4,9,3,12,5,7,8,10])
plt.subplot(1,3,3)
plt.plot(x1,y1,marker='p',ls='dotted',c='b')
plt.plot(x2,y2,marker='D',ls='-.',c='r')
plt.title('company')
plt.suptitle('multi line subplots')
plt.show()





