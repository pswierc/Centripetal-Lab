import math
import numpy as np
import matplotlib.pyplot as plt

m_hooks = .2083
unc_m_hooks = .0001
x = np.array([.206, .187, .164, .151])
y = np.array([1.4248**2, 1.365**2, 1.2524**2, 1.2272**2])
dy = np.array([.0045, .0032, .0097, .0042])

b,m=np.polynomial.polynomial.polyfit(x, y, 1 ,w=dy)

fit = b+m*x    

f_centripital = (1 / m) * m_hooks * (math.pi ** 2) * 4 

                                                                                #Calculate the error in slope and intercept 
#def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D
 
D=Delta(x, dy)
 
dm = np.sqrt(1/D*sum(1/dy**2)) #error in slope
db = np.sqrt(1/D*sum(x**2/dy**2)) #error in intercept

#Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x,y,dy):
    N = sum(((y-b-m*x)/dy)**2)
    return N
                      
N = LLSFD2(x,y,dy)

unc_f_centripital = f_centripital * math.sqrt(((unc_m_hooks / m_hooks) ** 2) + ((dm / m) ** 2))

print(f_centripital)
print(unc_f_centripital)


#plot

plt.figure(figsize=(15,10))
 
plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')
 
 
#create labels 
plt.xlabel('Radius (m)')
plt.ylabel('Period Squared (sec)')
plt.title('Period Squared over Radius')
 
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
 
plt.annotate('Slope (sec^2 / m) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')
 
plt.annotate('Error in Slope (sec^2 / m) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')

plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()