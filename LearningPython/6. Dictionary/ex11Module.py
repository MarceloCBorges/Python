student = {}


def order():  # ordena alfabetica
    pass


def show():
    order()
    if len(student) == 0:
        print('** There is no students registered. **')
    else:
        for k in student:
            print(f'--> Student: ', k, '    Grade: ', student.get(k))


def validateGrade():
    grade = float(input('- Inform new student\'s grade: '))
    if 0 <= grade <= 10:
        return grade
    else:
        print('** Invalid value. Inform a grade between 0 and 10. **')
        validateGrade()


def insert(name):
    if name in student:
        print('** There is another student with this name. **')
        print('\nPress any key to return to menu.')
        input()
    else:
        student[name] = validateGrade()


def confirm(old, new):
    while True:
        print(f'-- Are you secure you want to make changes?\n'
              f'- Old: {old}\n'
              f'- New: {new}')

        if validate():
            return True
        else:
            return False


def validate():
    print('1. Yes\n'
          '2. No.')
    option = int(input())

    if option == 1:
        return True
    elif option == 2:
        return False
    else:
        print('** Invalid menu option. **')
        validate()


def change():
    name = input('Inform student\'s name to change the grade: ')
    if name in student:
        old_grade = student.get(name)
        new_grade = validateGrade()
        if confirm(old_grade, new_grade):
            student[name] = new_grade
            print('** Student`s grade changed. **')
        else:
            print('** Student`s grade not changed. ** \n')
    else:
        print('** Student is not in the list. **')


def consult():
    name = input('Inform student\'s name to consult: ')
    if student.get(name):
        print(f'Name  {name} \nGrade:  {student.get(name)}')
        print('\nPress any key to return to menu.')
        input()
    else:
        print(f'** Student did not exist. **')
        print(f'->Would you like to insert the student {name}?')

        if validate():
            insert(name)


def delete():
    name = input('Inform student\'s name that you want delete: ')
    if name in student:
        print(f'Are you shure you want delete the student {name}?')
        if validate():
            student.pop(name)
            print('**Student deleted successfully**')
    else:
        print('Student not found in list.')
        print(f'Would you like to insert the student {name}?')

        if validate():
            insert(name)


def average():
    average_class = 0
    for k in student:
        average_class += student.get(k)

    print(f'--> Class average is {(average_class / len(student)):.2f}')


def changeName():
    old_name = input('Inform old student\'s name: ')
    if old_name in student:
        new_name = input('Inform new student\'s name: ')
        if confirm(old_name, new_name):
            student[new_name] = student.pop(old_name)
            print('** Student`s name changed successfully. **')
        else:
            print('** Student`s name not changed. ** \n')
    else:
        print('** Student not found in list. **')
