import sys
import pygame

WIDTH, HEIGHT = 640, 480
FPS = 60

def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Blank Window")
  clock = pygame.time.Clock()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((30, 32, 40))
    pygame.display.flip()
    clock.tick(FPS)

  pygame.quit()
  sys.exit()


if __name__ == "__main__":
  main()