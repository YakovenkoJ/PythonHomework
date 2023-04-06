from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"Вариант 1: \n\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"Вариант 2: \n\n"
                    f"{name}; {surname}; {phone}; {address}\n\n"
                    f"Выберите номер варианта: "))
    
    while var != 1 and var != 2:
        print("Упс! Такого варианта нет.")
        var = int(input("Выберите номер варианта: "))

    if var == 1:
        with open('data_1st_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_2nd_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def delete_data():
    data_first, data_second = print_data()
    print("Из какого файла Вы хотите удалить данные?")
    number_file = int(input("Введите номер файла: "))

    while number_file != 1 and number_file != 2:
        print("Упс! Такого файла нет.")
        number_file = int(input("Введите номер файла: "))

    if number_file == 1: 
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input("Введите номер записи: ")) 
        with open ('data_1st_variant.csv', 'r', encoding='utf-8') as file:
            index = number_journal - 1
            for i in range(len(data_first)):
                if i == index:
                    data_first.pop(i)

        with open ('data_1st_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(data_first))
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input("Введите номер записи: "))
        with open ('data_2nd_variant.csv', 'r', encoding='utf-8') as file:
            data_second_temp = []
            for i in range(len(data_second)):
                if data_second[i] != '\n':
                    data_second_temp.append(data_second[i])
            
            index = number_journal - 1

            for i in range(len(data_second_temp)):
                if i == index:
                    data_second_temp.pop(i)
            
        with open ('data_2nd_variant.csv', 'w', encoding='utf-8') as file:
            data_second = data_second_temp
            file.writelines('%s\n' % i for i in data_second)


def put_data():
    data_first, data_second = print_data()
    print("В каком файле Вы хотите изменить данные?")
    number_file = int(input("Введите номер файла: "))

    while number_file != 1 and number_file != 2:
        print("Упс! Такого файла нет.")
        number_file = int(input("Введите номер файла: "))

    if number_file == 1: 
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input("Введите номер записи: "))
        new_name = input("Введите новое имя: ")
        new_surname = input("Введите новую фамилию: ")
        new_phone = input("Введите новый номер телефона: ")
        new_address = input("Введите новый адрес: ")
        updated_data = f'{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n'

        with open ('data_1st_variant.csv', 'r', encoding='utf-8') as file:
            index = number_journal - 1
            for i in range(len(data_first)):
                if i == index:
                    data_first[i] = data_first[i].replace(data_first[i], updated_data)

        with open ('data_1st_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(data_first))
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input("Введите номер записи: "))
        new_name = input("Введите новое имя: ")
        new_surname = input("Введите новую фамилию: ")
        new_phone = input("Введите новый номер телефона: ")
        new_address = input("Введите новый адрес: ")
        updated_data = f'{new_name};{new_surname};{new_phone};{new_address}\n'
       
        with open ('data_2nd_variant.csv', 'r', encoding='utf-8') as file:
            data_second_temp = []
            for i in range(len(data_second)):
                if data_second[i] != '\n':
                    data_second_temp.append(data_second[i])
            
            index = number_journal - 1
            for i in range(len(data_second_temp)):
                if i == index:
                    data_second_temp[i] = data_second_temp[i].replace(data_second_temp[i], updated_data)
        with open ('data_2nd_variant.csv', 'w', encoding='utf-8') as file:
            data_second = data_second_temp
            file.writelines('\n'.join(data_second)) 
        

def print_data():
    print("Вывожу данные для Вас из первого файла:\n")
    with open ('data_1st_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        # data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                 data_first_version_second.append(''.join(data_first[j:i + 1]))
                 j = i
        data_first = data_first_version_second
        print(''.join(data_first))

        # print(*data_first, sep='')     # Вариант упрощения кода. 

    print("Вывожу данные для Вас из второго файла:\n")
    with open ('data_2nd_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second