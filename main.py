import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Box import Box


box = Box(1e-3, 10, 2, 2)
box.random_pos()


fig, axis = plt.subplots()

x=[]
y=[]
for i in range(box.number_of_particles):
    x.append(box.particles[i].position[0])
    y.append(box.particles[i].position[1])

scatter = axis.scatter(x, y,s=20,c='pink') #marker= '$Slay George$')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-box.width,box.width)
plt.ylim(-box.height,box.height)

def plot(frame):
    box.update_pos()
    positions=[]
    for i in range (box.number_of_particles):
        positions.append(box.particles[i].position)
    scatter.set_offsets(positions)


animation = FuncAnimation(fig, func=plot, interval=10, frames=1000)

plt.show()




