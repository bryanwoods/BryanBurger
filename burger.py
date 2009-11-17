from helpers import *

class Burger(pygame.sprite.Sprite):
  def __init__(self, rect=None):
    pygame.sprite.Sprite.__init__(self)
    self.image, self.rect = load_image('burger.gif', -1)
    if rect != None:
      self.rect = rect