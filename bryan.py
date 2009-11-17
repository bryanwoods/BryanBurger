from helpers import *

class Bryan(pygame.sprite.Sprite):
  """This is our bryan that will move around the screen."""
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image, self.rect = load_image('bryan.png', -1)
    self.burgers = 0
    self.x_dist = 5
    self.y_dist = 5

  def move(self, key):
    """Move your self in one of the 4 directions according to key"""
    """Key is the pygame definition for either up, down, left, or right key
    we will adjust ourselves in that direction"""
    xMove = 0;
    yMove = 0;

    if (key == K_RIGHT):
      xMove = self.x_dist
    elif (key == K_LEFT):
      xMove = -self.x_dist
    elif (key == K_UP):
      yMove = -self.y_dist
    elif (key == K_DOWN):
      yMove = self.y_dist
    self.rect.move_ip(xMove,yMove);