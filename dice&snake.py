# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:30:34 2018

@author: zhaoy
"""



from appJar import gui #imports the gui library from appJar


print("Yiwen, Quan, Kristie, Huy")

import random
import string
import tkinter
import time

def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Dice Rolling Game":
        app.infoBox("b1","this is our first game, dice rolling")
       # this game will be created by Quan and Yiwen 
        def Dice_Roll(roll_a_number):
            print("The Dice rolled..." + str(roll_a_number))
            print("you guys are all wrong, plz roll again!!!")
            re_Roll = random.randint(1,6)
            time.sleep(1)
            return re_Roll
#Generic function for what the winner and loser do; not player specific
        def Win(winner, loser, prz):
            print("The Dice rolled..." + str(diceNumber) + "\n" + str(winner).upper() + "Wins\n" + str(loser) + " must " + str(prz))
#Copied from your code
        print("lets play Dice Rolling!!!!!")
        player1 = input("Player 1 name?")
        player2 = input("Player 2 name?")
        prize = input("What does the loser have to do?")
#prize = input("What does the loser have to do?")
#slightly condensed your code
        print("Hi " + player1 + " & " + player2 + ", let's roll the dice!!!")
#moved this to a more appropriate place
        diceNumber = random.randint(1,6)
        play1Num = int(input(player1 + " choose a number 1-6."))
        play2Num = int(input(player2 + " choose a number 1-6."))
#changed while loop to roll the dice every time both are wrong
        while play1Num != diceNumber and play2Num != diceNumber:
            diceNumber = Dice_Roll(diceNumber)
            play1Num = int(input(player1 + " choose a number 1-6."))
            play2Num = int(input(player2 + " choose a number 1-6."))

        if play1Num == diceNumber:
            Win(player1, player2, prize)
        elif play2Num == diceNumber:
            Win(player2, player1, prize)
#Array implementation of win (with more than 2 players, would be best done using *args in win)
        players = [play1Num, play2Num]
        for item in players:
            if diceNumber == item:
                players.remove(item)
                Win(item, players[1], prize)
        
            
    elif btn == "Snake Game":
        app.infoBox("b1","this is our second game, Snake game")
       #this game will be created by Huy and Kristie 
        HEAD_CHARACTER = 'ö'
        FOOD_CHARACTERS = string.ascii_letters


        class Application:
            TITLE = 'Snake'
            SIZE = 300, 300

            def __init__(self, master):
                    self.master = master

                    self.head = None
                    self.head_position = None
                    self.segments = []
                    self.segment_positions = []
                    self.food = None
                    self.food_position = None
                    self.direction = None
                    self.moved = True

                    self.running = False
                    self.init()

            def init(self):
                    self.master.title(self.TITLE)

                    self.canvas = tkinter.Canvas(self.master)
                    self.canvas.grid(sticky=tkinter.NSEW)
                    
                    self.start_button = tkinter.Button(self.master, text='Start', command=self.on_start)
                    self.start_button.grid(sticky=tkinter.EW)

                    self.master.bind('w', self.on_up)
                    self.master.bind('a', self.on_left)
                    self.master.bind('s', self.on_down)
                    self.master.bind('d', self.on_right)

                    self.master.columnconfigure(0, weight=1)
                    self.master.rowconfigure(0, weight=1)
                    self.master.resizable(width=False, height=False)
                    self.master.geometry('%dx%d' % self.SIZE)

            def on_start(self):
                    self.reset()
                    if self.running:
                        self.running = False
                        self.start_button.configure(text='Start')
                    else:
                        self.running = True
                        self.start_button.configure(text='Stop')
                        self.start()

            def reset(self):
                    self.segments.clear()
                    self.segment_positions.clear()
                    self.canvas.delete(tkinter.ALL)

            def start(self):
                    width = self.canvas.winfo_width()
                    height = self.canvas.winfo_height()

                    self.canvas.create_rectangle(10, 10, width-10, height-10)
                    self.direction = random.choice('wasd')
                    head_position = [round(width // 2, -1), round(height // 2, -1)]
                    self.head = self.canvas.create_text(tuple(head_position), text=HEAD_CHARACTER)
                    self.head_position = head_position
                    self.spawn_food()
                    self.tick()

            def spawn_food(self):
                    width = self.canvas.winfo_width()
                    height = self.canvas.winfo_height()
                    positions = [tuple(self.head_position), self.food_position] + self.segment_positions
                    
                    position = (round(random.randint(20, width-20), -1), round(random.randint(20, height-20), -1))
                    while position in positions:
                        position = (round(random.randint(20, width-20), -1), round(random.randint(20, height-20), -1))

                    character = random.choice(FOOD_CHARACTERS)
                    self.food = self.canvas.create_text(position, text=character)
                    self.food_position = position
                    self.food_character = character

            def tick(self):
                    width = self.canvas.winfo_width()
                    height = self.canvas.winfo_height()
                    previous_head_position = tuple(self.head_position)

                    if self.direction == 'w':
                        self.head_position[1] -= 10
                    elif self.direction == 'a':
                        self.head_position[0] -= 10
                    elif self.direction == 's':
                        self.head_position[1] += 10
                    elif self.direction == 'd':
                        self.head_position[0] += 10

                    head_position = tuple(self.head_position)
                    if (self.head_position[0] < 10 or self.head_position[0] >= width-10 or
                        self.head_position[1] < 10 or self.head_position[1] >= height-10 or
                        any(segment_position == head_position for segment_position in self.segment_positions)):
                        self.game_over()
                        return

                    if head_position == self.food_position:
                        self.canvas.coords(self.food, previous_head_position)
                        self.segments.append(self.food)
                        self.segment_positions.append(previous_head_position)
                        self.spawn_food()

                    if self.segments:
                        previous_position = previous_head_position
                        for index, (segment, position) in enumerate(zip(self.segments, self.segment_positions)):
                            self.canvas.coords(segment, previous_position)
                            self.segment_positions[index] = previous_position
                            previous_position = position

                    self.canvas.coords(self.head, head_position)
                    self.moved = True

                    if self.running:
                        self.canvas.after(50, self.tick)

            def game_over(self):
                width = self.canvas.winfo_width()
                height = self.canvas.winfo_height()

                self.running = False
                self.start_button.configure(text='Start')
                score = len(self.segments) * 10
                self.canvas.create_text((round(width // 2, -1), round(height // 2, -1)), text='Game Over! Your score was: %d' % score)

            def on_up(self, event):
                if self.moved and not self.direction == 's':
                    self.direction = 'w'
                    self.moved = False

            def on_down(self, event):
                if self.moved and not self.direction == 'w':
                    self.direction = 's'
                    self.moved = False

            def on_left(self, event):
                if self.moved and not self.direction == 'd':
                    self.direction = 'a'
                    self.moved = False

            def on_right(self, event):
                if self.moved and not self.direction == 'a':
                    self.direction = 'd'
                    self.moved = False


        def main():
            root = tkinter.Tk()
            Application(root)
            root.mainloop()


        if __name__ == '__main__':
            main()
            
    elif btn == "Game X":
        app.infoBox("b1","this is our third game, X game")       
            
            
            
            
            
    else:
            print('Pick a valid option')



app=gui("Main Menu","500x500")

#Replace "Blank Team" with your team name in line 41

app.addLabel("title", "Welcome to Snake Team's Game Menu")
app.setLabelBg("title", "white")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 47

app.addImage("decor","snake.gif")
app.setFont(10)

#change the names Button 1-5 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Dice Rolling Game", press)
app.addButton("Snake Game", press)
app.addButton("Game X", press)
app.addButton("HAHAHA!", press)

app.addButton("Exit",press)
app.go() #displays the gui


