from random import choice, random

from amak import RenderableAgent, RenderableEntity, Agent


def grid_to_display_position(on_grid_position):
    return 5 + on_grid_position[0] * 10, 5 + on_grid_position[1] * 10


class Cube:
    def __init__(self, color):
        self.color = color

class RobotAgent(Agent):
    def __init__(self, mas, current_room):
        super().__init__(mas)
        self.current_room = current_room
        self.held_cube = None

    def on_perceive(self):
        # Exercise: Implement the Robot perception
        pass
    def on_decide_and_act(self):
        if self.held_cube is None:
            self.held_cube = self.amas.environment.pickup_any_cube(self.current_room)
            self.move_randomly()
        else:
            self.amas.environment.drop_cube(self.current_room, self.held_cube)
            self.held_cube = None
            self.move_randomly()

    def move_randomly(self):
        self.current_room = choice(self.amas.environment.rooms)