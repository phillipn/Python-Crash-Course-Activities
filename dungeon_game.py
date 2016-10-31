import random
import os

COORDS = [(0,2),(1,2),(2,2),
          (0,1),(1,1),(2,1),
          (0,0),(1,0),(2,0)]

def redraw():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_coords():
    player = random.choice(COORDS)
    monster = random.choice(COORDS)
    door = random.choice(COORDS)

    if(player == monster) or (player == door) or (door == monster):
        return get_coords()
    else:
        return player, monster, door


def move_player(subject, direction):
    x, y = subject

    if direction == "LEFT":
        x-=1
    elif direction == "RIGHT":
        x+=1
    elif direction == "UP":
        y+=1
    else:
        y-=1

    return x, y

def available_moves(subject):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    if subject[0] == 0:
        moves.remove("LEFT")
    if subject[0] == 2:
        moves.remove("RIGHT")
    if subject[1] == 2:
        moves.remove("UP")
    if subject[1] == 0:
        moves.remove("DOWN")

    return moves

def draw_map(player, monster, door):
    for index, value in enumerate(COORDS):
        if index in [0,3,6]:
            if value == player:
                print('|X ', end="")
            elif value == monster:
                print('|M ', end="")
            elif value == door:
                print('|D ', end="")
            else:
                print('|_ ', end="")
        elif(index in [2,5,8]):
            if value == player:
                print(' X|')
            elif value == monster:
                print(' M|')
            elif value == door:
                print(' D|')
            else:
                print(' _|')
        else:
            if value == player:
                print('X', end="")
            elif value == monster:
                print('M', end="")
            elif value == door:
                print('D', end="")
            else:
                print('_', end="")


player, monster, door = get_coords()
while True:
    redraw()
    print("Welcome to my dungeon!")
    print("Enter DONE to leave game")
    print("Enter either LEFT, RIGHT, UP, or DOWN to move\n")
    draw_map(player, monster, door)
    player_moves = available_moves(player)
    monster_moves = available_moves(monster)

    player_direction = input("\nChoose your move ")
    player_direction = player_direction.upper()

    monster_direction = random.choice(monster_moves)

    if player_direction not in player_moves:
        continue
    else:
        player = move_player(player, player_direction)

        if random.choice(range(2)) == 0:
            monster = move_player(monster, monster_direction)

        if player == door:
            print("You WIN!")
            break
        elif player == monster:
            print("You LOSE!")
            break
