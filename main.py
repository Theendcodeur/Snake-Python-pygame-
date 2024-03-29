import pygame
import random as rand

from game import Game
import time as t
pygame.init()
pygame.display.set_caption('Snake')


game = Game()
play =0
running = True
time = round(t.time(), 3)

def updateTitle(score):
    pygame.display.set_caption(f"Snake (Score: {score})".format(score))

    pygame.display.update()

pygame.draw.rect(game.screen, "green", (game.screen_size[0]*0.25, game.screen_size[1]/2, 30, 30))
while running:
    if play == 1:
        pygame.draw.rect(game.screen, "black", (0, 0, game.screen_size[0], game.screen_size[1]))
    
                                        #  X                     Y
    for i in game.snake_history:
        pygame.draw.rect(game.screen, "green", (i[0], i[1], 30, 30))
        
    pygame.draw.rect(game.screen, "red", (game.apple_pos[0], game.apple_pos[1], 30, 30))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.on_left_arrow()
            elif event.key == pygame.K_RIGHT:
                game.on_right_arrow()
                play = 1
            elif event.key == pygame.K_UP:
                game.on_up_arrow()
                play = 1
            elif event.key == pygame.K_DOWN:
                game.on_down_arrow()
                play = 1
                
    if t.time() - time >= 0.1 and play == 1:
        game.run()
        time = round(t.time(), 3)
    
    updateTitle(game.score);
    if game.play == True:
        pygame.display.flip()
    elif game.play == False:
        running = False
pygame.quit() 
 #comment 
 #comment 
 #comment 
 #comment
