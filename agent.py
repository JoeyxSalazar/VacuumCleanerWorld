import random

class ReflexAgent:
  """
  A class representing a simple reflex agent for the vacuum cleaner world.

  Attributes:
    world: The world that the agent is operating in.
  """

  def __init__(self, world):
    self.world = world
    self.actions = {}

  def percept(self):
      return (self.world.agent_location, self.world.is_dirty())


  def get_action(self):
    """
    Get the action that the agent should take.

    Returns:
      The action that the agent should take.
    """
    p = self.percept()
    if p == ('A', 0):
      #Location A is Clean
      return 'right'
      pass
    elif p == ('B', 0):
      #Location B is Clean
      return 'left'
      pass
    else:
      return 'suck'

  
    