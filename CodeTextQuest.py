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
        expensive.add('Старая видеокарта')
        break
    elif first == '1':
        print("В данной мусорке", name, 'нашёл кусок хлеба и рваный ботинок')
        food.update("Кусок хлеба")
        clothes.add("Рваный ботинок")
        break
    elif first != '1' and first != '2':
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
        rubbish.add("Огрызок мандарина")
        break
    elif second == '1':
        print("В данной мусорке", name, 'нашёл коробку от тротила')
        rubbish.add("Коробка от тротила")
        break
    elif second != '1' and second != '2':
        print("Вы ввели неверные данные")
        continue
print("Грустный", name, 'ушёл из 2-й мусорки ничего не найдя.',
      "Однако пройдя Ленинский Проспект он увидел большую свалку.",
      "Помогите с выбором, куда идти?")
while 2 > 1:
    print('Напишите 1 если советуете идти налево, 2 если направо')
    svalka = input()
    if svalka == '1':
        while 2 > 1:
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
                expensive.add("Серебрянные часы")
                break
            elif vibor != '1' or vibor != '2':
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
print("С радостью приняв подарок", name, 'пошёл в Ломбард потратя на проезд 50 рублей')
while 2 > 1:
    print("В ломбарде ему предложили 45000 рублей, соглашаться или поднимать цену?")
    print("1) Согласиться")
    print("2) Поднять цену")
    lombard = input()
    if lombard != '2' and lombard != '1':
        print('Данные неверны')
        continue
    if lombard == '1':
        while 2 > 1:
            print('Спасибо, за сделку!')
            print('Не хотите ли вы продать нам ещё что-то?')
            print('1) Да')
            print('2) Нет')
            vibor2 = input()
            if vibor2 == '1':
                print("Хорошо, что у вас есть?")
                if first == '1':
                    print("- Рванный ботинок")
                    print('- Спасибо, нам такое не надо, до свидания!')
                else:
                    print('- Старая видеокарта')
                    print('- Могу дать вам за неё 9000')
                    print('1) По рукам')
                    print('2) Как насчет 13000?')
                    vibor3 = input()
                    while 2 > 1:
                        if vibor3 == '1':
                            print('Заходите к нам ещё, до свидания!')
                            break
                        elif vibor3 == '2':
                            print('- Нууу... Ладно, вот ваши деньги')
                            print('- До свидания!')
                            break
                        else:
                            print('Вариант ответа введен некоретно')
                            continue
                break
            elif vibor2 == '2':
                print("Хорошего вам вечера!")
                break
            else:
                print('Ответ введен неправильно')
                continue
        break
    break
while 2 > 1:
    if lombard == '2':
        while 2 > 1:
            print("Хорошо, а за сколько вы мне готовы продать эти часы?")
            print("1) 55000")
            print("2) 50000")
            vibor4 = input()
            if vibor4 == '1':
                while 2 > 1:
                    print("Ок, я куплю за 55000 у вас часы")
                    print("Могу ли я что-нибудь ещё у вас приобрести?")
                    print("1) Да")
                    print("2) Нет")
                    vibor5 = input()
                    if vibor5 == '1':
                        if first == '1':
                            print("- У меня есть рваный ботинок")
                            print("- Спасибо нам такое не надо, до свидания")
                            break
                        else:
                            while 2 > 1:
                                print('- У меня есть старая видеокарта')
                                print("- 9000 вас устроит")
                                print("1) Да, устроит")
                                print("2) Давайте 13000")
                                vibor7 = input()
                                if vibor7 == '1':
                                    print("Всего наилучшего!")
                                    break
                                elif vibor7 == '2':
                                    print("Нууу... хорошо я куплю её у вас")
                                    print("До свидания!")
                                    break
                                else:
                                    print("Некоректно введены данные!")
                                    continue
                            break
                    elif vibor5 == '2':
                        print("Хорошо, всего наилучшего!")
                        break
                    else:
                        print("Данные неверны напишите 1 или 2")
                        continue
            elif vibor4 == '2':
                while 2 > 1:
                    print("Ок, я куплю за 55000 у вас часы")
                    print("Могу ли я что-нибудь ещё у вас приобрести?")
                    print("1) Да")
                    print("2) Нет")
                    vibor5 = input()
                    if vibor5 == '1':
                        if first == '1':
                            print("- У меня есть рваный ботинок")
                            print("- Спасибо нам такое не надо, до свидания")
                            break
                        else:
                            print("- У меня есть старая видеокарта")
                            print("Я готов купить за 9000")
                            print("1) Я согласен")
                            print("2) Что насчёт 13000?")
                            vibor6 = input()
                            while 2 > 1:
                                if vibor6 == '1':
                                    print("Спасибо за сделку")
                                    break
                                elif vibor6 == '2':
                                    print("Нууу... хорошо по рукам")
                                    print("Всего наилучшего")
                                    break
                                else:
                                    print("Напишите число 1 или 2")
                                    continue
                        break
                    elif vibor5 == '2':
                        print("Хорошо, всего наилучшего!")
                        break
                    else:
                        print("Данные неверны напишите 1 или 2")
                        continue
            else:
                print("ВВЕДИ 1 ИЛИ 2")
                continue
            break
    break
