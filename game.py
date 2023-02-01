import pygame
import random as rand

class Game:
    def __init__(self):
        #                    X    Y
        self.play = True
        self.score = 0
        self.screen_size = [600, 600]
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.apple_pos = [int(self.screen_size[0]*0.75), int(self.screen_size[1]/2)]
        
        # MOVE
        
        self.allowed_to_turn = True
        self.snake_pos = [self.screen_size[0]*0.25, self.screen_size[1]/2]
        self.direction = "Right"
        self.snake_history = []
        
        self.previous_turn = []
        
    def spawn_apple(self):
        
        self.not_in_snake = False
        
        while self.not_in_snake == False:
            self.apple_pos = [round(0.05 * rand.randint(0, 19)*self.screen_size[0]), round(0.05 * rand.randint(0, 19)*self.screen_size[1])]
            if self.apple_pos in self.snake_history:
                continue
            else:
                self.not_in_snake = True
        
    def on_up_arrow(self):
                
        if self.direction != "Down" and self.direction != "Up" and self.allowed_to_turn == True:
            self.direction = "Up"
            self.allowed_to_turn = False
        elif self.allowed_to_turn == False:
            self.previous_turn.append("Up")
            
    def on_down_arrow(self):
            
        if self.direction != "Up" and self.direction != "Down" and self.allowed_to_turn == True:
            self.direction = "Down"
            self.allowed_to_turn = False
        elif self.allowed_to_turn == False:
            self.previous_turn.append("Down")
            
    def on_left_arrow(self):
            
        if self.direction != "Right" and self.direction != "Left" and self.allowed_to_turn == True:
            self.direction = "Left"
            self.allowed_to_turn = False
        elif self.allowed_to_turn == False:
            self.previous_turn.append("Left")
            
    def on_right_arrow(self):
            
        if self.direction != "Left" and self.direction != "Right" and self.allowed_to_turn == True:
            self.direction = "Right"
            self.allowed_to_turn = False
        elif self.allowed_to_turn == False:
            self.previous_turn.append("Right")
            
    def run(self):
        
        if self.direction == "Up":
            self.snake_pos[1] -= 30
        elif self.direction == "Down":
            self.snake_pos[1] += 30
        elif self.direction == "Left":
            self.snake_pos[0] -= 30
        elif self.direction == "Right":
            self.snake_pos[0] += 30
            
        if len(self.snake_history) <= 1:
            self.snake_history.append(self.snake_pos.copy())
        elif self.snake_history[len(self.snake_history)-2] != self.snake_pos.copy():
            self.snake_history.append(self.snake_pos.copy())
        
        
        if not self.previous_turn:
            self.allowed_to_turn = True
            
        elif len(self.previous_turn) != 0:
            self.direction = self.previous_turn[0]
            del  self.previous_turn[0]
            
        self.snake_pos[0] = int(self.snake_pos[0])
        self.snake_pos[1] = int(self.snake_pos[1])
        
        
        if self.snake_pos[0] < 0 or self.snake_pos[1] < 0 or self.snake_pos[0] > 570 or self.snake_pos[1] > 570:
            self.play = False
        if self.snake_pos == self.apple_pos:
            self.spawn_apple()
            self.score += 1
            
        while len(self.snake_history) > self.score + 1:
            self.snake_history.pop(0)
        
        self.history2 = self.snake_history.copy()
        self.history2.pop(self.score)
        for i in self.history2:
            if self.snake_pos == i:
                self.play = False