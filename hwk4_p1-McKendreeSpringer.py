import numpy as np
import matplotlib.pyplot as plt
import math

#electric potential function
def calculateElectricPotential(charge, distance):
    return charge/(4*math.pi*(8.85418782*10**-12)*distance)

#charges defined
charge1 = {'position':(5,0), 'charge':1}
charge2 = {'position':(-5,0), 'charge':1}

#electric potential calculated for every cm x cm point on the m x m grid
electricPotentials = []
axis = np.arange(101) -  50
for i in range(len(axis)):
    for j in range(len(axis)):
        
        #electric potential calculated for every point relative to charge1
        distance1 = math.sqrt((axis[j]-charge1['position'][0])**2+(axis[i]-charge1['position'][1])**2)
        if distance1 != 0:
            a = calculateElectricPotential(charge1['charge'], distance1)
        else:
            a = 'infinity'
            
        #electric potential calculated for every point relative to charge2
        distance2 = math.sqrt((axis[j]-charge2['position'][0])**2+(axis[i]-charge2['position'][1])**2)
        if distance2 != 0:
            b = calculateElectricPotential(charge2['charge'], distance2)
        else:
            b = 'infinity'

        #combines electric potentials from both charges and puts them in list
        if a == 'infinity' or b == 'infinity':
            electricPotentials.append(9999999999)
        else:
            electricPotentials.append(a+b)

#coverts electric potential list to array and changes it to 2D
potentialArr1D = np.array(electricPotentials)
potentialArr2D = potentialArr1D.reshape(101,101)

#plots electric potential on a contour plot
plt.contour(axis, axis, potentialArr2D, levels=30)
plt.title('Electric Potential')
plt.xlabel('X-Axis (cm)')
plt.ylabel('Y-Axis (cm)')
plt.show()
plt.savefig('Electric_Potential.png')

#computes x component of E-field
xEfield = []
for i in range(len(potentialArr2D)-2):
    derivRow = []
    for j in range(len(potentialArr2D[i])-2):
        derivRow.append((potentialArr2D[i+1][(j+1)+1]-potentialArr2D[i+1][(j+1)-1])/2)
    xEfield.append(derivRow)

#computes y component of E-field
yEfield = []
for i in range(len(potentialArr2D)-2):
    derivRow = []
    for j in range(len(potentialArr2D[i])-2):
        derivRow.append((potentialArr2D[(i+1)+1][j+1]-potentialArr2D[(i+1)-1][j+1])/2)
    yEfield.append(derivRow)

#converts E-field value lists to arrays from plotting
xEfield = np.array(xEfield)
yEfield = np.array(yEfield)

#prints the E-field values at (0,0) and (5,7)
print('E-Field at (0,0): (', xEfield[0][0], 'i ,', yEfield[0][0], 'j )')
print('E-Field at (5,7): (', xEfield[5][7], 'i ,', yEfield[5][7], 'j )')

#plots the E-field direction on a quiver plot
plt.clf()
magEfield = (xEfield**2+yEfield**2)**(1/2)
plt.quiver(axis[0:-2], axis[0:-2], -xEfield/magEfield, -yEfield/magEfield)
plt.title('E-Field')
plt.xlabel('X-Axis (cm)')
plt.ylabel('Y-Axis (cm)')
plt.show()
plt.savefig('E-Field_Direction.png')

#plots the E-field direction and magnitude on a quiver plot
plt.clf()
magEfield = (xEfield**2+yEfield**2)**(1/2)
plt.quiver(axis[0:-2], axis[0:-2], -xEfield, -yEfield)
plt.title('E-Field')
plt.xlabel('X-Axis (cm)')
plt.ylabel('Y-Axis (cm)')
plt.show()
plt.savefig('E-Field_DirectionAndMagnitude.png')
'''
#attempts to plot the E-field direction and magnitude (as width) on a quiver plot
plt.clf()
magEfield = (xEfield**2+yEfield**2)**(1/2)
plt.quiver(axis[0:-2], axis[0:-2], -xEfield/magEfield, -yEfield/magEfield, width=(magEfield/350000000000))
plt.title('E-Field')
plt.xlabel('X-Axis (cm)')
plt.ylabel('Y-Axis (cm)')
plt.show()
plt.savefig('E-Field_Direction/Magnitude-width.png')'''
