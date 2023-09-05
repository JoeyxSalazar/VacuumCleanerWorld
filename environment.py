import random

class VacuumCleanerWorld:
  """
  A class representing the vacuum cleaner world.

  Attributes:
    dirt_locations: A list of the locations of the dirt in the world.
    agent_location: The location of the agent in the world.
  """

  def __init__(self, locations):
    self.dirt_list = locations
    self.dirt_locations = {}
    #Randomly assign whether or not the locations are clean or dirty
    print('\n\n\n\n')
    #print("O is clean and 1 is dirty")
    for loc in locations:
      #0 is clean and 1 is dirty
      rand_val = random.randint(0,1)
      self.dirt_locations[loc] = rand_val
      if rand_val == 0:
        print(loc, "is clean")
      else:
        print(loc, "is dirty")

    
    age_num = random.randint(0, len(self.dirt_locations)-1)
    #print("Age num", age_num)
    self.agent_location = locations[age_num]
    print('Agent is at location: ', self.agent_location)
    self.agent_location_pos = age_num
    self.performance_measure = 0
    self.actions_taken = 0
    



  def print_locations(self):
    for key, value in self.dirt_locations.items():
      print(str(key) + ':' + ' ' + str(value))


  def is_dirty(self):
    return self.dirt_locations[self.agent_location]
  
  def track_performance_measure(self, action):
    if action == 'left' or action == 'right':
      self.performance_measure -= 1
    elif action == 'suck':
      self.performance_measure += 3
    self.actions_taken += 1
    print('Current Performance Measure: ', self.performance_measure / self.actions_taken )

  def move_agent(self, action):
    if action == 'left':
      self.agent_location_pos -= 1
    else:
      self.agent_location_pos += 1

    self.agent_location = self.dirt_list[self.agent_location_pos]
    print("Agent Moved to position ", self.agent_location)
    self.track_performance_measure(action) 

  def clean_location(self):
    #0 is denoted for locations that are clean
    self.dirt_locations[self.agent_location] = 0
    print("Agent Cleaned")
    self.track_performance_measure("suck")

  def take_action(self, action):
    if action == 'left' or action == 'right':
      self.move_agent(action)
    else:
      self.clean_location()

