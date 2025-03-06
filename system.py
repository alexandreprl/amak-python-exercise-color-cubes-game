from random import random

from amak import MAS

from entities import Cube, RobotAgent


def random_color():
    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255)]
    return colors[int(random() * len(colors))]


class ColorCubesGameEnvironment:
    def __init__(self, cubes_count, rooms_count):
        self.rooms = []
        self.cubes = []
        self.cubes_count = cubes_count

        for i in range(cubes_count):
            self.cubes.append(Cube(random_color()))

        for i in range(rooms_count):
            self.rooms.append({
                "cubes": []
            })

        for cube in self.cubes:
            room = self.rooms[int(random() * len(self.rooms))]
            room["cubes"].append(cube)

    def cycle(self):
        pass

    def pickup_any_cube(self, room):
        if len(room["cubes"]) > 0:
            return room["cubes"].pop(0)
        return None

    def drop_cube(self, room, cube):
        room["cubes"].append(cube)

    def render(self, display_surface):
        display_surface.fill((255, 255, 255))
        x = 0
        for room in self.rooms:
            y = 0
            display_surface.fill((0, 0, 0), (x * 10, 0, 10, self.cubes_count * 10))
            for cube in room["cubes"]:
                display_surface.fill(cube.color, (x * 10 + 1, y * 10, 8, 10))
                y += 1
            x += 2


class ColorCubesGameAMAS(MAS):
    def __init__(self, environment, robots_count):
        super().__init__(environment)
        for i in range(robots_count):
            RobotAgent(self, environment.rooms[int(random() * len(environment.rooms))])


    def is_ready_to_stop(self):
        return False
