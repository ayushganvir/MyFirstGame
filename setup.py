from nbody.parts import Particle
import random
from constants import WIDTH, HEIGHT
from core.physics import Point, Transform


class Universe:

    def __init__(self, number_of_stars, number_of_particles):
        self.stars = []
        for n in range(number_of_stars):
            r_random = random.randint(1, 100)
            g_random = random.randint(1, 100)
            b_random = random.randint(1, 100)
            x = random.randint(-WIDTH / 2, WIDTH / 2)
            y = random.randint(-HEIGHT / 2, HEIGHT / 2)
            location = Point(Transform.x(x), Transform.y(y))
            star_color = (r_random, g_random, b_random)
            size = random.randint(1, 5)
            star = Particle("Star", star_color, size, 0, location, 0)
            self.stars.append(star)

        self.sun = Particle("Sun", (255, 0, 0), 50, 10000000, Point(Transform.x(0), Transform.y(0)), Point(1, 0))
        self.particles = [self.sun]

        for n in range(number_of_particles):
            x = random.randint(-WIDTH / 2, WIDTH / 2)
            y = random.randint(-HEIGHT / 2, HEIGHT / 2)
            location = Point(Transform.x(x), Transform.y(y))
            r_random = random.randint(1, 255)
            g_random = random.randint(1, 255)
            b_random = random.randint(1, 255)
            color = (r_random, g_random, b_random)
            mass = random.uniform(4000, 15000)
            size = int(mass / 500)
            vx = random.uniform(50, 150)
            vy = random.uniform(50, 150)
            velocity = Point(vx, vy)
            particle = Particle("A-%s" % n, color, size, mass, location, velocity)
            self.particles.append(particle)
