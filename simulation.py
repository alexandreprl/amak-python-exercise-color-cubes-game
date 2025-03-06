from amak import AMAKPygame

from system import ColorCubesGameAMAS, ColorCubesGameEnvironment

environment = ColorCubesGameEnvironment(20, 10)
mas = ColorCubesGameAMAS(environment, 10)

if __name__ == "__main__":
    AMAKPygame(mas, environment, 640,480, 120)
