import math

print('[ 1 ] Prism')
print('[ 2 ] Cylinder')

choice = int(input('Which shape do you want to calculate the volume of?: '))

if choice == 1:
    print('[ 1 ] Triangle')
    print('[ 2 ] Square')
    print('[ 3 ] Trapezoid')
    base_choice = int(input('What is the base type of the prism?: '))

    if base_choice == 1:
        base = float(input('Enter the base length of the triangle: '))
        height = float(input('Enter the height of the triangle: '))
        prism_height = float(input('Enter the height of the prism: '))
        area_base = base * height / 2
        result = area_base * prism_height
        print(f'The volume of the TRIANGULAR PRISM is: {result:.2f}')

    elif base_choice == 2:
        side1 = float(input('Enter the length of the first side: '))
        side2 = float(input('Enter the length of the second side: '))
        prism_height = float(input('Enter the height of the prism: '))
        area_base = side1 * side2
        result = area_base * prism_height
        print(f'The volume of the SQUARE PRISM is: {result:.2f}')

    elif base_choice == 3:
        base_small = float(input('Enter the smaller base of the trapezoid: '))
        base_large = float(input('Enter the larger base of the trapezoid: '))
        trapezoid_height = float(input('Enter the height of the trapezoid: '))
        prism_height = float(input('Enter the height of the prism: '))
        area_base = (base_small + base_large) * trapezoid_height / 2
        result = area_base * prism_height
        print(f'The volume of the TRAPEZOIDAL PRISM is: {result:.2f}')

    else:
        print('Please select a valid base type.')

elif choice == 2:
    radius = float(input('Enter the radius of the base: '))
    height = float(input('Enter the height of the cylinder: '))
    area_base = math.pi * radius ** 2
    result = area_base * height
    print(f'The volume of the CYLINDER is: {result:.2f}')

else:
    print('Please select a valid option.')