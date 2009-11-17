from PyManMain import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

if __name__ == "__main__":
  MainWindow = PyManMain()
  MainWindow.MainLoop()