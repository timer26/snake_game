import os
import time
import keyboard
import sys, subprocess
import random

vector = [0, 0]  # initial movement direction
p_input = None # initial input

print("Welcome to Snake CMD Game")

def resolution_handler(num: int) -> int:
    return num if num % 2 != 0 else num + 1

def border_generator(res_x: int, res_y: int)-> list:
    screen = []
    for y in range(res_y):
        temp_list = []
        for x in range(res_x):
            # generate top and bottom border
            if y == 0 or y == res_y - 1:
                temp_list.append("+") if x == 0 or x == res_x - 1 else temp_list.append("---")
            # generate side borders
            elif x == 0 or x == res_x - 1:
                temp_list.append("|")
            # generate field
            else:
                temp_list.append("   ")
        screen.append(temp_list)
    return screen

def refresh_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# get movement vector and position
def get_vector(vector: list, current_x: int, current_y: int, p_input)-> list:

    # decide resulting vector
    if p_input == "w" and vector != [0, 1]:
        vector = [0, -1]
        current_y -= 1
    elif p_input == "a" and vector != [1, 0]:
        vector = [-1, 0]
        current_x -= 1
    elif p_input == "s" and vector != [0, -1]:
        vector = [0, 1]
        current_y += 1
    elif p_input == "d" and vector != [-1, 0]:
        vector = [1, 0]
        current_x += 1
    return [vector, [current_x, current_y]]

def snake_head(vector: list)-> str:

    # orient snake head sprite
    if vector == [0, -1]:  # moving up
        return " ▲ "
    elif vector == [-1, 0]:  # moving left
        return " < "
    elif vector == [0, 1]:  # moving down
        return " ▼ "
    elif vector == [1, 0]:  # moving right
        return " > "
    else:                   # idle
        return " @ "

def snake_body_generator(snake_head_vector_position: list, snake_body_value: list) -> list:
    snake_body_value.append(snake_head_vector_position[1])  # add body
    return snake_body_value


def snake_body(snake_head_vector_position: list, snake_body_value: list) -> list:
    if not snake_body_value:
        return []

    new_body = [snake_head_vector_position[1]]  # new head position
    for i in range(len(snake_body_value) - 1):
        new_body.append(snake_body_value[i])  # move each segment forward

    return new_body

def fruit_generator(arena: list, fruits: set) -> set:
    fruit_sprite = " © "
    # scan for possible placement
    empty_positions = []
    for y in range(len(arena)):
        for x in range(len(arena[y])):
            if arena[x][y] == "   ":
                empty_positions.append((y, x))

    if empty_positions:
        y, x = random.choice(empty_positions)
        fruits.add((x, y))  # hold fruit positions with coordinate correction

    return fruits

def colision_check(snake_head_position: list, fruits: set)-> bool:
    return tuple(snake_head_position[1]) in fruits

res_x = resolution_handler(int(input("Insert width: ")))
res_y = resolution_handler(int(input("Insert height: ")))

# start in the center of the arena
current_x = res_x // 2
current_y = res_y // 2
maximum_fruits = 8
total_empty_space = ((res_x - 2) * (res_y - 2)) // 2
fruits = set()
snake_body_value = []
score = 0

while True:
    time.sleep(0.1)
    # get new position and vector
    snake_head_vector_position = get_vector(vector, current_x, current_y, p_input)        # main source of data for other function      
    refresh_screen()
    vector = snake_head_vector_position[0]  
    current_y = snake_head_vector_position[1][1]
    current_x = snake_head_vector_position[1][0]

    # prevent movement outside the border
    if current_x <= 0:
        current_x = 1
    elif current_x >= res_x - 1:
        current_x = res_x - 2
    if current_y <= 0:
        current_y = 1
    elif current_y >= res_y - 1:
        current_y = res_y - 2

    # print arena with snake
    arena = border_generator(res_x, res_y)
    snake_render = snake_head(vector)
    arena[current_y][current_x] = snake_render

    # insert previous fruit positions
    for x, y in fruits:
        arena[y][x] = " © "

    if maximum_fruits <= 9 and total_empty_space >= total_empty_space * 0.7:
        while maximum_fruits > 0:
            fruits = fruit_generator(arena, fruits)
            maximum_fruits -= 1
    if maximum_fruits <= 6 and total_empty_space >= total_empty_space * 0.5:
        while maximum_fruits > 0:
            fruits = fruit_generator(arena, fruits)
            maximum_fruits -= 1
    if maximum_fruits <= 2 and total_empty_space >= total_empty_space * 0.15:
        while maximum_fruits > 0:
            fruits = fruit_generator(snake_head_vector_position, fruits)
            maximum_fruits -= 1

    if colision_check(snake_head_vector_position, fruits):
        maximum_fruits += 1
        fruits.remove(tuple(snake_head_vector_position[1]))
        score += 1
        snake_body_value = snake_body_generator(snake_head_vector_position, snake_body_value)  #current vector current_x and current_y
    else:
        pass

    snake_body_value = snake_body(snake_head_vector_position, snake_body_value)

    if not snake_body_value:
        pass
    else:
        for x, y in snake_body_value:
            arena[y][x] = " 0 "

    print(maximum_fruits)
    print(current_x, current_y)
    print(fruits)
    print(snake_body_value)
    print("SCORE: ", score)
    for row in arena:
        print("".join(row))

    p_input = keyboard.read_event().name
