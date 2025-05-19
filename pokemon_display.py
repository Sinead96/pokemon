class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry 
    self.name = name 
    self.types = types
    self.description = description 
    self.is_caught = is_caught

  def speak (self): 
    print(self.name + ',' + self.name)

  def display_details (self):
    print (f'Entry Name: {self.entry}')
    print (f'Name: {self.name}')
    print (f'Type: {self.types}')
    print (f'Description: {self.description}')
    if self.is_caught == True: 
      print (f'{self.name} has already been caught!')
    elif self.is_caught == False: 
      print (f'{self.name} has not been caught yet!')

clefairy = Pokemon (35, 'Clefairy', 'Fairy', 'On nights with a full moon, Clefairy gather from all over and dance. Bathing in moonlight makes them float.', True)

clefairy.display_details()

clefairy.speak()

ninetales = Pokemon (38, 'Ninetales', 'Fire', 'Some legends claim that each of its nine tails has its own unique type of special mystical power.', False)

ninetales.display_details()

ninetales.speak()

ditto = Pokemon (132, 'Ditto', 'Normal', 'Its transformation ability is perfect. However, if made to laugh, it can’t maintain its disguise.', False)

ditto.display_details()

ditto.speak()
