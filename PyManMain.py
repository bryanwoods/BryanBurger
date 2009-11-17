from snake import *
from pellet import *

class PyManMain:
  """The Main PyMan Class - This class handles the main
  initialization and creating of the Game."""

  def __init__(self, width=640, height=480):
    """Initialize"""
    """Initialize PyGame"""
    pygame.init()
    """Set the window Size"""
    self.width = width
    self.height = height
    """Create the Screen"""
    self.screen = pygame.display.set_mode((self.width, self.height))

  def MainLoop(self):
    """This is the Main Loop of the Game"""
    """Load All of our Sprites"""
    self.LoadSprites();

    """Tell pygame to keep sending up keystrokes when
    they are held down"""
    pygame.key.set_repeat(500, 30)

    """Create the background"""
    self.background = pygame.Surface(self.screen.get_size())
    self.background = self.background.convert()
    self.background.fill((0, 0, 0))

    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == KEYDOWN:
          if ((event.key == K_RIGHT)
          or (event.key == K_LEFT)
          or (event.key == K_UP)
          or (event.key == K_DOWN)):
            self.snake.move(event.key)

      """Check for collision"""
      lstCols = pygame.sprite.spritecollide(self.snake
                                           , self.pellet_sprites
                                           , True)
      """Update the amount of pellets eaten"""
      self.snake.pellets = self.snake.pellets + len(lstCols)

      """Do the drawing"""
      self.screen.blit(self.background, (0, 0))
      if pygame.font:
        font = pygame.font.Font(None, 36)
        if self.snake.pellets < 70:
          text = font.render("Burgers %s" % self.snake.pellets
                              , 1, (255, 0, 0))
        else:
          text = font.render("OMGZ SO GOOD!!!!", 1, (255, 0, 0))
        textpos = text.get_rect(centerx=self.background.get_width() / 2)
        self.screen.blit(text, textpos)

      self.pellet_sprites.draw(self.screen)
      self.snake_sprites.draw(self.screen)
      pygame.display.flip()

  def LoadSprites(self):
    """Load the sprites that we need"""
    self.snake = Snake()
    self.snake_sprites = pygame.sprite.RenderPlain((self.snake))

    """figure out how many pellets we can display"""
    nNumHorizontal = int(self.width / 64)
    nNumVertical = int(self.height / 64)

    """Create the Pellet group"""
    self.pellet_sprites = pygame.sprite.Group()

    """Create all of the pellets and add them to the
    pellet_sprites group"""
    for x in range(nNumHorizontal):
      for y in range(nNumVertical):
        self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))