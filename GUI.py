import pygame
from Game import Board
from copy import deepcopy
pygame.init()
size = w, h = 550, 550
black = (0, 0, 0)
white = (211, 211, 211)
red = (255, 0, 0)

window = pygame.display.set_mode(size)
window.fill(white)
pygame.display.set_caption("Sudoku")
# pygame.draw.rect(window, black,(50,50,450,450), 2)

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

temp = deepcopy(board)
game = Board(deepcopy(board))
game.solve()

print(game)

font20 = pygame.font.Font(None, 26)
font12 = pygame.font.Font(None, 18)

for x, row in enumerate(board):
    for y, value in enumerate(row):
        if value != '.':
            text = font20.render(board[x][y], True, black, white)
            textRect = text.get_rect()
            textRect.center = ((y * 50) + 75, (x * 50) + 75)
            window.blit(text, textRect)

def generateBoard():
    for i, offset in enumerate(range(0, 500, 50)):
        if i == 3 or i == 6:
            thickness = 4
        else:
            thickness = 2
        pygame.draw.line(window, black, (50 + offset, 50), (50 + offset, 500), thickness)
        pygame.draw.line(window, black, (50, 50 + offset), (500, 50 + offset), thickness)

# pygame.draw.line(window, black, (400,100), (400,400),5)
pygame.display.update()


def select(x, y):
    pygame.draw.rect(window, red, ((y + 1) * 50 + 2, (x + 1) * 50 + 2, 47, 47), 2)

def deselect(x, y):
    pygame.draw.rect(window, white, ((y + 1) * 50 + 2, (x + 1) * 50 + 2, 48, 48), 4)
    generateBoard()

def clearCell(x, y):
    pygame.draw.rect(window, white, ((y + 1) * 50 + 2, (x + 1) * 50 + 2, 48, 48))
    generateBoard()

generateBoard()

selected = False
run = True
while run:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:

            # remove previous selection
            if selected:
                deselect(x, y)

            # get new selection
            y, x = pygame.mouse.get_pos()
            x, y = x // 50 - 1, y // 50 - 1

            # display selection
            if 0 <= x < 9 and 0 <= y < 9:
                if board[x][y] == '.':
                    select(x, y)
                    selected = True

                    print("you clicked an empty slot")
                else:
                    print(board[x][y])

            print("you clicked ", (x, y))

    if selected:
        for i, key in enumerate(keys[49:58]):
            if key:
                temp[x][y] = str(i + 1)

                clearCell(x, y)
                select(x, y)
                text = font12.render(temp[x][y], True, black)
                textRect = text.get_rect(center=((y * 50) + 63, (x * 50) + 63))
                window.blit(text, textRect)

        if keys[pygame.K_DELETE] and temp[x][y] != '.':
            clearCell(x, y)
            select(x, y)

        if keys[pygame.K_RETURN] and temp[x][y] != '.':
            if game.board[x][y] == temp[x][y]:
                clearCell(x, y)
                board[x][y] = temp[x][y]
                text = font20.render(temp[x][y], True, black, white)
                textRect = text.get_rect()
                textRect.center = ((y * 50) + 75, (x * 50) + 75)
                window.blit(text, textRect)
            else:
                print("WRONG")
    pygame.display.update()

    if keys[pygame.K_ESCAPE]:
        run = False


pygame.quit()
