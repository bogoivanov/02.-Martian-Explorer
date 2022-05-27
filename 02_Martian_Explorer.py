from collections import deque


def move_up(ma, r, c):
    r = r - 1
    if r < 0:
        r = len(ma) - 1
    return r, c


def move_down(ma, r, c):
    r = r + 1
    if r >= len(ma):
        r = 0
    return r, c


def move_left(ma, r, c):
    c = c - 1
    if c < 0:
        c = len(ma) - 1
    return r, c


def move_right(ma, r, c):
    c = c + 1
    if c >= len(ma):
        c = 0
    return r, c


size = 6
rover_row = 0
rover_col = 0
matrix = []
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == "E":
            rover_row = row
            rover_col = col

commands = deque(input().split(", "))

deposits = {"Water": 0, "Metal": 0, "Concrete": 0}

while commands:
    command = commands[0]
    commands.popleft()
    if command == "up":
        next_row, next_col = move_up(matrix, rover_row, rover_col)
    elif command == "down":
        next_row, next_col = move_down(matrix, rover_row, rover_col)
    elif command == "left":
        next_row, next_col = move_left(matrix, rover_row, rover_col)
    elif command == "right":
        next_row, next_col = move_right(matrix, rover_row, rover_col)

    matrix[rover_row][rover_col] = "-"
    rover_row, rover_col = next_row, next_col
    if matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    elif matrix[next_row][next_col] == "W":
        print(f"Water deposit found at ({next_row}, {next_col})")
        deposits["Water"] += 1
        matrix[next_row][next_col] = "E"
    elif matrix[next_row][next_col] == "M":
        print(f"Metal deposit found at ({next_row}, {next_col})")
        deposits["Metal"] += 1
        matrix[next_row][next_col] = "E"
    elif matrix[next_row][next_col] == "C":
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        deposits["Concrete"] += 1
        matrix[next_row][next_col] = "E"
    else:
        matrix[next_row][next_col] = "E"
count = 0
for k, v in deposits.items():
    if v > 0:
        count += 1

if count == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
