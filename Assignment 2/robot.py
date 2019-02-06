from map import Map
import numpy as np


class Robot:
    def __init__(self):
        self.pos = (0, 0)
        self.track = [self.pos]
        self.movingRight = True

    def setZero(self, home):    # Set map value of self.pos to 0
        home[self.pos[0]][self.pos[1]] = 0

    def clean(self, home):
        if self.pos[0] > 17 or self.pos[1] > 17:    # Make sure robot is not in row or column 15 or higher
            return

        #elif self.pos[0] % 3 == 0 and self.pos[1] % 3 == 0:   # Assert that robot starts off in a top right corner
        if home[self.pos[0]][self.pos[1]] == 1:
            self.setZero(home)
        if self.movingRight:
            self.downRight(home)
        #else:
         #   print("Robot should not be here: " + self.pos)
          #  print(self.track)

        # Start off in center of 3x3 and look around
        if self.movingRight:
            adjValues = self.scan(home)
            if self.pos[1] == 16:  # In rightmost 3x3 square
                if adjValues["upRight"] == 1:
                    self.upRight(home)
                    self.left(home)
                    self.downLeft(home)
                elif adjValues["up"] == 1:
                    self.up(home)
                    self.downLeft(home)
                else:
                    self.left(home)
        
                # At left
                if adjValues["downLeft"] == 1:
                    self.down(home)
                    self.right(home)
                else:
                    self.downRight(home)
                # At down
                if adjValues["right"] == 1:
                    self.upRight(home)
                    self.down(home)
                else:
                    self.right(home)


            # Follow a cleaning pattern based on which areas are dirty and which are clean
            elif adjValues["up"] == 1: 
                if adjValues["right"] == 1:
                    self.up(home)
                    self.downLeft(home)
                    self.down(home)
                    self.right(home)
                    if adjValues["downRight"] == 1:
                        self.right(home)
                        self.up(home)
                    else:
                        self.upRight(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)
                elif adjValues["upRight"] == 1:  # right = 0 
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

            elif adjValues["left"] == 1: # up = 0
                self.left(home)
                if adjValues["downLeft"] == 1:
                    
                    self.down(home)
                    self.right(home)
                else:   # up = 0, downLeft = 0, left = 1
                    self.downRight(home)
                if adjValues["downRight"] == 1:
                    self.right(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)
                        self.up(home)
                    elif adjValues["right"] == 1:
                        self.up(home)
                else:   # downright = 0
                    self.upRight(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)
                #if upRight == 1:
                 #   self.up(home)
            elif adjValues["downLeft"] == 1: # up = 0, left = 0
                self.downLeft(home)
                self.right(home)
                if adjValues["downRight"] == 1:
                    self.right(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)
                        self.up(home)
                    elif adjValues["right"] == 1:
                        self.up(home)
                else:
                    self.upRight(home)
                if adjValues["upRight"] == 1:
                    self.up(home)

            elif adjValues["down"] == 1: # up = 0, left = 0, downLeft = 0
                self.down(home)
                if adjValues["downRight"] == 1:
                    self.right(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)
                        self.up(home)
                    elif adjValues["right"] == 1:
                        self.up(home)
                else:
                    self.upRight(home)
                    if adjValues["upRight"] == 1:
                        self.up(home)

            else:   # up = 0, left = 0, down = 0, downLeft = 0
                self.downRight(home)
                if adjValues["upRight"] == 1:
                    self.up(home)
                    self.up(home)
                elif adjValues["right"] == 1:
                    self.up(home)

            if self.pos[1] == 17:
                self.down(home)
                self.movingRight = False
            else:
                # Current box is clean
                # Get to the top left corner of the next 3x3 box
                current = self.pos[0] % 3  # Get current row location
                if current == 0:    # Already in correct row; move right
                    self.right(home)
                elif current == 1:  # Need to go up and to the right
                    self.upRight(home)
                else:               # Need to go up, then up and to the right
                    self.up(home)
                    self.upRight(home)

        else:   # moving left
            self.downLeft(home) # Go to center
            if self.pos[0] > 17:
                return
            adjValues = self.scan(home)
            if self.pos[1] <= 1:
                if adjValues["down"] == 1:
                    self.down(home)
                    if adjValues["downRight"] == 1:
                        self.right(home)
                        self.up(home)
                        self.upLeft(home)
                    else:
                        self.upRight(home)
                        self.upLeft(home)
                elif adjValues["downRight"] == 1:
                    self.downRight(home)
                    self.up(home)
                    self.upLeft(home)
                elif adjValues["right"] == 1:
                    self.right(home)
                    self.upLeft(home)
                else:
                    self.up(home)
                # At top
                if adjValues["upLeft"] == 1:
                    self.left(home)
                    self.down(home)
                    self.down(home)
                else:
                    self.downLeft(home)
                    self.down(home)
                self.down(home)
                self.movingRight = True


            else:
                
                if adjValues["right"] == 1:
                    self.right(home)
                    if adjValues["downRight"] == 1:
                        self.down(home)
                        self.left(home)
                    else:
                        self.downLeft(home)
                elif adjValues["downRight"] == 1:
                    self.downRight(home)
                    self.left(home)
                else:
                    self.down(home)
                # At down
                if adjValues["downLeft"] == 1:
                    self.left(home)
                    self.up(home)
                else:
                    self.upLeft(home)
                # At left
                if adjValues["up"] == 1:
                    self.upRight(home)
                    self.left(home)
                    self.left(home)
                elif adjValues["upLeft"] == 1:
                    self.up(home)
                    self.left(home)
                else:
                    self.upLeft(home)

        self.clean(home)
        
    def scan(self, home):
        adjValues = {}
        adjValues["up"] = home[self.pos[0]-1][self.pos[1]]
        adjValues["down"] = home[self.pos[0]+1][self.pos[1]]
        adjValues["right"] = home[self.pos[0]][self.pos[1] + 1]
        adjValues["left"] = home[self.pos[0]][self.pos[1]-1]
        adjValues["upLeft"] = home[self.pos[0]-1][self.pos[1]-1]
        adjValues["upRight"] = home[self.pos[0]-1][self.pos[1]+1]
        adjValues["downLeft"] = home[self.pos[0]+1][self.pos[1]-1]
        adjValues["downRight"] = home[self.pos[0]+1][self.pos[1]+1] 
        return adjValues


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


    #def clean(self, home):
        #matrix = np.array(home.dirty)
        #print(matrix[1][2])
        #self.scan(home)
        #print(self.track)
        
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
    print(agent.track)
    agent.show()
    print(home)
    #home.show()
