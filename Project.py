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
            colour="blue"
    ):
            self.id = id
            self.position = np.array(position, dtype=float)
            self.velocity = np.array(velocity, dtype=float)
            self.radius = radius
            self.mass = mass
            self.colour = colour
        

class Box:
    def __init__(
        self,
        time_increment = 1E-5,
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
        for i in range (self.number_of_particles):
            self.particles[i].position = np.random.uniform(self.width, self.height, 2)
            self.particles[i].velocity = 20 * np.random.uniform(-1, 1, 2)

    def update_pos(self):
        for i in range (self.number_of_particles):
            self.particles[i].position += self.time_increment * self.particles[i].velocity

    def plot(self):
        for i in range (self.number_of_particles):
            plt.scatter(box.particles[i].position[0], box.particles[i].position[1])#, color=box.particles[i].colour)
            plt.xlabel('time')
            plt.ylabel('position')

       
box = Box(1, 1, 5, 10)
box.random_pos()
box.plot()



box.update_pos()
box.plot()

plt.show()





