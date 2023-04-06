from script import input_data, delete_data, put_data, print_data

def interface():
    print('Доброго времени суток! Вы попали на специальную программу от нашей группы!\n'
          'Что же мы будем делать?\n'
          '1. Записывать данные (в 2-ух форматах);\n'
          '2. Удалять данные;\n'
          '3. Изменять данные;\n'
          '4. Выводить данные.\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print("Упс! Такой операции нет.")
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()




