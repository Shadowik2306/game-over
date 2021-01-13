import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class GameOver(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('gameover.png', -1)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -600, 0

    def update(self):
        if self.rect.x != 0:
            self.rect.x += 1


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    fps = 60
    gmov = GameOver()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(gmov)
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
