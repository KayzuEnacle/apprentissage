import tkinter as tk
from random import randrange

class Tetris:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=200, height=400)
        self.canvas.pack()
        self.score = 0
        self.board = [[' ']*10 for _ in range(20)]
        self.shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 1], [1, 0, 0]]
        ]
        self.shape = self.shapes[randrange(len(self.shapes))]
        self.position = [0, 4]

    def draw(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == ' ':
                    self.canvas.create_rectangle(j*20, i*20, j*20+20, i*20+20, fill='black')
                else:
                    self.canvas.create_rectangle(j*20, i*20, j*20+20, i*20+20, fill='black')

    def move(self, dx, dy):
        self.position[1] += dx
        self.position[0] += dy

    def rotate(self):
        self.shape = [list(x) for x in zip(*self.shape[::-1])]

    def drop(self):
        while not self.collision([1, 0]):
            self.move(0, 1)

    def game_over(self):
        return self.collision([1, 0])

    def collision(self, offset):
        off_x, off_y = offset
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell and (i + self.position[0] + off_x >= 20 or
                             j + self.position[1] + off_y >= 10 or
                             j + self.position[1] + off_y < 0 or 
                             self.board[i + self.position[0] + off_x][j + self.position[1] + off_y] != ' '):
                    return True
        return False

    def tick(self):
        if not self.collision([1, 0]):
            self.move(0, 1)
        else:
            for i, row in enumerate(self.shape):
                for j, cell in enumerate(row):
                    if cell:
                        self.board[i + self.position[0]][j + self.position[1]] = 'black'
            self.score += 1
            self.shape = self.shapes[randrange(len(self.shapes))]
            self.position = [0, 4]
            if self.collision([0, 0]):
                self.board = [[' ']*10 for _ in range(20)]
                self.score = 0
        self.draw()

    def on_key_press(self, event):
        if event.keysym == 'Left':
            if not self.collision([0, -1]):
                self.move(0, -1)
        elif event.keysym == 'Right':
            if not self.collision([0, 1]):
                self.move(0, 1)
        elif event.keysym == 'Down':
            if not self.collision([1, 0]):
                self.move(1, 0)
        elif event.keysym == 'space':
            self.rotate()

def main():
    root = tk.Tk()
    game = Tetris(root)
    game.draw()
    root.bind("<KeyPress>", game.on_key_press)
    root.after(1000, game.tick)
    root.mainloop()

if __name__ == "__main__":
    main()