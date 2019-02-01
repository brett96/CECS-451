from map import Map
import numpy as np


class Robot:
    def __init__(self):
        self.pos = (0, 0)
        self.track = [self.pos]

    def setZero(self, home):    # Set map value of self.pos to 0
        home[self.pos[0]][self.pos[1]] = 0

    def scan(self, home):

        movingRight, movingLeft = False, False

        if self.pos == (0,0):
            if home[0][0] == 1:
                self.setZero(home)
            self.downRight(home)
            movingRight = True
            movingLeft = False
        else:
            movingLeft = True
            movingRight = False

        if movingRight:
            # Get values of surrounding area
            up = home[self.pos[0]-1][self.pos[1]]
            down = home[self.pos[0]+1][self.pos[1]]
            right = home[self.pos[0]][self.pos[1] + 1]
            left = home[self.pos[0]][self.pos[1]-1]
            upLeft = home[self.pos[0]-1][self.pos[1]-1]
            upRight = home[self.pos[0]-1][self.pos[1]+1]
            downLeft = home[self.pos[0]+1][self.pos[1]-1]
            downRight = home[self.pos[0]+1][self.pos[1]+1]

            if up == 1:
                if right == 1:
                    self.up(home)
                    self.downLeft(home)
                    self.down(home)
                    self.right(home)
                    if downRight == 1:
                        self.right(home)
                        self.up(home)
                    else:
                        self.upRight(home)
                    if upRight == 1:
                        self.up(home)
                elif upRight == 1:  # right = 0 
                    self.upRight(home)
                    self.left(home)
                    self.downLeft(home)
                    self.down(home)
                    self.right(home)
                    self.right(home)
                else:   # right & upRight = 0
                    self.up(home)
                    self.downLeft(home)
                    self.down(home)
                    self.right(home)
                    self.right(home)

            elif left == 1: # up = 0
                self.left(home)
                if downLeft == 1:
                    self.down(home)
                    self.right(home)
                else:   # up = 0, downLeft = 0, left = 1
                    self.downRight(home)
                if downRight == 1:
                    self.right(home)
                    if upRight == 1:
                        self.up(home)
                        self.up(home)
                    elif right == 1:
                        self.up(home)
                else:   # downright = 0
                    self.upRight(home)
                    if upRight == 1:
                        self.up(home)
                #if upRight == 1:
                 #   self.up(home)
            elif downLeft == 1: # up = 0, left = 0
                self.downLeft(home)
                self.right(home)
                if downRight == 1:
                    self.right(home)
                    if upRight == 1:
                        self.up(home)
                        self.up(home)
                    elif right == 1:
                        self.up(home)
                else:
                    self.upRight(home)
                if upRight == 1:
                    self.up(home)

            elif down == 1: # up = 0, left = 0, downLeft = 0
                self.down(home)
                if downRight == 1:
                    self.right(home)
                    if upRight == 1:
                        self.up(home)
                        self.up(home)
                    elif right == 1:
                        self.up(home)
                else:
                    self.upRight(home)
                    if upRight == 1:
                        self.up(home)

            else:   # up = 0, left = 0, down = 0, downLeft = 0
                self.downRight(home)
                if upRight == 1:
                    self.up(home)
                    self.up(home)
                elif right == 1:
                    self.up(home)
            if right == 1:
                pass

            if upRight == 1:
                pass

        else:   # moving left
            pass


    def up(self, home):
        if self.pos[0] > 0:    # If not on the top row, move up one row
            self.pos = (self.pos[0]-1, self.pos[1]) # Decrease row by 1
            self.setZero(home)
            self.track.append(self.pos) # Add new position to track


    def down(self, home):
        if self.pos[0] < 18:    # If not on the bottom row, move down one row
            self.pos = (self.pos[0]+1, self.pos[1]) # Increase row by 1
            self.setZero(home)
            self.track.append(self.pos) # Add new position to track


    def left(self, home):
        if self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def right(self, home):
        if self.pos[1] < 18:
            self.pos = (self.pos[0], self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)


    def upLeft(self, home):
        if self.pos[0] > 0 and self.pos[1] > 0:
            self.pos = (self.pos[0]-1, self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def upRight(self, home):
        if self.pos[0] > 0 and self.pos[1] < 18:
            self.pos = (self.pos[0]-1, self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)


    def downLeft(self, home):
        if self.pos[0] < 18 and self.pos[1] > 0:
            self.pos = (self.pos[0]+1, self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def downRight(self, home):
        if self.pos[0] < 18 and self.pos[1] < 18:
            self.pos = (self.pos[0]+1, self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)


    def clean(self, home):
        #matrix = np.array(home.dirty)
        #print(matrix[1][2])
        self.scan(home)
        
        #for row in home.dirty:
            #print(row)


    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home = np.array(home.dirty)
    agent = Robot()
    print(home)
    agent.clean(home)
    agent.show()
    print(home)
    #home.show()
