x, y, x_1, y_1, A, B, C, K = map(int, input().split())

maze = [['#' for _ in range(2*K+3)] for _ in range(2*K+3)]

total_time = 0

game = True
know = False

side = 1

visited = [(x, y)]
need_to_visit = []

#описание функции просмотра лабиринта
def look():
    print(3)
    for i in range (2 * K + 1):
        line = input().split()
        for j in range (2 * K + 1):
            maze[i+1][j+1] = line[j]

#функция вычисляющая всех соседей возможных для посещения
def analys():
    if ((maze[x-1][y-1] == '_') and not((x-1, y-1) in visited)):
        need_to_visit.append((x-1, y-1))
    if maze[x+1][y-1] == '_' and not((x+1, y-1) in visited):
        need_to_visit.append((x+1, y-1))
    if maze[x+1][y+1] == '_' and not((x+1, y+1) in visited):
        need_to_visit.append((x+1, y+1))
    if maze[x-1][y+1] == '_' and not((x-1, y+1) in visited):
        need_to_visit.append((x-1, y+1))

#функция проверки необходимого колличества поворотов для посешения следующего соседа   
def rotate(x, y, a, b, x_1, y_1):
    answer = 0
    first = abs(a - x_1)
    second = abs(b - y_1)
    if first == 2 or second == 2:
        answer = 2
    elif first == 0:
        answer = -1
    elif x == x_1 and y - y_1 == 1:
        answer = 0
    elif x == x_1 and y - y_1 == -1:
        answer = -1
    elif y == y_1 and x - x_1 == 1:
        answer = 0
    elif y == y_1 and x - x_1 == -1:
        answer = -1
    return answer

#функция посщения всех доступных соседей
def visit():
    for (a, b) in need_to_visit:
        need = rotate(x, y, a, b, x_1, y_1)
        if need == -1:
            print (1)
            total_time = total_time + A
            answer = int(input())
            if answer == 1:
                visited.append((a, b))
                need_to_visit.remove((a, b))
            print("2, 1")
            print("2, 1")
            total_time = total_time + 2 * B
            print (1)
            total_time = total_time + A 
        elif (need == 2):
            print("2, 1")
            print("2, 1")
            total_time = total_time + 2 * B
            print (1)
            total_time = total_time + A
            answer = int(input())
            if answer == 1:
                visited.append((a, b))
                need_to_visit.remove((a, b))
            print("2, 1")
            print("2, 1")
            total_time = total_time + 2 * B
            print (1)
            total_time = total_time + A 
        elif need == 1:
            print("2, 1")
            total_time = total_time + B
            print (1)
            total_time = total_time + A
            answer = int(input())
            if answer == 1:
                visited.append((a, b))
                need_to_visit.remove((a, b))
            print("2, 1")
            print("2, 1")
            total_time = total_time + 2 * B
            print (1)
            total_time = total_time + A 
        else:
            print("2, 0")
            total_time = total_time + B
            print (1)
            total_time = total_time + A
            answer = int(input())
            if answer == 1:
                visited.append((a, b))
                need_to_visit.remove((a, b))
            print("2, 1")
            print("2, 1")
            total_time = total_time + 2 * B
            print (1)
            total_time = total_time + A    
        



look()
analys()
visit()
# на данный момент проверили всех соседей исходной клетки

#фунция для посещения всех еще не пройденных соседей уже посещенных вершин
for (c, d) in visited:
    x = c
    y = d
    x_1 = c
    y_1 = d
    analys()
    visit()

print (4, total_time)
