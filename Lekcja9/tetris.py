import sys
from random import random
from time import sleep
import pygame
from pygame.sprite import Group




class BlockBasic(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
    def update(self):
        self.rect.move_ip(0,50)

def random_block():
    # choice = round((random()) * 4)
    group = Group()
    choice = 3

    colors = [
        pygame.Color('cyan'),  # I piece
        pygame.Color('blue'),  # J piece
        pygame.Color('orange'),  # L piece
        pygame.Color('yellow'),  # O piece
        pygame.Color('green'),  # S piece
        pygame.Color('red'),  # Z piece
        pygame.Color('purple'),  # T piece
    ]

    offset = (width/2) -50
    if choice == 0:
        group.add(BlockBasic(0+offset, 0, 50, 50, color = round((random()) * 6)))
    elif choice == 1:
        group.add(BlockBasic(0+offset, 0, 100, 50,color = round((random()) * 6)))
    elif choice == 2:
        group.add(BlockBasic(0+offset, 0, 150, 50, color = round((random()) * 6)))
    elif choice == 3:
        color = colors[round(random() * 6)]
        group.add(BlockBasic(0+offset, 0, 150, 50,color=color))
        group.add(BlockBasic(50+offset, 0, 50, 150,color=color))
    elif choice == 4:
        color = colors[round(random()*6)]
        group.add(BlockBasic(0+offset, 0, 100, 50, color=color))
        group.add(BlockBasic(0+offset, 0, 50, 150,color=color))
    return group






if __name__ == "__main__":
    # variables
    group_static = Group()
    group_falling = Group()
    speed_vec = (0,50)
    FPS = 60

    pygame.init()
    pygame.display.set_caption('Tetris game')

    # Clock setup max 60 fps
    BLOCKSPAWN_EVENT = pygame.USEREVENT + 1
    BLOCKMOVE_EVENT = pygame.USEREVENT + 2
    clock = pygame.time.Clock()

    # setting blockspawn event and blockmove event
    pygame.time.set_timer(BLOCKSPAWN_EVENT, 50000)
    pygame.time.set_timer(BLOCKMOVE_EVENT, 1000)


    # colors and sizes and fonts
    size_surface = width, height = (800,600)
    surface_color = pygame.Color("black")
    text_color = pygame.Color("red")
    font = pygame.font.SysFont("Arial", 50)

    # Main surface setup
    surface = pygame.display.set_mode(size_surface)
    surface.fill(surface_color)

    # creating invisible down border
    group_falling.add(random_block())
    group_static.add(BlockBasic(0, height, width, 1, color=pygame.Color('white')))

    # ==============MAIN GAME LOOP==============
    done = False
    game_over = False
    while not done:

        # check colission with already static objects
        for sprite_fall in group_falling:
            for sprite_static in group_static:
                if sprite_fall.rect.move(*speed_vec).colliderect(sprite_static.rect):
                    group_static.add(group_falling)
                    group_falling.empty()
                    pygame.event.post(pygame.event.Event(BLOCKSPAWN_EVENT))

        # check if we are above hight limit
        for sprite in group_static:
            if sprite.rect.y == 0:
                done = True
                game_over = True

        # main event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    done = True
                if event.key == pygame.K_a: pass
                if event.key == pygame.K_d: pass
                if event.key == pygame.K_s: pass
            if event.type == BLOCKSPAWN_EVENT:
                group_falling.add(random_block())
            if event.type == BLOCKMOVE_EVENT:
                group_falling.update()

        surface.fill(surface_color)
        group_falling.draw(surface)
        group_static.draw(surface)

        pygame.display.update()
        clock.tick(FPS)
    # ==============END OF MAIN GAME LOOP==============


    # ==============END SCREEN LOOP==============
    clicked = False
    if game_over:
        text = "Gameover"
    else:
        text = "Victory"
    while not clicked:
        text_surf = font.render(text, False, text_color)
        text_rect = text_surf.get_rect(center=(width / 2, height / 2))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clicked = True
            if event.type == pygame.QUIT:
                clicked = True

        surface.blit(text_surf, text_rect)
        pygame.display.update()
    # ==============END OF END SCREEN LOOP==============


    pygame.quit()
