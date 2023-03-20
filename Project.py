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

    def setVelocity(self, x, y):
        self.velocity[0] = x
        self.velocity[1] = y
        pass

    def setPosition(self, x, y):
        self.position[0] = x
        self.position[1] = y
        pass
        

class Box:
    def __init__(
        self,
        time_increment = 1e-5,
        number_of_particles = 10,
        width = 5,
        height = 5
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
        for particle in self.particles:

            new_x = particle.position[0] + (self.time_increment * particle.velocity[0])
            new_y = particle.position[1] + (self.time_increment * particle.velocity[1])
            
            if new_x <= -self.width or new_x >= self.width:
                particle.setVelocity(particle.velocity[0] * -1, particle.velocity[1])

            if new_y <= -self.height or new_y >= self.height:
                particle.setVelocity(particle.velocity[0], particle.velocity[1] * -1)

            particle.setPosition(new_x, new_y)

    def wall_collisions(self):
        for particle in self.particles:
            if particle.position[0] == -self.width or particle.position[0] == self.width:
                particle.setVelocity(particle.velocity[0] * -1, particle.velocity[1])

            if particle.position[1] == -self.height or particle.position[1] == self.height:
                particle.setVelocity(particle.velocity[0], particle.velocity[1] * -1)


initial_colour = "red"
box = Box(1e-3, 1000, 2, 2)
box.random_pos()


fig, axis = plt.subplots()

x=[]
y=[]
for i in range(box.number_of_particles):
    x.append(box.particles[i].position[0])
    y.append(box.particles[i].position[1])

scatter = axis.scatter(x, y,s=20,c='indigo',marker= '.')

plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2,2)
plt.xlim(-2,2)

def plot(frame):
    box.update_pos()
    positions=[]
    for i in range (box.number_of_particles):
        positions.append(box.particles[i].position)
    scatter.set_offsets(positions)


animation = FuncAnimation(fig, func=plot, interval=10)

plt.show()




