from turtle import width
from xml.sax.handler import DTDHandler
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Particle:
    def __init__( #this function alongside _str_ sets up our particle class
            self,
            id=0,
            position=np.array([0, 0], dtype=float),
            velocity=np.array([0, 0], dtype=float),
            radius=1E-2,
            mass=1.0,
            colour="red",
            gradient = 1
    ):
            self.id = id
            self.position = np.array(position, dtype=float)
            self.velocity = np.array(velocity, dtype=float)
            self.radius = radius
            self.mass = mass
            self.colour = colour
            self.gradient = gradient
        

class Box:
    def __init__(
        self,
        time_increment = 1e-5,
        number_of_particles = 10,
        width = 10,
        height = 10
    ):
        self.time_increment = time_increment
        self.number_of_particles = number_of_particles
        self.width = width
        self.height = height
        self.particles = [Particle(i) for i in range(self.number_of_particles)]

    def random_pos(self):
        for i in range(self.number_of_particles):
            self.particles[i].position[0] = np.random.uniform(-self.width / 2, self.width / 2)
            self.particles[i].position[1] = np.random.uniform(-self.height / 2, self.height / 2)
            self.particles[i].velocity = 20 * np.random.uniform(-1, 1, 2)

    def update_pos(self):
        for i in range (self.number_of_particles):
            self.particles[i].position[0] += self.time_increment * self.particles[i].velocity[0]
            self.particles[i].position[1] += self.time_increment * self.particles[i].velocity[1]

    #def wall_collisions(self):
    #    if 



initial_colour = "blue"
box = Box(1e-3, 10, 10, 10)
box.random_pos()


fig, axis = plt.subplots()

x=[]
y=[]
for i in range(box.number_of_particles):
    x.append(box.particles[i].position[0])
    y.append(box.particles[i].position[1])

scatter = axis.scatter(x, y)


#plt.scatter(box.particles[i].position[0], box.particles[i].position[1], initial_colour, alpha=box.particles[i].gradient)
plt.xlabel('time')
plt.ylabel('position')

def plot(frame):
    box.update_pos()
    positions=[]
    for i in range (box.number_of_particles):
        positions.append(box.particles[i].position)
    scatter.set_offsets(positions)


animation = FuncAnimation(fig, func=plot, interval=100)

# for i in range(500):
#     for particle in box.particles:
#         particle.gradient = particle.gradient - (particle.gradient * 0.05)
#         box.update_pos()
#         box.plot("blue")

plt.show()




