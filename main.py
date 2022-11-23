# create the tables
def turn_into_list():
    data = []
    try:
        with open('tables.txt', 'r') as file:
            for row in file:
                if not row.strip():
                    continue
                else:
                    row = [int(x) for x in row.split()]
                    data.append(row)
    except Exception as e:
        print(e)

    # Turn every fifth list into a list
    K = 5
    res = []
    subl = []
    cnt = 0
    for sub in data:
        subl.append(sub)
        cnt = cnt + 1
        if cnt >= K:
            res.append(subl)
            subl = []
            cnt = 0

    return res


tables = turn_into_list()
numbers_to_draw = [
     1, 76, 38, 96, 62, 41, 27, 33, 4, 2, 94, 15, 89, 25, 66, 14, 30, 0, 71,
     21, 48, 44, 87, 73, 60, 50, 77, 45, 29, 18, 5, 99, 65, 16, 93, 95, 37,
     3, 52, 32, 46, 80, 98, 63, 92, 24, 35, 55, 12, 81, 51, 17, 70, 78, 61,
     91, 54, 8, 72, 40, 74, 68, 75, 67, 39, 64, 10, 53, 9, 31, 6, 7, 47, 42,
     90, 20, 19, 36, 22, 43, 58, 28, 79, 86, 57, 49, 83, 84, 97, 11, 85, 26,
     69, 23, 59, 82, 88, 34, 56, 13]
winner_tables = []
win = False


# Check for horizontal win i.e 5 marked numbers in a row
def check_for_horizontal_win(table, last_draw_num):
    global win
    five_x = ['x', 'x', 'x', 'x', 'x']
    for row in table:
        if row == five_x:
            sum = calculate_score(table)
            score = sum * last_draw_num
            winner_tables.append(score)
            win = True


# Check for vertical win i.e 5 marked numbers in a coulmn
def check_for_vertical_win(table, last_draw_num):
    global win
    five_x = ['x', 'x', 'x', 'x', 'x']
    for i in range(5):
        vertical_sqaures = []
        for j in range(5):
            vertical_sqaures.append(table[j][i])
        if vertical_sqaures == five_x:
            sum = calculate_score(table)
            score = sum * last_draw_num
            winner_tables.append(score)
            win = True


# Calculate the score sum of all unmarked numbers
def calculate_score(table):
    unbolded_num = []

    for i in range(5):
        for j in range(5):
            if table[i][j] != 'x':
                unbolded_num.append(table[i][j])
    return sum(unbolded_num)


def bingo(table):
    if len(numbers_to_draw) == 0:
        this_turns_number = [0]
    this_turns_number = numbers_to_draw[0]
    numbers_to_draw.remove(this_turns_number)

    for i in range(5):
        for j in range(5):
            if table[i][j] == this_turns_number:
                table[i][j] = 'x'

    check_for_horizontal_win(table, this_turns_number)
    check_for_vertical_win(table, this_turns_number)


for table in tables:
    win = False
    numbers_to_draw = numbers_to_draw = [
     1, 76, 38, 96, 62, 41, 27, 33, 4, 2, 94, 15, 89, 25, 66, 14, 30, 0, 71,
     21, 48, 44, 87, 73, 60, 50, 77, 45, 29, 18, 5, 99, 65, 16, 93, 95, 37,
     3, 52, 32, 46, 80, 98, 63, 92, 24, 35, 55, 12, 81, 51, 17, 70, 78, 61,
     91, 54, 8, 72, 40, 74, 68, 75, 67, 39, 64, 10, 53, 9, 31, 6, 7, 47, 42,
     90, 20, 19, 36, 22, 43, 58, 28, 79, 86, 57, 49, 83, 84, 97, 11, 85, 26,
     69, 23, 59, 82, 88, 34, 56, 13]
    while not win:
        bingo(table)

print(f'Last Winner tabel: {min(winner_tables)}')
