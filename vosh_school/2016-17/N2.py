# Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов.
# Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота
# имеет координаты (x1, y1), северо-восточный угол – координаты (x2, y2).
# Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или
# восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно
# плыть, чтобы как можно скорее добраться до плота


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
if x < x1:
    if y < y1:
        print('SW')
    elif y1 < y < y2:
        print('W')
    elif y2 < y:
        print('NW')
elif x1 < x < x2:
    if y2 < y:
        print('N')
    if y < y1:
        print('S')
elif x2 < x:
    if y < y1:
        print('SE')
    elif y1 < y < y2:
        print('E')
    elif y2 < y:
        print('NE')