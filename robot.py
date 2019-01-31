from map import Map
import numpy as np


class Robot:
    def __init__(self):
        self.pos = (0, 0)
        self.track = [self.pos]

    def scan(self):

        movingRight = True

        if movingRight:
            up = (self.pos[0]-1, self.pos[1])
            right = (self.pos[0], self.pos[1] + 1)
            upRight = (self.pos[0]-1, self.pos[1]+1)

            if up == 1:
                if right == 1 and upRight == 0:
                    self.up
                    self.downLeft
                    self.down
                    self.right
                    self.right
                    self.up
                else:   # All three = 1
                    self.up
                    self.downLeft
                    self.down
                    self.right
                    self.right
                    self.up
                    self.up

            if right == 1:
                pass

            if upRight == 1:
                pass

        else:   # moving left
            pass


    def up(self):
        if self.pos[0] > 0:    # If not on the top row, move up one row
            self.pos = (self.pos[0]-1, self.pos[1]) # Decrease row by 1
            self.track.append(self.pos) # Add new position to track


    def down(self):
        if self.pos[0] < 18:    # If not on the bottom row, move down one row
            self.pos = (self.pos[0]+1, self.pos[1]) # Increase row by 1
            self.track.append(self.pos) # Add new position to track


    def left(self):
        if self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1]-1)
            self.track.append(self.pos)


    def right(self):
        if self.pos[1] < 18:
            self.pos = (self.pos[0], self.pos[1]+1)
            self.track.append(self.pos)


    def topLeft(self):
        if self.pos[0] > 0 and self.pos[1] > 0:
            self.pos = (self.pos[0]-1, self.pos[1]-1)
            self.track.append(self.pos)


    def upRight(self):
        if self.pos[0] > 0 and self.pos[1] < 18:
            self.pos = (self.pos[0]-1, self.pos[1]+1)
            self.track.append(self.pos)


    def downLeft(self):
        if self.pos[0] < 18 and self.pos[1] > 0:
            self.pos = (self.pos[0]+1, self.pos[1]-1)
            self.track.append(self.pos)


    def downRight(self):
        if self.pos[0] < 18 and self.pos[1] < 18:
            self.pos = (self.pos[0]+1, self.pos[1]+1)
            self.track.append(self.pos)


    def clean(self, home):
        matrix = np.array(home.dirty)
        print(matrix[1][2])
        
        #for row in home.dirty:
            #print(row)


    def show(self):
        print('Number of steps: ', len(self.track) - 1)


if __name__ == '__main__':
    home = Map(19, 19)
    agent = Robot()
    agent.clean(home)
    agent.show()
    home.show()
