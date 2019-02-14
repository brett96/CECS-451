from map import Map
import numpy as np


class Robot:
    def __init__(self):
        self.pos = (0, 0)
        self.track = [self.pos]
        self.movingRight = True

    def setZero(self, home):    # Set map value of self.pos to 0
        home[self.pos[0]][self.pos[1]] = 0

    def finish(self, home): # Clean entire last row and last column
        for i in range(0, len(home[1])):
            self.right(home)
        for j in range(0, len(home[0])):
            self.up(home)

    def clean(self, home):
        if self.pos[0] > 17 or self.pos[1] > 17:    # Make sure robot is not in row or column 15 or higher
            return

        if home[self.pos[0]][self.pos[1]] == 1: # If current position is dirty, clean it
            self.setZero(home)
        if self.movingRight:    # Go to center
            self.downRight(home)

        # Start off in center of 3x3 and look around
        if self.movingRight:
            adjValues = self.scan(home) # Get values of surroundings
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

            #
            # Follow a cleaning pattern based on which areas are dirty and which are clean
            else:
                if adjValues["up"] == 1:
                    self.up(home)
                    self.downLeft(home)
                    if adjValues["downLeft"] == 1:
                        self.down(home)
                        self.right(home)
                    else:
                        self.downRight(home)
                elif adjValues["left"] == 1:
                    self.left(home)
                    if adjValues["downLeft"] == 1:
                        self.down(home)
                        self.right(home)
                    else:
                        self.downRight(home)
                elif adjValues["downLeft"] == 1:
                    self.downLeft(home)
                    self.right(home)
                else:
                    self.down(home)    

                # At bottom
                if adjValues["downRight"] == 1:
                    self.right(home)
                    self.up(home)
                else:
                    self.upRight(home)
                # At Right
                if adjValues["upRight"] == 1:
                    self.up(home)
                    self.right(home)
                else:
                    self.upRight(home)
                # At top left of next square

            if self.pos[1] == 17:   # If at right edge, go down and start going left
                self.down(home)
                self.movingRight = False

        else:   # moving left
            self.downLeft(home) # Go to center
            if self.pos[0] > 17:    # At bottom left corner:  exit and start finish pattern
                return
            adjValues = self.scan(home)
            if self.pos[1] <= 1:    # At left edge
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

        self.clean(home)    # 3x3 square is clean, start cleaning next square
        
    def scan(self, home):   # Get a dictionary of adjacent location:values
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


    def up(self, home): # Go up from current location
        if self.pos[0] > 0:    # If not on the top row, move up one row
            self.pos = (self.pos[0]-1, self.pos[1]) # Decrease row by 1
            self.setZero(home)
            self.track.append(self.pos) # Add new position to track


    def down(self, home):   # Go down from current location
        if self.pos[0] < 18:    # If not on the bottom row, move down one row
            self.pos = (self.pos[0]+1, self.pos[1]) # Increase row by 1
            self.setZero(home)
            self.track.append(self.pos) # Add new position to track


    def left(self, home):   # Go left
        if self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def right(self, home):  # Go down
        if self.pos[1] < 18:
            self.pos = (self.pos[0], self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)


    def upLeft(self, home): # Go up and to the left
        if self.pos[0] > 0 and self.pos[1] > 0:
            self.pos = (self.pos[0]-1, self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def upRight(self, home):    # Go up and to the right
        if self.pos[0] > 0 and self.pos[1] < 18:
            self.pos = (self.pos[0]-1, self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)


    def downLeft(self, home):   # Go down and to the left
        if self.pos[0] < 18 and self.pos[1] > 0:
            self.pos = (self.pos[0]+1, self.pos[1]-1)
            self.setZero(home)
            self.track.append(self.pos)


    def downRight(self, home):  # Go down and to the right
        if self.pos[0] < 18 and self.pos[1] < 18:
            self.pos = (self.pos[0]+1, self.pos[1]+1)
            self.setZero(home)
            self.track.append(self.pos)

    def show(self): # Show total number of steps taken
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    home = np.array(home.dirty)
    agent = Robot()
    print(home)
    agent.clean(home)
    agent.finish(home)
    print(agent.track)
    agent.show()
    print(home)
    #home.show()
