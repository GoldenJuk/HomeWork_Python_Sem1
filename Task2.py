# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

letters = ['X','Y','Z']
xyz = []
for i in range(3):
    xyz.append(input(f'Введите {letters[i]}: '))

if not(xyz[0] or xyz[1] or xyz[2]) == (not(xyz[0]) and not(xyz[1]) and not(xyz[1])):
    print('Утверждение истинно')
