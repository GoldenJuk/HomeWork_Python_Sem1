#coding:cp1251
#�������� ���������, ������� ��������� �� ���� ���������� ���� ����� 
#� ������� ���������� ����� ���� � 2D ������������.

#������:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

def Get_Distance(coord):
    result = ((coord[2] - coord[0])**2 + (coord[3] - coord[1])**2)**0.5
    return result    

letters = ['X1','Y1','X2','Y2']
coord_list = []
for i in range(len(letters)):
    coord_list.append(float(input(f'������� ���������� {letters[i]}: ')))

distance = Get_Distance(coord_list)
print(f'���������� ����� ������� �({coord_list[0]}, {coord_list[1]}) � B({coord_list[2]}, {coord_list[3]})  = ', '{:.2f}'.format(distance))
