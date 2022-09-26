# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3




def create_coordinate():
    coordinate = [None] * 2
    for i in range(2):
        is_false = False
        while not is_false:
            number = int(input(f"Введите координату {i+1}: "))
            if number != 0:
                coordinate[i] = number
                is_false = True
            else:
                print(f"координата {i+1} не должна быть равна нулю")
    return coordinate

def check_coordinate(points):
    quarter_plane = 4
    if points[0] > 0 and points[1] > 0:
        quarter_plane = 1
    elif points[0] < 0 and points[1] > 0:
        quarter_plane = 2
    elif points[0] < 0 and points[1] < 0:
        quarter_plane = 3
    print(f"X={points[0]}; Y={points[1]} -> {quarter_plane}")

coordinates = create_coordinate()
check_coordinate(coordinates)

