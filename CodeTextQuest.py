money = 0
food = set()
rubbish = set()
expensive = set()
clothes = set()
print('Привет, я бомжик. Для начала истории вам надо выбрать мне имя.')
print("Когда вы доберетесь до чекпоинта(Перехода на следующую стадию) вы получите уведомление об этом")
name = input('Введите мне имя.')
print('Ура!Моё имя:' + name)
while 2 > 1:
    print("Передо мной 2 помойки, в какую мне идти?   1) Правая     2) Левая    В ответ запишите 1 или 2")
    first = input()
    if first == '2':
        print("В данной мусорке", name, 'нашёл 100 рублей и старую видеокарту')
        money += 100
        expensive.update('Старая видеокарта')
        break
    elif first == '1':
        print("В данной мусорке", name, 'нашёл кусок хлеба и рваный ботинок')
        food.update("Кусок хлеба")
        clothes.update("Рваный ботинок")
        break
    elif first != '1' or first != '2':
        print("Вы ввели неверные данные")
        continue
print('После этого', name, 'пошёл спать')
while 2 > 1:
    print("День 2. Очередные поиски мусорки, куда идём?")
    print("1) Лево")
    print("2) Право")
    second = input()
    if second == '2':
        print("В данной мусорке", name, ' нашел огрызок мандарина')
        rubbish.update("Огрызок мандарина")
        break
    elif second == '1':
        print("В данной мусорке", name, 'нашёл коробку от тротила')
        rubbish.update("Коробка от тротила")
        break
    elif second != '1' or second != '2':
        print("Вы ввели неверные данные")
        continue
print("Грустный", name, 'ушёл из 2-й мусорки ничего не найдя',\
"Однако пройдя Ленинский Проспект он увидел большую свалку",\
"Помогите с выбором, куда идти?")
while 2 > 1:
    print('Напишите 1 если советуете идти налево, 2 если направо')
    svalka = input()
    while 2 > 1:
        if svalka == '1':
            print("Здесь были только бесполезные жестянки,", name, 'хочет пойти направо')
            print('1) Да')
            print('2) Нет')
            vibor = input()
            if vibor == '1':
                print(name, 'нашёл серебрянные часы и шоколадку!')
                expensive.update("Серебрянные часы")
                food.update("Шоколадка")
                break
            elif vibor == '2':
                print(name, 'вас опередил и уже пошёл направо')
                print("Где он нашёл Серебрянные часы и 5000 рублей")
                money += 5000
                expensive.update("Серебрянные часы")
                break
            else:
                print("Неверно введенные данные, введите цифру 1 или 2")
                continue
        rubbish.update("5 Бесполезных жестянок")
        break
    elif svalka == '2':
        print('УРА!!!', name, 'нашёл серебрянные часы и 2000 рублей')
        money += 2000
        expensive.update("Серебрянные часы")
        break
    else:
        print("Да введи ты нормальные данные")
        continue
