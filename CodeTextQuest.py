money = 0
food = set()
rubbish = set()
expensive = set()
clothes = set()
print('Привет, я бомжик. Для начала истории вам надо выбрать мне имя.')
name = input('Введите мне имя.')
print('Ура!Моё имя:' + name)
while 2 > 1:
    print("Передо мной 2 помойки, в какую мне идти?   1) Правая     2) Левая    В ответ запишите 1 или 2")
    first = input()
    if first == '2':
        print("В данной мусорке", name, 'нашёл 100 рублей и старую видеокарту')
        money += 100
        expensive.add('1')  # 1 - Старая видеокарта
        break
    elif first == '1':
        print("В данной мусорке", name, 'нашёл кусок хлеба и рваный ботинок')
        food.add("1")  # 1 - Кусок хлеба
        clothes.add("1")  # 1 - Рванный ботинок
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
        rubbish.add("1")  # 1 - Огрызок мандарина
        break
    elif second == '1':
        print("В данной мусорке", name, 'нашёл коробку от тротила')
        rubbish.add("2")  # 2 - Коробка от тротила
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
                expensive.add("2")  # 2 - Серебрянные часы
                food.add("2")  # 2 - Шоколадка
                break
            elif vibor == '2':
                print(name, 'вас опередил и уже пошёл направо')
                print("Где он нашёл Серебрянные часы и 5000 рублей")
                money += 5000
                expensive.update("2")  # 2 - Серебрянные часы
                break
            elif vibor != '1' or vibor != '2':
                print("Неверно введенные данные, введите цифру 1 или 2")
                continue
        rubbish.update("3")  # 3 - 5 Бесполезных жестянок
        break
    elif svalka == '2':
        print('УРА!!!', name, 'нашёл серебрянные часы и 2000 рублей')
        money += 2000
        expensive.update("2")  # 2 - Серебрянные часы
        break
    else:
        print("Да введи ты нормальные данные")
        continue
print("С радостью приняв подарок", name, 'пошёл в Ломбард потратя на проезд 50 рублей')
money -= 50
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
            money += 45000
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
                            money += 9000
                            expensive.discard("1")  # Старая видеокарта
                            break
                        elif vibor3 == '2':
                            print('- Нууу... Ладно, вот ваши деньги')
                            print('- До свидания!')
                            expensive.discard("1")  # Старая видеокарта
                            money += 13000
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
                    money += 55000
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
                                    money += 9000
                                    expensive.discard("1")  # Старая видеокарта
                                    break
                                elif vibor7 == '2':
                                    print("Нууу... хорошо я куплю её у вас")
                                    print("До свидания!")
                                    money += 13000
                                    expensive.discard("1")  # Старая видеокарта
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
                    print("Ок, я куплю за 50000 у вас часы")
                    print("Могу ли я что-нибудь ещё у вас приобрести?")
                    print("1) Да")
                    print("2) Нет")
                    money += 50000
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
                                    money += 9000
                                    expensive.discard("1")  # Старая видеокарта
                                    break
                                elif vibor6 == '2':
                                    print("Нууу... хорошо по рукам")
                                    print("Всего наилучшего")
                                    money += 13000
                                    expensive.discard("1")  # Старая видеокарта
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
expensive.discard("2")  # Серебрянные часы
money -= 20000
expensive.add(1)  # Iphone 15 ProMax
print("После продажи вы купили Iphone 15 ProMax. На какую оффлайн работу вы пойдёте?")
print("1) Программист")
print("2) Дизайнер")
print("3) Математик")
job = input()
while job != '1' and job != '2' and job != '3':
    print("Введи 1, 2 или 3")
    job = input()
if job == '1':
    print("Вы успешно стали программистом. У вас 3 задачи. Вам достаточно выполнить одну. Какую вы выберите?")
    print("1) Тест на знание python")
    print("2) Тест на знание python")
    print("3) ???")
    zadacha = input()
    while zadacha != '1' and zadacha != '2' and zadacha != '3':
        print("Не работать здесь нельзя, пожалуйста выбери себе задачу 1, 2 или 3(???)")
        zadacha = input()
    if zadacha == '1' or zadacha == '2':
        print("Маленький тест на программиста из 3 вопросов. Готовы? Вас не спрашивали, вы готовы!")
        print("Вопрос 1. Что выполняет эта команда?(for)")
        print("1) Ничего, её добавили по приколу")
        print("2) Повторяет что либо определенное количество раз")
        print("3) Повторяет что либо пока компьютер не сгорит")
        otvet = input()
        while otvet != '1' and otvet != '2' and otvet != '3':
            print("Такой ответ не принимается, введи нормальный ответ")
            otvet = input()
        if otvet == '1' or otvet == '3':
            print("Это неправильный ответ, так что мы вас увольняем и даём 30000 за вашу попытку ответить")
            money += 30000
        else:
            print("Вы молодец! Это правильный ответ, но мы вас увольняем т.к нашли более качественного сотрудника")
            print("В качестве извинений вот вам 50000")
            money += 50000
    else:
        print("Посмотрите это видео после чего напишите 1 если вы всё поняли")
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        video = input()
        while video != '1':
            print("Посмотри видео, отказываться нельзя")
            video = input()
        print("Поздравляю вы разблокировали пасхалочку rickroll")
        print("Теперь вернёмся к работе, вас уволили и дали 30000 из-за того что вы не проходили тест на python")
        money += 30000
elif job == '2':
    print("Мы приносим свои извинения, однако мы нашли вам замену.")
    print("У вас будет только 1 задача, за которую вы получите 40000")
    print("Нарисуйте вот такой домик:")
    print("      **      ")
    print("    **  **    ")
    print(" ***      *** ")
    print("*            *")
    print("*   *****    *")
    print("*   *   *    *")
    print("*   *****    *")
    print("*            *")
    print("**************")
    print("Хотя, не надо вот ваши деньги, идите")
    money += 40000
else:
    print('Мы взяли вас на испытательный срок после которого вы получите 20000')
    print("Ваша задача решить 3 простых примера. Готовы?")
    print("1) Да")
    print("2) Конечно")
    print("3) Естественно")
    matematik = input()
    while matematik != '1' and matematik != '2' and matematik != '3':
        print("Вы обязаны сделать выбор!")
        matematik = input()
    print("Отлично! Первый пример:")
    print("x^2 + 4x + 4 = 0")
    primer1 = input()
    if primer1 == '-2':
        print("Правильно")
    else:
        print("Как можно не знать что ответ -2?")
    print("Второй пример:")
    print("9x^2 - 39x + 12 = 0")
    print("В ответ запишите больший корень")
    primer2 = input()
    if primer2 == "4":
        print("Молодец, но медленно как-то...")
    else:
        print("Это даже первоклассник за 5 секунд решит и получит ответ 4!!!")
    print("Третий пример:")
    print("25x^2 + 20x + 4 = 0")
    print("В ответ запишите один корень")
    primer3 = input()
    if primer3 == '-0.4' or primer3 == '0,4':
        print("Молодец, но очень медленно!")
    else:
        print('НЕТ!')
    print("Подводя итоги решения у вас разумные(иногда), но решаете вы очень медленно, вы нам не подходите.")
    print("Вот ваши 20000, идите.")
    money += 20000
