import random
from tkinter import *
import math


def Visual1(n, array):

    def b1(event):
        x = event.x
        y = event.y
        ind = 0
        while RedLine:
            element = RedLine.pop(0)
            c.itemconfig(element, fill='white')
        while ind < n:

            if X[ind] + 10 >= x and x >= X[ind]:
                if Y[ind] + 10 >= y and y >= Y[ind]:
                    root.title(f"координаты {x}, {y}")
                    j = 0
                    while j < n:
                        if Line[ind][j] != 0:
                            c.itemconfig(Line[ind][j], fill='red')
                            RedLine.append(Line[ind][j])
                        if Line[j][ind] != 0:
                            c.itemconfig(Line[j][ind], fill='red')
                            RedLine.append(Line[j][ind])
                        j += 1
                    ind = n
            ind += 1

    root = Tk()

    c = Canvas(root, width="2048", heigh="1024")  # Создаю окно
    c.pack()

    i = 0
    centerX = 700.0  # Вершины будут расположены в форме правильного n-угольника
    centerY = 370.0  # Для этого задаю координаты центра окружности в которую впсиан многоугольник
    radius = 10*n  # Расстояние на которое вершина удалена от центра
    angel = 2 * math.pi / n  # Угол между двумя смежными вершинами
    X = []
    Y = []
    while i < n:
        x = centerX + radius * math.sin(i * angel)  # Координата новой вершины по x
        y = centerY + radius * math.cos(i * angel)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину
        c.create_text(x + 15, y - 2, text=f"{i + 1}")  # Подписываем её
        i += 1

    A = []
    Line = []
    i = 0
    while i < n:
        l = [0] * n
        Line.append(l)
        i += 1
    i = 0
    while i < n:
        a = array[i]
        A.append(a)
        l = len(a)  # Узнаём степень i-й вершины
        j = 0
        while j < l:
            if (a[j] > (i + 1)):  # чтобы не рисовать дважды одно ребро, проверяем не было ли оно уже нарисовано
                line_id = c.create_line(X[i] + 5, Y[i] + 5, X[a[j] - 1] + 5,
                                        Y[a[j] - 1] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
                Line[i][a[j] - 1] = line_id
            j += 1
        i += 1
    RedLine = []
    root.bind('<Button-1>', b1)

    root.mainloop()

def Visual2(n, array):

    def b1(event):
        x = event.x
        y = event.y
        ind = 0
        while RedLine:
            element = RedLine.pop(0)
            c.itemconfig(element, fill='white')
        while ind < n:

            if X[ind] + 10 >= x and x >= X[ind]:
                if Y[ind] + 10 >= y and y >= Y[ind]:
                    root.title(f"координаты {x}, {y}")
                    j = 0
                    while j < n:
                        if Line[ind][j] != 0:
                            c.itemconfig(Line[ind][j], fill='red')
                            RedLine.append(Line[ind][j])
                        if Line[j][ind] != 0:
                            c.itemconfig(Line[j][ind], fill='red')
                            RedLine.append(Line[j][ind])
                        j += 1
                    ind = n
            ind += 1

    root = Tk()

    c = Canvas(root, width="2048", heigh="1024")  # Создаю окно
    c.pack()

    i = 0
    X = []
    Y = []
    while i < n:
        x = random.randint(10,1330) # Координата новой вершины по x
        y = random.randint(10,770)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину
        c.create_text(x + 15, y - 2, text=f"{i + 1}")  # Подписываем её
        i += 1

    A = []
    Line = []
    i = 0
    while i < n:
        l = [0] * n
        Line.append(l)
        i += 1
    i = 0
    while i < n:
        a = array[i]
        A.append(a)
        l = len(a)  # Узнаём степень i-й вершины
        j = 0
        while j < l:
            if (a[j] > (i + 1)):  # чтобы не рисовать дважды одно ребро, проверяем не было ли оно уже нарисовано
                line_id = c.create_line(X[i] + 5, Y[i] + 5, X[a[j] - 1] + 5,
                                        Y[a[j] - 1] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
                Line[i][a[j] - 1] = line_id
            j += 1
        i += 1
    RedLine = []
    root.bind('<Button-1>', b1)

    root.mainloop()

def Visual5(n, array):
    root = Tk()

    c = Canvas(root, width="2048", heigh="1024")  # Создаю окно
    c.pack()
    i = 0
    centerX = 700.0  # Вершины будут расположены в форме правильного n-угольника
    centerY = 370.0  # Для этого задаю координаты центра окружности в которую впсиан многоугольник
    radius = 10 * n  # Расстояние на которое вершина удалена от центра
    angel = 2 * math.pi / n  # Угол между двумя смежными вершинами
    X = []
    Y = []
    while i < n:
        x = centerX + radius * math.sin(i * angel)  # Координата новой вершины по x
        y = centerY + radius * math.cos(i * angel)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину
        if (i < n / 4):
            c.create_text(x + 20, y + 20, text=f"{i + 1}")
        elif (i < n / 2):
            c.create_text(x + 30, y + 2, text=f"{i + 1}")
        elif (i < 3 * n / 4):
            c.create_text(x - 15, y - 9, text=f"{i + 1}")
        else:
            c.create_text(x - 20, y + 10, text=f"{i + 1}")
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < n:
            if array[i][j] > 0:
                c.create_line(X[i] + 5, Y[i] + 5, X[j] + 5,
                              Y[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с
                if X[i] - X[j] != 0:
                    c.create_text((X[i] + X[j]) / 2, (Y[i] + Y[j]) / 2 - 5, text=f"{array[i][j]}", angle=(math.degrees(math.atan((Y[i] - Y[j]) / (X[i] - X[j])) * -1)))
                else:
                    c.create_text((X[i] + X[j]) / 2, (Y[i] + Y[j]) / 2 - 5, text=f"{array[i][j]}")
            j += 1
        i += 1

    root.mainloop()

def Visual52(n, array):
    root = Tk()

    c = Canvas(root, width="2048", heigh="1024")  # Создаю окно
    c.pack()
    i = 0

    X = []
    Y = []
    while i < n:
        x = random.randint(10, 1330)  # Координата новой вершины по x
        y = random.randint(10, 770)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину
        c.create_text(x + 20, y + 20, text=f"{i + 1}")
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < n:
            if array[i][j] > 0:
                c.create_line(X[i] + 5, Y[i] + 5, X[j] + 5,
                              Y[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с
                if X[i] - X[j] != 0:
                    c.create_text((X[i] + X[j]) / 2, (Y[i] + Y[j]) / 2 - 5, text=f"{array[i][j]}",
                                  angle=(math.degrees(math.atan((Y[i] - Y[j]) / (X[i] - X[j])) * -1)))
                else:
                    c.create_text((X[i] + X[j]) / 2, (Y[i] + Y[j]) / 2 - 5, text=f"{array[i][j]}")
            j += 1
        i += 1

    root.mainloop()
print("Эта программ генерирует графы по заданым параметрам \n"
      "Введите: \n"
      "1 Если хотите сделать неориентированный граф \n"
      "2 Если хотите сделать ориентированный граф \n")
orientir = int(input())
print("Какой граф вы хотите сделать? Введите соответствующую цифру \n"
      "1 Двудольный граф\n"
      "2 Эйлеров граф\n"
      "3 Регулярный граф\n"
      "4 Гамильтонов граф\n"
      "5 Взвешенный граф\n"
      "6 Граф дерево\n"
      "7 Произвольный граф\n")
graf = int(input())
print("Как расположить вершины?\n"
      "1 В форме правильного n-угольника\n"
      "2 Произвольно")
vid = int(input())
print("Сколько вершин будет в вашем графе?")
V = int(input())

if graf == 5:
    print("Какой максимальный вес ребра?")
    M = int(input())
    A = []
    i = 0
    while i < V:
        a = [0]*V
        A.append(a)
        i += 1
    i = 0
    while i < V:
        j = i
        while j < V:
            tmp = random.randint(-1, M)
            A[i][j] = tmp
            A[j][i] = tmp
            j += 1
        i += 1
    if vid == 1:
        Visual5(V, A)
    else:
        Visual52(V, A)


if graf == 7:
    A = []
    i = 0
    while i < V:
        a = [0]*V
        A.append(a)
        i += 1
    i = 0
    while i < V:
        j = i
        while j < V:
            tmp = random.randint(0, 1)
            A[i][j] = tmp
            A[j][i] = tmp
            j += 1
        i += 1
    B = []
    i = 0
    while i < V:
        j = 0
        B.append([])
        while j < V:
            if A[i][j] == 1:
                B[i].append(j + 1)
            j += 1
        i += 1
    print(B)
    if vid == 1:
        Visual1(V, B)
    else:
        Visual2(V, B)