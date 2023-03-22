import numpy as np
from Particle import Particle

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

        self.particle_collisions() # check for particle collisions after updating positions
    

    def wall_collisions(self):
        for particle in self.particles:
            if particle.position[0] == -self.width or particle.position[0] == self.width:
                particle.setVelocity(particle.velocity[0] * -1, particle.velocity[1])

            if particle.position[1] == -self.height or particle.position[1] == self.height:
                particle.setVelocity(particle.velocity[0], particle.velocity[1] * -1)

    def particle_collisions(self):
        for i, particle1 in enumerate(self.particles):
            for particle2 in self.particles[i+1:]:
                dist = np.linalg.norm(particle1.position - particle2.position)
                if dist <= 1* (particle1.radius + particle2.radius):
                    # calculate new velocities
                    v1, v2 = particle1.velocity, particle2.velocity
                    m1, m2 = particle1.mass, particle2.mass
                    x1, x2 = particle1.position, particle2.position
                    v1_new = v1 - 2 * m2 / (m1 + m2) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2)**2 * (x1 - x2)
                    v2_new = v2 - 2 * m1 / (m1 + m2) * np.dot(v2 - v1, x2 - x1) / np.linalg.norm(x2 - x1)**2 * (x2 - x1)
                    particle1.setVelocity(v1_new[0], v1_new[1])
                    particle2.setVelocity(v2_new[0], v2_new[1])