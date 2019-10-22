import time
import math
import random
from rolepy.globals import Ordinal


class NpcAi:

    def __init__(self, center):
        self.last_movement = 0
        self.next_movement = 0
        self.max_time_between_movements = 10.
        self.min_time_between_movements = 1.
        self.max_distance_to_center = 5
        self.center = center

    def iterate(self, entity):
        now = time.time()
        if now > self.next_movement:
            remoteness = entity.position - self.center
            if remoteness.norm_inf() > self.max_distance_to_center:
                angle = remoteness.angle()
                if math.pi / 4 >= angle > -math.pi / 4:
                    direction = Ordinal.WEST
                elif 3 * math.pi / 4 >= angle > math.pi / 4:
                    direction = Ordinal.NORTH
                elif -math.pi / 4 >= angle > -3 * math.pi / 4:
                    direction = Ordinal.SOUTH
                else:
                    direction = Ordinal.EAST
            else:
                direction = random.choice(list(Ordinal))
            distance = random.randint(1, 5)
            entity.move(direction, distance).start()
            self.last_movement = now
            self.next_movement = random.random() * (self.max_time_between_movements - self.min_time_between_movements) + self.min_time_between_movements + self.last_movement
        entity.thinking = True
