import json
import os


class DataBase:
    def __init__(self, file_name):
        self.file_name = file_name

        if os.path.exists(self.file_name):
            with open(self.file_name, encoding='utf-8') as f:
                self.all_employee = json.load(f)

        else:
            self.all_employee = []

    def save(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.all_employee, f, ensure_ascii=False)

    def get(self, num):
        return self.all_employee[num - 1]

    def add_employee(self, name, surname, data, post, age):
        self.all_employee.append({"Имя": name, "Фамилия": surname, "Дата приёма на работу": data, "Должность": post, "Возраст": age})
        self.save()

    def select_by_age(self, age ):
        return [x for x in self.all_employee if x['age'] == age]


if __name__ == '__main__':
    db = DataBase('all_employee.json')

    print('''\
Выберите действие:
    1 - добавить Сотрудника,
    2 - вывод по номеру,
    3 - вывод по возрасту,
    4 - вывод из файла
    для выхода - 0
''')

    while True:
        f = input('Ввод действия:  ')
        if f == '1':
            print('Введите данные через пробел (имя,фамилия,дату приёма, должность, возраст)')
            name, surname, data, post, age = input().split()
            db.add_employee(name, surname, data, post, age)

        elif f == '2':
            num = int(input('Номер ->  '))
            print(db.get(num))

        elif f == '3':
            items = db.select_by_age(input('Возраст-> '))
            print(items)

        elif f == '4':
            with open(db.file_name, encoding='utf-8') as f:
                text = f.read()
                print(repr(text))

        else:
            break

    # Save file
    db.save()

