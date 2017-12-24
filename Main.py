import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Jeu de l'oie")
font = pygame.font.Font(None, 50)
rect_visible = []
player_count = 2


def showmainscreen():
    rect_visible.clear()
    window.fill((231, 242, 255))
    choose_player_count = font.render('Choisissez le nombre de joueurs', 1, (0, 0, 0))
    window.blit(choose_player_count, (328, 125))
    # center = pygame.Rect(600, 0, 1, 700)
    button2player = pygame.Rect(375, 200, 450, 100)
    button3player = pygame.Rect(375, 350, 450, 100)
    button4player = pygame.Rect(375, 500, 450, 100)
    text2player = font.render('2 joueurs', 1, (0, 0, 0))
    text3player = font.render('3 joueurs', 1, (0, 0, 0))
    text4player = font.render('4 joueurs', 1, (0, 0, 0))
    rect_visible.append(button2player)
    rect_visible.append(button3player)
    rect_visible.append(button4player)
    pygame.draw.rect(window, [50, 107, 146], button2player)
    pygame.draw.rect(window, [50, 107, 146], button3player)
    pygame.draw.rect(window, [50, 107, 146], button4player)
    window.blit(text2player, (button2player.centerx-font.size("2 joueurs")[0]/2, button2player.centery-font.size("2 joueurs")[1]/2))
    window.blit(text3player, (button3player.centerx-font.size("3 joueurs")[0]/2, button3player.centery-font.size("3 joueurs")[1]/2))
    window.blit(text4player, (button4player.centerx-font.size("4 joueurs")[0]/2, button4player.centery-font.size("4 joueurs")[1]/2))
    # pygame.draw.rect(window, [255, 0, 0], center)
    pygame.display.flip()


def startgame(playercount: int):
    global player_count
    player_count = playercount
    print(playercount)
    # TODO Je sais compter jusqu'à 2 en Hindou : in, dou


def actionbyrect(rect: Rect):
    if rect.x == 375 and rect.y == 200 and rect.width == 450 and rect.height == 100:  # button2player
        startgame(2)
    if rect.x == 375 and rect.y == 350 and rect.width == 450 and rect.height == 100:  # button3player
        startgame(3)
    if rect.x == 375 and rect.y == 500 and rect.width == 450 and rect.height == 100:  # button4player
        startgame(4)


showmainscreen()

gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for rect in rect_visible:
                if rect.collidepoint(mouse_pos):
                    actionbyrect(rect)
        elif event.type == QUIT:
            gameloop = False
pygame.quit()
