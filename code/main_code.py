from pygame.image import load
import pygame
from random import randint
import pygame.freetype  # Import the freetype module.


class Difficulties(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_difficulty = 1

    def update(self, lst):
        pygame.draw.rect(screen, (56, 37, 11), (0, 0, 50, 50), 5)
        self.draw_text(str(lst[0]), "pictures\Roboto-Regular.ttf", 45, (102, 51, 0), 12, 0)
        pygame.draw.rect(screen, (56, 37, 11), (0, 51, 50, 50), 5)
        self.draw_text(str(lst[1]), "pictures\Roboto-Regular.ttf", 45, (102, 51, 0), 12, 50)
        pygame.draw.rect(screen, (56, 37, 11), (0, 101, 50, 50), 5)
        self.draw_text(str(lst[2]), "pictures\Roboto-Regular.ttf", 45, (102, 51, 0), 12, 100)
        pygame.draw.rect(screen, (56, 37, 11), (0, 151, 50, 50), 5)
        self.draw_text(str(lst[3]), "pictures\Roboto-Regular.ttf", 45, (102, 51, 0), 12, 150)

    def draw_text(self, text, font_name, sizes, color, x, y):
        font = pygame.font.Font(font_name, sizes)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)

    def get_click(self, pos):
        x, y = pos[0], pos[1]
        if x in range(51):
            if y in range(51):
                return 1
            if y in range(51, 101):
                return 2
            if y in range(101, 151):
                return 3
            if y in range(151, 201):
                return 4


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.draw.rect(screen, "black", (730, 0, 80, 80), 10)
        self.scr = 0
        self.lives = 0

    def update(self, lst):
        pygame.draw.rect(screen, "black", (730, 0, 80, 80), 10)
        catch = 0
        misses = 0
        for i in lst:
            if i.is_catch is True:
                catch += 1
            elif i.is_catch is False:
                misses += 1
        self.scr = catch
        self.lives = misses
        self.draw_text(str(self.scr), "pictures\Roboto-Regular.ttf", 50, (0, 0, 0), 745, 10)

    def draw_text(self, text, font_name, sizes, color, x, y):
        font = pygame.font.Font(font_name, sizes)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)


class Lava(pygame.sprite.Sprite):
    image = load("pictures/lava.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Lava.image
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (800, 20))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 480
        self.mask = pygame.mask.from_surface(self.image)


class Gold(pygame.sprite.Sprite):
    image = load("pictures/gold.png")
    fire_image = load("pictures/fire.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.is_catch = None
        self.image = pygame.transform.scale(Gold.image, (40, 30))
        color_key = self.image.get_at((0, 0))
        self.image.set_colorkey(color_key)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        if pygame.sprite.collide_mask(self, lava):
            self.is_catch = False
            self.image = pygame.transform.scale(self.fire_image, (50, 40))
            color_key = self.image.get_at((0, 0))
            self.image.set_colorkey(color_key)
            self.image = self.image.convert_alpha()
        elif pygame.sprite.collide_mask(self, trolley):
            self.is_catch = True
            self.rect.x = 1000
            self.rect.y = 1000
        if self.is_catch is None:
            self.rect.y += 2


class Trolley(pygame.sprite.Sprite):
    image = load("pictures/trolley_2.png")

    def __init__(self):
        super().__init__(all_sprites)
        color_key = self.image.get_at((0, 0))
        self.image.set_colorkey(color_key)
        self.image = pygame.transform.scale(self.image, (160, 110))
        self.image = self.image.convert_alpha()
        self.speed = 0
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 320
        self.rect.y = 380

    def update(self, speed):
        if speed == -1 and self.rect.x == 0 or speed == 1 and self.rect.x == 640:
            self.speed = speed
            self.rect.x -= self.speed
        else:
            self.speed = speed
            self.rect.x += self.speed


class GameOver(pygame.sprite.Sprite):
    image = load("pictures/game_over.png")
    image = pygame.transform.scale(image, (800, 500))

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(all_sprites)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -800
        self.rect.y = 0

    def update(self):
        self.rect.x += 4


class TheWin(pygame.sprite.Sprite):
    image = load("pictures/win.png")
    image = pygame.transform.scale(image, (800, 500))

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(all_sprites)
        self.image = TheWin.image
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -800
        self.rect.y = 0

    def update(self):
        self.rect.x += 2


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Balls')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    running = True
    all_sprites = pygame.sprite.Group()
    score = Score()
    trolley = Trolley()
    lava = Lava()
    difficulties = Difficulties()
    gameover = None
    win = None
    v = 0
    trolley_speed = 4

    clock = pygame.time.Clock()
    fps = 60
    gold_list = list()
    difficulty_list = [1, 2, 3, 4]

    SPAWNGOLD = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNGOLD, 2000)

    while running:
        screen.fill((160, 110, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = difficulties.get_click(event.pos)
                if cell is not None:
                    v = 0
                    if cell == 1:
                        trolley_speed = 8
                    if cell == 2:
                        trolley_speed = 6
                    if cell == 3:
                        trolley_speed = 4
                    if cell == 4:
                        trolley_speed = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if v != -trolley_speed and trolley.rect.x > 0:
                        v -= trolley_speed
                    else:
                        v = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if v != trolley_speed and trolley.rect.x < 640:
                        v += trolley_speed
                    else:
                        v = 0
            if event.type == SPAWNGOLD:
                gold_list.append(Gold((randint(0, 770))))
        if score.lives >= 3:
            if gameover is None:
                gameover = GameOver()
                pygame.time.set_timer(SPAWNGOLD, 200000)
            if gameover.rect.x != 0:
                gameover.update()
        elif score.scr >= 20:
            if win is None:
                win = TheWin()
                pygame.time.set_timer(SPAWNGOLD, 200000)
            if win.rect.x != 0:
                win.update()
        else:
            if trolley.rect.x == 0:
                v += trolley_speed
            elif trolley.rect.x == 640:
                v -= trolley_speed
            all_sprites.update(v)
            score.update(gold_list)
            difficulties.update(difficulty_list)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
