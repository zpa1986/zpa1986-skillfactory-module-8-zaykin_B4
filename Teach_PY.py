# Импортируем модуль json
import json
# импортируем модуль os для работы с текущей операционной системой
import os
# импортируем модуль uuid для возможности генерации ID
import uuid


# в этой переменной будем хранить путь к JSON документу
DATA_FILE_PATH = "users.json"

def read():
    #проверяем наличие файла на диске
    if not os.path.exists(DATA_FILE_PATH):
        #возвращаем пустой список (в который потом будем писать значения)
        return []
    #открываем файл на чтение
    with open(DATA_FILE_PATH) as fd:
        #загружаем JSON документ
        users = json.load(fd)
    #возвращаем список пользователей
    return users

def save(users_list):
    # открываем файл на запись
    with open(DATA_FILE_PATH, "w") as fd:
        # сохраняем список пользователей на диск в соответствующий каталог fd
        json.dump(users_list, fd)

def find(users_list):
    name = input("Введите имя для поиска: ")
    # итерируемся по всем пользователям по имени
    for user in users_list:
        #проверяем совпадение
        if user["first_name"] == name:
            #если имя совпало, то возвращаем идентификатор пользователя
            return user["id"]

def request_data():
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введите своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    while valid_email(email) == False:
        print("Электронный адрес должен содержать \"@\" и хотя бы одну точку в домене!")
        email = input("Введите электронный адрес еще раз: ")

    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем словарь пользователя
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    #возвращаем созданного пользователя
    return

def valid_email(email):
    if email.find(".", email.find("@")) == -1 or email.find("@") == -1:
        return False
    elif email.count("@") > 1:
        return False
    else:
        return True

def main():
    # читаем список сохранённых пользователей
    users_list = read()
    #просим пользователя выбрать режим (поиск или создание нового пользователя)
    mode = input("Выберите режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    if mode == "1":
        #выбран режим поиска, запускаем его
        user_id = find(users_list)
        if user_id:
            print("Найден пользователь с идентификатором: ",user_id)
        else:
            print("Такого пользователя нет.")
    elif mode == "2":
        user = request_data()
        # добавляем нового пользователя в список всех пользователей
        users_list.append(user)
        # сохраняем список пользователей
        save(users_list)
        print("Спасибо, данные сохранены")
    else:
        print("Некорректный режим")

if __name__ == "__main__":
    main()















