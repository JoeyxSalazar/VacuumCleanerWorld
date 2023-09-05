import random

from environment import VacuumCleanerWorld
from agent import ReflexAgent


def main():
  locs = ['A', 'B']

  for i in range(0,10):
    new_world = VacuumCleanerWorld(locs)
    agent = ReflexAgent(new_world)
    while not all(value == 0 for value in new_world.dirt_locations.values()):
      action = agent.get_action()
      new_world.take_action(action)
    print('All Areas Cleaned!')


if __name__ == "__main__":
  main()