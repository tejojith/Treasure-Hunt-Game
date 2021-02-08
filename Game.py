# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:32:02 2021

@author: Tejojith 
"""
import turtle
import math
import random 

sc = turtle.Screen()
sc.bgcolor("black")
sc.title('A ""Game"" ')
sc.setup(700,700)


images = ["play_right.gif","play_left.gif",
          "tt.gif", "wall.gif","bad.gif" , "YOU WIN.gif", "YOU LOSE.gif"]

#register shapes 
#so  that Turtle recognises these images as shapes for different turtles
for i in images:
    turtle.register_shape(i)

#create pen
class Pen(turtle.Turtle):
 
 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
 
class Player(turtle.Turtle):
 
    def __init__(self):
 
        turtle.Turtle.__init__(self)
        self.shape("play_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        
    def go_up(self):
        #calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        
        #check if th espace has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            
    def go_down(self):
        #calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        
        #check if th espace has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            
    def go_left(self):
        #calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        
        self.shape("play_left.gif")
        
        #check if th espace has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        #calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        
        self.shape("play_right.gif")
        
        #check if th espace has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)    
    def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )
 
            if distance < 5:
                return True
            else:
                return False
        
        
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("tt.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
 
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
        sc.clear()
        #print()
 
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("bad.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
 
    def move(self):
            if self.direction =="up":
                dx = 0
                dy = 24
 
            elif self.direction =="down":
                dx = 0
                dy = -24
 
            elif self.direction =="left":
                dx = -24
                dy = 24
 
            elif self.direction =="right":
                dx = 24
                dy = 0
            else:
                dx = 0
                dy = 0
            #check if the player is close
            #if so go in that direction
            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction = "left"
                elif player.xcor() > self.xcor():
                    self.direction = "right"
                elif player.ycor() < self.ycor():
                    self.direction = "down"
                elif player.ycor() < self.ycor():
                    self.direction = "up"    
            
            #calculate the spot to move to
            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy
 
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", "down", "left", "right"])
 
            turtle.ontimer(self.move, t=random.randint(100, 300))
    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        
        if distance == 75:
            return True
        else:
            return False
     
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
       
            
#create level list
levels = [""]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXX       XX    X",
"XXX P XXXX       XXX    X",
"XX    XX        XXXT    X",
"XXX     X    XXXXXXX    X",
"XXXE        XXXXXXX     X",
"XXXX    X     XXXX      X",
"XXX    XX     XXX    XXXX",
"XX    XXX     XXX     XXX",
"X     XXX     XXXXX     X",
"XX    XXXXX   XXXXXX    X",
"XXX  XXXX     XXX       X",
"X   XXXXX     XXXXE     X",
"X    XXXXXXXXXXXXXXX    X",
"XX      XXXXXXXXXXXX    X",
"XXX              XXXX   X",
"XXXX             XXXX   X",
"XXXXXXXXXXXXX    XXX    X",
"XXXXXXXXXXXXX    XXX    X",
"XXX       XXX    XXX    X",
"XE               XXX    X",
"XXXX       XXXXXXXX     X",
"XXXXXX   XXXXXXXX      XX",
"X                     XXX",
"X                   XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
 
 
#adding Treasure list
treasures = []
#ADDING ENEMY LIST
enemies = []

levels.append (level_1)
 
def setup_maze(level):
 
    for y in range(len(level)):
        for x in range(len(level[y])):
 
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
 
            if character == "X":
 
 
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                
                #add coordinates to wall list
                walls.append((screen_x, screen_y))
 
            if character == "P":
                player.goto(screen_x, screen_y)
                
             #Check if it is a T (representing treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            #check is it is a enemy
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
#class instances
pen = Pen()
player = Player()

#creating wall coordinates
walls = []
 

setup_maze(levels[1])
 
 
#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"d")
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"s")
 
sc.tracer(0)
 

#start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)

#main game loop
while True:
    #Checks for player collision with treaure
    #Iterate through treaure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)
            
    for enemy in enemies:
        if player.is_collision(enemy):
            print("One of the Player's body part have been cut!!!!")
            
    if treasure not in treasures:
        sc.bgpic("YOU WIN.gif")
        sc.bgcolor("black")
        sc.title("A boring game for comp practical")
        sc.setup(700,700)         
    sc.update()