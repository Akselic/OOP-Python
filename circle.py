import math


while True:

    print('Инструкция. Я могу посчитать площадь круга, периметр или определить, находится ли точка внутри заданной\n' 
    'окружности. Чтобы найти площадь круга, введите площадь. Чтобы найти периметр окружности, введите периметр. \n'
    'Чтобы проверить, находится ли точка внутри заданной окружности, введите точка. Чтобы остановить программу, \n'
    'введите стоп.')

    a = input('Введите требуемое слово  \n')

    class Circle:

        def __init__(self, x_center = 0, y_center = 0, radius = 0, area = 0, perimetr = 0):
            self.x_center = x_center
            self.y_center = y_center
            self.radius = radius
            self.area = area
            self.perimetr = perimetr


        def getcenter(self):
            r = int(input('Введите радиус = '))
            print('Введите координаты центра окружности')
            a = float(input('x = '))
            b = float(input('y = '))

            print('Введите координаты точки')
            x = float(input('x = '))
            y = float(input('y = '))
            if math.sqrt(x - a) + math.sqrt(y - b) <= math.sqrt(r):
                return print('Эта точка внутри окружности')
            else:
                return print('Эта точка не внутри окружности')

        def getarea(self):

            print('введите радиус окружности')
            radius = float(input('радиус = '))

            return print(math.pi * radius ** 2)

        def getperimetr(self):

            print('Введите радиус окружности')
            radius = float(input('Радиус = '))

            return print(2 * radius * math.pi)



    cir = Circle()
    if 'площадь' in a:

        cir.getarea()

    elif 'периметр' in a:
        cir.getperimetr()

    elif 'точка' in a:

        cir.getcenter()

    elif 'стоп' in a:
        break

    else:
        print('Я вас не понимаю. Повторите ввод')









