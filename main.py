
import keyboard
vector = [0, -1]
fps = 1

print("welcome to snake CMD game")


def resolution_handler(num: int) -> int:
    return num if num % 2 != 0 else num + 1

def border_gene(res_x: int, res_y: int) -> str:
    screen = []
    for y in range(res_y):
        # Generate top and bottom border
        if y == 0 or y == res_y - 1:
            screen.append("+" + "---" * res_x + "+")
        # Generate side borders and playing field
        else:
            screen.append("|" + "   " * res_x + "|")
    return"\n".join(screen)



def get_vector(vector: list)->list:

    # read input and execute
    p_input = keyboard.read_event().name
    # decide resulting vector
    if p_input == "w":
        vector = [0, 1]
    elif p_input == "a":
        vector = [-1, 0]
    elif p_input == "s":
        vector = [0, -1]
    elif p_input == "d":
        vector = [1, 0]
    else:
        vector = vector

    return vector


def snake(res_x: int, res_y: int, vector: list)-> list:
    snake_pos = (res_x * res_y)//2
    blanc_canvas = border_gene(res_x,res_y)

    snake_body_sprite = "⦾"

    # calculate snake head sprite
    if vector == [0, 1]:            # looking up pressing w
        snake_head_sprite = "▲"
    elif vector == [-1, 0]:            # looking left pressing a
        snake_head_sprite = "<"
    elif vector == [0, -1]:            # looking down pressing s
        snake_head_sprite = "▼"
    elif vector == [1, 0]:            # looking right pressing d
        snake_head_sprite = ">"
    # blanc_canvas[3][3] = snake_head_sprite
    # for x in blanc_canvas:
    #     print(x)
    print(snake_head_sprite)


res_x = resolution_handler(int(input("Insert width: ")))
res_y = resolution_handler(int(input("Insert height: ")))


while True:
    print(border_gene(res_x, res_y))
    vector = get_vector(vector)
    snake(res_x,res_y,vector)
