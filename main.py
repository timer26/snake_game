import time
import keyboard
import sys
vector = [0, -1] #inicial vector




print("welcome to snake CMD game")


def resolution_handler(num: int) -> int:
    return num if num % 2 != 0 else num + 1

def border_generator(res_x: int, res_y: int) -> str:
    screen = []
    for y in range(res_y):
        temp_list = []
        for x in range(res_x):
            # Generate top and bottom border
            if y == 0 or y == res_y - 1:
                temp_list.append("+") if x == 0 or x == res_x - 1 else temp_list.append("---")
            # Generate side borders
            elif x == 0 or x == res_x - 1:
                temp_list.append("|")
            # Generate field
            else:
                temp_list.append("   ")
        screen.append(temp_list)

    return screen

def refresh_screen ():
    sys.stdout.write("\033c")
    sys.stdout.flush()


# emit vector and current position
def get_vector(vector: list, current_x: int, current_y: int)->list:

    # read input and execute
    p_input = keyboard.read_event().name
    # decide resulting vector
    # need 180 prevention <-------------------------
    if p_input == "w":
        vector = [0, -1]
    elif p_input == "a":
        vector = [-1, 0]
    elif p_input == "s":
        vector = [0, 1]
    elif p_input == "d":
        vector = [1, 0]
    else:
        vector = vector

    current_x += vector[0]
    current_y += vector[1]

    return [vector, [current_x, current_y]]





def snake(vector: list):
    snake_body_sprite = "⦾"

    # calculate snake head sprite
    if vector == [0, -1]:            # looking up pressing w
        snake_head_sprite = " ▲ "
    elif vector == [-1, 0]:            # looking left pressing a
        snake_head_sprite = " < "
    elif vector == [0, 1]:            # looking down pressing s
        snake_head_sprite = " ▼ "
    elif vector == [1, 0]:            # looking right pressing d
        snake_head_sprite = " > "

    return snake_head_sprite

res_x = resolution_handler(int(input("Insert width: ")))
res_y = resolution_handler(int(input("Insert height: ")))
current_x = res_x//2
current_y = res_y//2


while True:
    skeleton = get_vector(vector, current_y, current_x)
    current_x = skeleton[1][0]
    current_y = skeleton[1][1]
    vector = skeleton[0]
    print(current_x)
    print(current_y)
    print(vector)

    #border limit checker --> placeholder
    if current_x <= 0:
        current_x = 1
    elif current_x >= res_x - 1:
        current_x = res_x - 2
    if current_y <= 0:
        current_y = 1
    elif current_y >= res_y - 1:
        current_y = res_y - 2

    snake_render = snake(vector)
    arena = border_generator(res_x, res_y)
    arena[current_y][current_x] = snake_render
    for x in arena:
        print("".join(x))
    time.sleep(0.3)
    print("--------------------------------")
    refresh_screen()
# while True:
#     skeleton = get_vector(vector, current_y, current_x)
#     current_x = skeleton[1][0]
#     current_y = skeleton [1][1]
#     vector = skeleton [1]
#
#     display = snake(res_x, res_y, currdent_x,current_y)
#     for x in display:
#         print("".join(x))
#     vector = get_vector(vector)
#     time.sleep(0.2)