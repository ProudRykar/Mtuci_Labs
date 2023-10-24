import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = ((b**2) - (4*a*c))

if D > 0:
    x1 = ((-b + math.sqrt(D)) / (2*a))
    x2 = ((-b - math.sqrt(D)) / (2*a))
    print(f"Уравнение имеет два корня: x1 = {round(x1,4)}, x2 = {round(x2,4)}")
elif D == 0:
    x = -b / (2*a)
    print(f"Уравнение имеет один корень: x = {round(x,4)}")
else:
    print('Уравнение не имеет корней')