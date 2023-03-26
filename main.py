#this code is written by Adham Tarek

from math import *
import random
import curses

# intialize the screen and curses library
screen = curses.initscr()

# remove the cursor
curses.curs_set(0)

# get max height and max width of the screen
screen_height, screen_width = screen.getmaxyx()

# make the window with max height and max width of the screen
window = curses.newwin(screen_height, screen_width, 0, 0)

# make the window accept input from the user
window.keypad(1)

# make the window delays every 100 ms to update the screen
window.timeout(125)

# set the initial position of the snake
snk_height = screen_height // 2
snk_width = screen_width // 4

# design the initial snake poistion by lists
snake = [
    [snk_height, snk_width],
    [snk_height, snk_width - 1],
    [snk_height, snk_width - 2]
]

# design the initial food poistion by list
food = [screen_height // 2, screen_width // 2]

# let the food appear at the shape of (PI)
window.addch(food[0], food[1], curses.ACS_PI)

# set the initial direction of snake to the right
key = curses.KEY_RIGHT




# infinite loop to run the game
while True:
    # get the next input from the user to move the snake
    next_key = window.getch()
    # check the next key
    if next_key == -1:
        key = key
    else:
        key = next_key

    # make a new head for the movement the user make
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_DOWN:
        new_head[0] += 1

    # update the snake head position
    snake.insert(0, new_head)

    # if the snake head crashes in any wall or the head crashes in the body and the tail
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # generate new food position if the snake eat the food and get bigger if it eats the food
    if snake[0] == food:
        food = None
        while food is None:
          new_food=[random.randint(1,screen_height-1),
                    random.randint(1,screen_width-1)]
          if new_food not in snake:
            food = new_food
          else:
            food = None

        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    #add the shape to the snake
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

