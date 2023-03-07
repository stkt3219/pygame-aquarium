import pygame
from sys import exit
import random
from pygame import mixer


class RightFish(pygame.sprite.Sprite):
    def __init__(self, src, x, y):
        super().__init__()
        self.x = random.randint(-600, -100)
        self.y = random.randint(100, 500)
        self.image = pygame.image.load(src).convert_alpha()
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        # self.rect = self.image.get_rect()

    def update(self):
        # called each frame
        # moves block to the right 1 pixel
        self.x += random.randint(1, 2)
        if self.x > WINDOW_WIDTH:
            self.x = random.randint(-600, -100)
            # self.y = random.randint(100, 400)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class LeftFish(pygame.sprite.Sprite):
    def __init__(self, src, x, y):
        super().__init__()
        self.x = random.randint(1100, 1500)
        self.y = random.randint(100, 500)
        self.image = pygame.image.load(src).convert_alpha()
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

    def update(self):
        # called each frame
        # moves block to the right 1 pixel
        self.x -= random.randint(1, 2)
        if self.x < -100:
            self.x = random.randint(1100, 1500)
            # self.y = random.randint(100, 400)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
DEFAULT_IMAGE_SIZE = (120, 120)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
mixer.music.load("indoor-fish-tank.mp3")
mixer.music.play()
pygame.display.set_caption('Aquarium')
clock = pygame.time.Clock()

background = pygame.image.load("aquarium-images/aquarium-background.png").convert()
background = pygame.transform.scale(background, screen.get_size())  # scale the bg image

# right_fish_list = ["aquarium-images/angel-fish.png",
#                    "aquarium-images/green-fish.png",
#                    "aquarium-images/nemo.png",
#                    "aquarium-images/purple-fish.png"]

right_fish_list = [
    RightFish("aquarium-images/angel-fish.png", 0, 0),
    RightFish("aquarium-images/green-fish.png", 0, 0),
    RightFish("aquarium-images/nemo.png", 0, 0),
    RightFish("aquarium-images/purple-fish.png", 0, 0)
]

left_fish_list = [
    LeftFish("aquarium-images/dory.png", 0, 0),
    LeftFish("aquarium-images/goldfish.png", 0, 0),
    LeftFish("aquarium-images/orange-brown-fish.png", 0, 0),
    LeftFish("aquarium-images/yellow-fish.png", 0, 0),
]

# fishA = pygame.image.load("aquarium-images/angel-fish.png").convert_alpha()
# fishB = pygame.image.load("aquarium-images/dory.png").convert_alpha()
# fishC = pygame.image.load("aquarium-images/goldfish.png").convert_alpha()
# fishD = pygame.image.load("aquarium-images/green-fish.png").convert_alpha()
# fishE = pygame.image.load("aquarium-images/nemo.png").convert_alpha()
# fishF = pygame.image.load("aquarium-images/orange-brown-fish.png").convert_alpha()
# fishG = pygame.image.load("aquarium-images/purple-fish.png").convert_alpha()
# fishH = pygame.image.load("aquarium-images/yellow-fish.png").convert_alpha()

# fish1 = RightFish("aquarium-images/angel-fish.png", 0, random.randint(200, 400))
# fish2 = RightFish("aquarium-images/green-fish.png", 0, random.randint(200, 400))
# fish3 = RightFish("aquarium-images/nemo.png", 0, random.randint(200, 400))
# fish4 = RightFish("aquarium-images/purple-fish.png", 0, random.randint(200, 400))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    for fish in right_fish_list:
        fish.draw()
        fish.update()

    for fish in left_fish_list:
        fish.draw()
        fish.update()

    # draw all the elements
    # update everything
    pygame.display.update()
    # loop should not run faster than 60 times per second
    clock.tick(60)
