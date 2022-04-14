# Вывод текста в графическое окно
# Для вывода текста в графическое окно применяется команда write(). Аргумент этой команды — строка текста, которую
# требуется вывести на экран. Левый нижний угол первого символа выведенного текста будет расположен в точке с
# координатами черепашки.
import turtle
turtle.write('Пpивeт, мир!')

# Приведенный ниже код показывает, как черепаха перемещается в соответствующие позиции для вывода текста:
import turtle
turtle.Screen().setup(400, 300)
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху')
turtle.goto(50, -120)
turtle.write('Снизу')
turtle.goto(100, 20)
turtle.write('Справа')

# Мы можем настроить вывод текста, задавая размер и тип шрифта, начертание, выравнивание и т.д.
# Аргументы команды write():
#     arg – текст, который нужно вывести;
#     move – указывает будет ли двигаться черепашка по мере рисования надписи (по умолчанию значение False);
#     align – служит для выравнивания надписи относительно черепашки, может принимать три строковых значения right,
#       center, left (по умолчанию значению right);
#     font – кортеж из трех значений: (название шрифта, размер шрифта, тип начертания). В качестве начертания можно
#       использовать строковые значения: normal — обычный, bold — полужирный, italic — курсив, или объединить два
#       последних, тогда текст будет напечатан полужирным курсивом.


# Заполнение геометрических фигур
# Для заполнения геометрической фигуры цветом используется команда turtle.begin_fill(), причем она применяется до
# начертания фигуры, а после завершения начертания используется команда turtle.end_fill() и геометрическая фигура
# заполняется текущим цветом заливки.
import turtle
turtle.hideturtle()
turtle.begin_fill()     # включаем заливку
turtle.circle(80)
turtle.end_fill()       # выключаем заливку

# Цвет заливки можно изменить при помощи команды fillcolor(). Аргумент команды — название цвета в виде строкового
# литерала, либо значения трех компонентов RGB.
import turtle
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# Приведенный ниже код рисует квадрат, заполненный зеленым цветом.
import turtle
turtle.hideturtle()
turtle.fillcolor('green')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# Если заполнить незамкнутую фигуру, она будет закрашена, будто был начерчен отрезок, соединяющий начальную и конечную
# точки.
import turtle
turtle.hideturtle()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(-50, 120)
turtle.goto(120, 120)
turtle.goto(150, -80)
turtle.end_fill()


# Создание нескольких черепашек
# Можно работать сразу с несколькими черепашками. Для этого надо создать несколько переменных, содержащих экземпляры
# класса Turtle.
import turtle
turtle.Screen().bgcolor('yellow')  # устанавливаем цвет фона
tim = turtle.Turtle()    # создаем первую черепашку и устанавливаем ее свойства
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)
alex = turtle.Turtle()    # создаем вторую черепашку и устанавливаем ее свойства
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

# Черепашек можно сохранить в списке, а затем в цикле обрабатывать его.
import turtle
from random import randrange
def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)
turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turt.tracer(25, 0)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles
for i in range(70):
    move_turtles(turtles, 10, i)

# Команда turtle.tracer(n, delay) включает/выключает анимацию черепашки и устанавливает задержку для обновления
# рисунков. Может использоваться для ускорения рисования сложной графики.


# Отслеживание нажатия клавиш
# Черепашья графика позволяет отслеживать происходящие события, такие как нажатия клавиш клавиатуры, перемещение мышки
# или нажатие на мышку. Изначально программа никак не реагирует на эти события и чтобы это поведение изменить необходимо
# привязать функции обратного вызова к событиям. Для этого существуют специальные команды. Для отслеживания нажатия
# клавиш клавиатуры используется команда onkey(fun, key), которая связывает функцию обратного вызова fun с событием
# нажатия клавиши key.
import turtle
def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + 5)
def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - 5)
def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - 5, y)
def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + 5, y)
turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.shape('turtle')
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки
turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо

# Для отслеживания событий также необходимо установить фокус на экран черепашки с помощью команды turtle.Screen().listen().

# Давайте теперь сделаем так, чтобы по нажатию на пробел черепашка скрывалась и переставала оставлять след. Также
# добавим возможность увеличивать скорость перемещения черепашки по нажатию на клавиши клавиатуры q и w.
import turtle
speed = 5
def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + speed)
def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - speed)
def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - speed, y)
def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + speed, y)
def change():  # функция обратного вызова
    if turtle.isvisible():
        turtle.up()
        turtle.hideturtle()
    else:
        turtle.down()
        turtle.showturtle()
def speed_increase():  # функция обратного вызова
    global speed
    speed += 1
def speed_decrease():  # функция обратного вызова
    global speed
    speed -= 1
turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки
turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')


# Отслеживание нажатия мыши
# Аналогичным образом можно отслеживать нажатие на мышку. Для отслеживания нажатия мыши используется команда
# onclick(fun), которая связывает функцию обратного вызова fun с событием нажатия левой кнопки мыши.

# Приведенный ниже код рисует круг по нажатию на левую кнопку мыши.
import turtle
from random import randrange
def random_color():
  return randrange(256), randrange(256), randrange(256)
def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)
def left_mouse_click(x, y):
    draw_circle(x, y, 10)
turtle.hideturtle()
turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()






