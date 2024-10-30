grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
# Список - Оценки для учеников в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Множество -
print(students)
score = {}  # Словарь Студент - оценка
my_students = list(students)
print(my_students) #перевод множества в список
print(len(my_students))
my_students.sort()
print(my_students) # список отсортирован в алфавитном порядок
#  my_studentsA = sum(grades[0])/len(grades[0]) # средний балл первого студента
#  print(my_studentsA)
#  my_studentsB = sum(grades[1])/len(grades[1]) # средний балл второго студента
#  print(my_studentsB)
#  my_studentsС = sum(grades[2])/len(grades[2]) # средний балл третьего студента
#  print(my_studentsС)
#  my_studentsD = sum(grades[3])/len(grades[3]) # средний балл четвертого студента
#  print(my_studentsD)
#  my_studentsE = sum(grades[4])/len(grades[4]) # средний балл пятого студента
#  print(my_studentsE)
score [my_students[0]] = {sum(grades[0])/len(grades[0])}
score [my_students[1]] = {sum(grades[1])/len(grades[1])}
score [my_students[2]] = {sum(grades[2])/len(grades[2])}
score [my_students[3]] = {sum(grades[3])/len(grades[3])}
score [my_students[4]] = {sum(grades[4])/len(grades[4])}
print(score)

