from scipy.interpolate import interp1d
import math
import numpy as np
import matplotlib.pyplot as plt

#Base function
def y(x):
    return x**(1/2)+math.cos(x)

#Base function analytic derivative
def deriv_y(x):
    return (1/2)*x**(-1/2)-math.sin(x)

#Linear and cubic interpolant functions
linear = interp1d(x, y)
cubic = interp1d(x, y, kind='cubic')

#Calculates y values for y(x) and deriv_y(x) over 0 to 4pi with spacing of 0.01
xAxisFine = np.arange(0, 4*math.pi, 0.01)
yAxis = []
deriv_yAxis = []
for value in xAxisFine:
    yAxis.append(y(value))
    deriv_yAxis.append(deriv_y(value))

#Calculates y values for linear and cubic interpolants of y(x) and deriv_y(x) over 0 to 4pi with spacing of 0.8
xAxisSparse = np.arange(0, 4*math.pi, 0.8)
linearInterpolant_yAxis = []
cubicInterpolant_yAxis = []
linearInterpolantDeriv_yAxis = []
cubicInterpolantDeriv_yAxis = []
for value in xAxisSparse:
    linearInterpolant_yAxis.append(linear(value, y(value)))
    cubicInterpolant_yAxis.append(cubic(value, y(value)))
    linearInterpolantDeriv_yAxis.append(linear(value, deriv_y(value)))
    cubicInterpolantDeriv_yAxis.append(cubic(value, deriv_y(value)))

#converts all lists to arrays for plotting
yAxis = np.array(yAxis)
deriv_yAxis = np.array(deriv_yAxis)
linearInterpolant_yAxis = np.array(linearInterpolant_yAxis)
cubicInterpolant_yAxis = np.array(cubicInterpolant_yAxis)
linearInterpolantDeriv_yAxis = np.array(linearInterpolantDeriv_yAxis)
cubicInterpolantDeriv_yAxis = np.array(cubicInterpolantDeriv_yAxis)

#plots y(x), deriv_y(x), and their linear and cubic interpolants
plt.plot(xAxisFine, yAxis, color='navy')
plt.plot(xAxisFine, deriv_yAxis, color='navy', linestyle='dashed')
plt.plot(xAxisSparse, linearInterpolant_yAxis, color='red')
plt.plot(xAxisSparse, linearInterpolantDeriv_yAxis, color='red', linestyle='dashed')
plt.plot(xAxisSparse, cubicInterpolant_yAxis, color='gold')
plt.plot(xAxisSparse, cubicInterpolantDeriv_yAxis, color='gold', linestyle='dashed')
plt.title('Interpolation Examples')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(['True Function','True Derivative','Linear Interpolant','Linear Interpolant Derivative','Cubic Interpolant','Cubic Interpolant Derivative'])
plt.savefig('Interpolation_Examples.png')
