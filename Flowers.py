import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

ppr= 3.6 # petals per 1 revolution
nr = 30  # radius resolution
pr = 30  # petal resolution
pn = 40  # total number of petals
pf = 2   # How much the ends of the petals tilt up or down
ps = 5/4 # Separation between petals
ol = [.2, 1.02] # How open is it? [inner outer]

pt = (1/ppr) * np.pi * 2
theta = np.linspace(0, pn*pt,pn*pr+1)
R,THETA = np.meshgrid(np.linspace(0,1,nr), theta, indexing='ij')
x = 1-((ps*((1-np.mod(ppr*THETA, 2*np.pi)/np.pi)**2)-1/4)**2)/2
phi = (np.pi/2)*(np.linspace(ol[0],ol[1],pn*pr+1))**2
y = pf*(R**2)*((1.28*R-1)**2)*np.sin(phi)
R2 = (x*(R*np.sin(phi))) + (y*np.cos(phi))

X = R2*np.sin(THETA)
Y = R2*np.cos(THETA)
Z = x*((R*np.cos(phi))-(y*np.sin(phi)))
C = np.hypot(np.hypot(X,Y), Z)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

vals = np.zeros((256, 3))
vals[:, 0] = np.linspace(0,1,256)
newcmp = colors.ListedColormap(vals)

surf = ax.plot_surface(X, Y, Z, cmap = newcmp, rstride=1,
                        cstride=1, linewidth=0, antialiased=False)
ax.axis('equal')
ax.axis('off')
plt.show()

# Using a colormap from matplotlib reference
from matplotlib import cm
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
my_col = cm.hot_r(C)
surf = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors = my_col,
        linewidth=0, antialiased=False)
ax2.axis('equal')
ax2.axis('off')
plt.show()