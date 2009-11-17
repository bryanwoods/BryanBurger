from bryan import *
from burger import *

class BryanBurgerMain:
  """The Main BryanBurger Class - This class handles the main
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
            self.bryan.move(event.key)

      """Check for collision"""
      lstCols = pygame.sprite.spritecollide(self.bryan
                                           , self.burger_sprites
                                           , True)
      """Update the amount of burgers eaten"""
      self.bryan.burgers = self.bryan.burgers + len(lstCols)

      """Do the drawing"""
      self.screen.blit(self.background, (0, 0))
      if pygame.font:
        font = pygame.font.Font(None, 36)
        if self.bryan.burgers < 70:
          text = font.render("Burgers %s" % self.bryan.burgers
                              , 1, (255, 0, 0))
        else:
          text = font.render("OMGZ SO GOOD!!!!", 1, (255, 0, 0))
        textpos = text.get_rect(centerx=self.background.get_width() / 2)
        self.screen.blit(text, textpos)

      self.burger_sprites.draw(self.screen)
      self.bryan_sprites.draw(self.screen)
      pygame.display.flip()

  def LoadSprites(self):
    """Load the sprites that we need"""
    self.bryan = Bryan()
    self.bryan_sprites = pygame.sprite.RenderPlain((self.bryan))

    """figure out how many burgers we can display"""
    nNumHorizontal = int(self.width / 64)
    nNumVertical = int(self.height / 64)

    """Create the Burger group"""
    self.burger_sprites = pygame.sprite.Group()

    """Create all of the burgers and add them to the
    burger_sprites group"""
    for x in range(nNumHorizontal):
      for y in range(nNumVertical):
        self.burger_sprites.add(Burger(pygame.Rect(x*64, y*64, 64, 64)))