def draw_custom_triangle(height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print('* ' * i)
        else:
            print('*  ' + ' ' * (2 * (i - 2)) + '*')

height = int(input("Nhập chiều cao của tam giác: "))
draw_custom_triangle(height)