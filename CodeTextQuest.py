money = 0
food = set()
rubbish = set()
expensive = set()
clothes = set()
bankrot = 0
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
print("Идея с заработком в интернете была не очень, однако теперь мы можем устроиться оффициально")
print("Нас готовы взять на работу 3 компании в какую пойдёт наш", name, '?')
print("1) Microsoft")
print("2) Apple")
print("3) Rockstar")
company = input()
while company != '1' and company != '2' and company != '3':
    print("По сюжету вы должны устроиться на работу")
    company = input()
if company == '1':
    print("Прошло много времени с того момента как", name, 'тут работает.')
    print("За это время чистыми учитывая абсолютно все расходы", name, 'заработал(а) 400к')
    print("Однако", name, 'это надоедает. DDOS атаки, взломы аккаунтов и.т.п')
    print("И такое каждый день.", name, 'хочет уволиться и открыть бизнес. Выбор за вами.')
    print("1) Отработать ещё 2 месяца получить чистыми 150к, а затем уволиться")
    print("2) Уволиться сейчас")
    uvolnenie = input()
    while uvolnenie != '1' and uvolnenie != '2':
        print("Вариант не увольняться не рассматривается!")
        uvolnenie = input()
    if uvolnenie == '1':
        print("Вы успешно отработали 2 месяца, теперь можно уволиться...")
        money += 150000
    else:
        print("- Вот документы на увольнение подписывайте вот там")
        print("- Пожалуйста, моё заявление на увольнение")
        print("- До свидания")
    money += 400000
elif company == '2':
    print('Вы успешно устроились в Apple, однако спустя месяц вы нарушили 1 из правил этой компании.')
    print("Вы подумали о друге у которого нет телефона от Apple. За это вас уволили.")
    print("Однако вы получили зарплату за этот месяц в размере 140к")
    print("Отомстить Apple и открыть свою компанию?")
    print("1) Да")
    print("2) Да")
    topovii_vibor = input()
    while topovii_vibor != '1' and topovii_vibor != '2':
        print("Да")
        topovii_vibor = input()
    money += 140000
else:
    print("Вы только пришли в компанию Rockstar. Вам авансом дали 100к.")
    print("Вы решили сразу повышения, однако у них были другие планы.")
    print("Вам сразу дали заявление на увольнение.")
    print("Ну хоть 100к дали...")
    money += 100000
print("После того как", name, 'уволился(лась) он(а) решает создать свой бизнес.')
print("Однако какой именно бизнес", name, 'не придумал(а). Помогите с выбором.')
print("1) Собственная кофейня")
print("2) Собственная сеть магазинов")
print("3) Собственная заправка")
business_vibor = input()
while business_vibor != '1' and business_vibor != '2' and business_vibor != '3':
    print("Другой бизнес открыть нельзя")
    business_vibor = input()
if business_vibor == '1':
    print("Для кофейни нам нужно:")
    print("- Аренда помещения(10000)")
    print("- Кофемашина(30000)")
    print("- Посуда(5000)")
    print("- Зерна для кофе(2000)")
    print("- Наём персонала(100000)")
    print("Когда всё было куплено", name, 'открыл(а) бизнес.')
    print('Время шло, бизнес шёл в гору, однако у владельцев бизнеса тоже есть свои задания.')
    print("С какого начнёт наш персонаж?")
    nazvanie_biznesa = 'кофейня'
    print("1) Расширить меню")  # Расширение меню после чего посетители жалуются на грязные чашки, падение бизнеса
    print("2) Заказать новые продукты и посуду")  # Дальнейший рост бизнеса после чего его отбирает гос-во
    print("3) Ничего не делать, у меня есть персонал пусть делают всё за меня")  # Падение бизнеса
    zadaniya = input()
    while zadaniya != '1' and zadaniya != '2' and zadaniya != '3':
        print("Задание надо выбрать")
        zadaniya = input()
    if zadaniya == '1':
        print("- Босс мы добавили 5 новых видов кофе.")
        print("- Отлично, как дела с прибылью?")
        print("- Всё очень плохо, наши посетители жалуются на грязную посуду, и ещё уходят из меню другие продукты.")
        print("- Из-за чего?")
        print("- У нас нет нужных ингридиентов для приготовления. Надо что-то делать.")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    elif zadaniya == '2':
        print("- Босс, босс! Наш бизнес хочет купить крупная компания, ответ нужен прямо сейчас!")
        print("1) О какой сумме идёт речь?")
        print("2) Скажи им, что я отказываюсь.")
        vibor10 = input()
        while vibor10 != '1' and vibor10 != '2':
            print("Всё зависит от вас, помогите определиться, время на исходе!")
            vibor10 = input()
        if vibor10 == '1':
            print('- О какой сумме идёт речь?')
            print("- 20.000.000")
            print("1) Меня это не устраивает, скажи, что это очень мало.")
            vibor11 = input()
            while vibor11 != '1':
                print("Это очень маленькая цена!")
                vibor11 = input()
            print("- Меня это не устраивает, скажи, что это очень мало.")
            print("- Хорошо, слушаюсь.")
            print("Спустя 2 месяца...")
            print("- БОСС У НАС ОТСУДИЛИ БИЗНЕС, ТЕПЕРЬ ОН НЕ ПРИНАДЛЕЖИТ НИ НАМ НИ ТОЙ КОМПАНИИ!!!")
            print('- А кому он принадлежит?')
            print("- ГОСУДАРСТВУ")
        else:
            print("- Босс у нас отсудили бизнес и присудили его государству.")
            print("- ГОСУДАРСТВУ?")
            print("- Да.")
        business_sostoyanie_count = 2  # 2 - Означает потеря бизнеса
    else:
        print("- Босс я вас поздравляю, т.к вы ничего не делали, бизнес сильно упал, мы работаем в убыток.")
        print("- Что же нам делать?")
        print("- Я увольняюсь я тут работать больше не могу!")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
elif business_vibor == '2':
    print("Прекрасный выбор! Однако для этой сети магазинов нам нужно название.")
    print("Дайте название данной сети магазинов:")
    shop = input()
    print("Ах да... забыл сказать, надо очень много денег(2000000). У", name, 'их всего', money)
    print("Придется выбирать что-то другое...")
    print("1) Кофейня")
    print("2) Заправка")
    business_vibor2 = input()
    while business_vibor2 != '1' and business_vibor2 != '2':
        print("Не получится развить этот бизнес.")
        print("Мало денег.")
        business_vibor2 = input()
    if business_vibor2 == '1':
        print("Для кофейни нам нужно:")
        print("- Аренда помещения(10000)")
        print("- Кофемашина(30000)")
        print("- Посуда(5000)")
        print("- Зерна для кофе(2000)")
        print("- Наём персонала(100000)")
        print("Когда всё было куплено,", name, 'открыл(а) бизнес.')
        print('Время шло, бизнес шёл в гору, однако, у владельцев бизнеса тоже есть свои задания.')
        print("С какого начнёт наш персонаж?")
        nazvanie_biznesa = 'кофейня'
        print("1) Расширить меню")  # Расширение меню после чего посетители жалуются на грязные чашки, падение бизнеса
        print("2) Заказать новые продукты и посуду")  # Дальнейший рост бизнеса после чего его отбирает гос-во
        print("3) Ничего не делать, у меня есть персонал пусть делают всё за меня")  # Падение бизнеса
        zadaniya = input()
        while zadaniya != '1' and zadaniya != '2' and zadaniya != '3':
            print("Задание надо выбрать")
            zadaniya = input()
        if zadaniya == '1':
            print("- Босс, мы добавили 5 новых видов кофе.")
            print("- Отлично, как дела с прибылью?")
            print("- Всё очень плохо, наши посетители жалуются на грязную посуду, и ещё уходят из меню другие продукты.")
            print("- Из-за чего?")
            print("- У нас нет нужных ингридиентов для приготовления. Надо что-то делать.")
            business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
        elif zadaniya == '2':
            print("- Босс, босс! Наш бизнес хочет купить крупная компания, ответ нужен прямо сейчас!")
            print("1) О какой сумме идёт речь?")
            print("2) Скажи им, что я отказываюсь.")
            vibor10 = input()
            while vibor10 != '1' and vibor10 != '2':
                print("Всё зависит от вас, помогите определиться, время на исходе!")
                vibor10 = input()
            if vibor10 == '1':
                print('- О какой сумме идёт речь?')
                print("- 20.000.000")
                print("1) Меня это не устраивает, скажи, что это очень мало.")
                vibor11 = input()
                while vibor11 != '1':
                    print("Это очень маленькая цена!")
                    vibor11 = input()
                print("- Меня это не устраивает, скажи, что это очень мало.")
                print("- Хорошо, слушаюсь.")
                print("Спустя 2 месяца...")
                print("- БОСС, У НАС ОТСУДИЛИ БИЗНЕС, ТЕПЕРЬ ОН НЕ ПРИНАДЛЕЖИТ НИ НАМ, НИ ТОЙ КОМПАНИИ!!!")
                print('- А кому он принадлежит?')
                print("- ГОСУДАРСТВУ")
            else:
                print("- Босс, у нас отсудили бизнес и присудили его государству.")
                print("- ГОСУДАРСТВУ?")
                print("- Да.")
            business_sostoyanie_count = 2  # 2 - Означает потеря бизнеса
        else:
            print("- Босс, я вас поздравляю, т.к вы ничего не делали, бизнес сильно упал, мы работаем в убыток.")
            print("- Что же нам делать?")
            print("- Я увольняюсь, я тут работать больше не могу!")
            business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    else:
        print("Это отличный выбор! С покупкой проблем не возникло.")
        print("Однако, для заправки нужен бензин, товары в магазин и оборудование.")
    print("После того, как всё было куплено бизнес приносил много денег. Однако бензин и товары заканчивались.")
    print("Надо решать эту проблему, иначе бизнес себя не окупит.")
    nazvanie_biznesa = 'заправка'
    print("1) Пойти решать проблему с нехваткой бензина")  # Другая проблема не решена --> падение бизнеса
    print("2) Пойти решать проблему с нехваткой продуктов в магазине")  # Другая проблема не решена --> падение бизнеса
    print('3) Пойти решать обе проблемы')  # Высокий рост --> бизнес забирает гос-во
    vibor12 = input()
    while vibor12 != '1' and vibor12 != '2' and vibor12 != '3':
        print("Надо решать проблемы, вы же не хотите чтобы бизнес прогорел?")
        vibor12 = input()
    if vibor12 == '1':
        print("- Босс, мы заказали бензин, только наши посетители жалуются на нехватку продуктов в магазине.")
        print("- Ну и пусть жалуются, прибыль то всё равно идёт.")
        print("- Я бы так не сказал, раньше у нас было по 100 клиентов как и в магазине так и на заправочной станции,")
        print("а сейчас около 10 - 15 клиентов в день.")
        print("- Убыток очень большой?")
        print("- За последние 3 месяца да.")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    elif vibor12 == '2':
        print("- Босс, мы заказали продукты, как вы и сказали.")
        print("- А с бензином что у нас?")
        print("- На него денег не хватило, поэтому бизнес работает плохо.")
        print("- Я займусь этим.")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    else:
        print("- Босс, у меня хорошие новости! Наш бизнес уверенно растёт.")
        print("- Это отлично!")
        print("- Только что поступило предложение о покупке бизнеса! Босс, выбор за вами!")
        print("1) Сколько нам предлагают?")
        print("2) Скажи им что я отказываюсь")
        vibor13 = input()
        while vibor13 != '1' and vibor13 != '2':
            print("На предложение надо ответить, мы же культурные люди.")
            vibor13 = input()
        if vibor13 == '1':
            print("- Сколько нам предлагают?")
            print("- 45.000.000")
            print("- Скажи что это ма...")
            print("- Иначе у нас его заберет государство.")
            print("- Заберёт гос-во? Бред, гос-во никак не сможет забрать наш бизнес.")
            print("- Я иду говорить что мы отказываемся?")
            print("1) Да")
            print("2) Предложи цену в 70.000.000")
            vibor14 = input()
            while vibor14 != '1' and vibor14 != '2':
                print("Надо что-то сказать.")
                vibor14 = input()
            if vibor14 == '1':
                print("Переговоры нашего сотрудника и компании:")
                print("- Ваше предложение было очень важно для нас! Однако мы откажемся у него.")
                print("- Хорошо, только теперь принадлежит нам.")
                print("- Как? Почему это?")
                print("- Это уже остается тайной. Так что теперь ты тут не работаешь. Всё иди отсюда")
            else:
                print("Они сказали что это очень много, поэтому они забрали ваш бизнес силой.")
        else:
            print("Босс, у нас украли бизнес, из-за того что мы им отказались продавать его.")
        business_sostoyanie_count = 2  # 2 - Означает потеря бизнеса
else:
    print("Это отличный выбор! С покупкой проблем не возникло.")
    print("Однако, для заправки нужен бензин, товары в магазин и оборудование.")
    print("После того, как всё было куплено бизнес приносил много денег. Однако бензин и товары заканчивались.")
    print("Надо решать эту проблему, иначе бизнес себя не окупит.")
    nazvanie_biznesa = 'заправка'
    print("1) Пойти решать проблему с нехваткой бензина")  # Другая проблема не решена --> падение бизнеса
    print("2) Пойти решать проблему с нехваткой продуктов в магазине")  # Другая проблема не решена --> падение бизнеса
    print('3) Пойти решать обе проблемы')  # Высокий рост --> бизнес забирает гос-во
    vibor12 = input()
    while vibor12 != '1' and vibor12 != '2' and vibor12 != '3':
        print("Надо решать проблемы, вы же не хотите чтобы бизнес прогорел?")
        vibor12 = input()
    if vibor12 == '1':
        print("- Босс, мы заказали бензин, только наши посетители жалуются на нехватку продуктов в магазине.")
        print("- Ну и пусть жалуются, прибыль то всё равно идёт.")
        print("- Я бы так не сказал, раньше у нас было по 100 клиентов как и в магазине так и на заправочной станции,")
        print("а сейчас около 10 - 15 клиентов в день.")
        print("- Убыток очень большой?")
        print("- За последние 3 месяца да.")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    elif vibor12 == '2':
        print("- Босс, мы заказали продукты, как вы и сказали.")
        print("- А с бензином что у нас?")
        print("- На него денег не хватило, поэтому бизнес работает плохо.")
        print("- Я займусь этим.")
        business_sostoyanie_count = 1  # 1 - Означает падение бизнеса
    else:
        print("- Босс, у меня хорошие новости! Наш бизнес уверенно растёт.")
        print("- Это отлично!")
        print("- Только что поступило предложение о покупке бизнеса! Босс, выбор за вами!")
        print("1) Сколько нам предлагают?")
        print("2) Скажи им что я отказываюсь")
        vibor13 = input()
        while vibor13 != '1' and vibor13 != '2':
            print("На предложение надо ответить, мы же культурные люди.")
            vibor13 = input()
        if vibor13 == '1':
            print("- Сколько нам предлагают?")
            print("- 45.000.000")
            print("- Скажи что это ма...")
            print("- Иначе у нас его заберет государство.")
            print("- Заберёт гос-во? Бред, гос-во никак не сможет забрать наш бизнес.")
            print("- Я иду говорить что мы отказываемся?")
            print("1) Да")
            print("2) Предложи цену в 70.000.000")
            vibor14 = input()
            while vibor14 != '1' and vibor14 != '2':
                print("Надо что-то сказать.")
                vibor14 = input()
            if vibor14 == '1':
                print("Переговоры нашего сотрудника и компании:")
                print("- Ваше предложение было очень важно для нас! Однако мы откажемся у него.")
                print("- Хорошо, только теперь принадлежит нам.")
                print("- Как? Почему это?")
                print("- Это уже остается тайной. Так что теперь ты тут не работаешь. Всё иди отсюда")
            else:
                print("Они сказали что это очень много, поэтому они забрали ваш бизнес силой.")
        else:
            print("Босс, у нас украли бизнес, из-за того что мы им отказались продавать его.")
        business_sostoyanie_count = 2  # 2 - Означает потеря бизнеса
# Окончание пункта 6(УРА)
if business_sostoyanie_count == 1:
    print("Бизнес очень сильно упал из-за ваших ошибок! Это срочно надо исправлять, пока не поздно!")
    print("Для того чтобы вернуть прибыль бизнесу, надо сделать:")
    if nazvanie_biznesa == 'кофейня':
        print("- Нанять новый персонал")
        print("- Заказать продукты")
        print("- Помыть и заказать новые чашки")
        print("- Починить кофемашинки")
        print("1) Нанять новый персонал и починить кофемашинки")
        print("2) Заказать продукты и новые чашки")
        vibor15 = input()
        while vibor15 != '1' and vibor15 != '2':
            print("Ты бизнес поднять хочешь или нет?")
            vibor15 = input()
        if vibor15 == '1':
            print("Вы успешно наняли персонал и починили кофемашинки, а толку если нету ни чашек ни кофе?")
            print("Вы потратили все деньги на персонал и кофемашинки у вас на счету 500 рублей. Вы банкрот!")
            bankrot = 1  # 1 - банкрот
        else:
            print("Хоть и со старыми машинками хоть и один без чей либо помощи", name, 'справился(лась).')
            print('Теперь есть хоть какие-то деньги, на них были отремонтированны кофемашинки и нанят персонал.')
            print("Бизнес опять начал идти в гору, УРА!")
    else:
        print("- Заказать новое топливо")
        print("- Продукты в магазин")
        print("- Нанять новых работников")
        print("1) Нанять новых работников, заказать продукты")
        print("2) Заказать продукты и бензин")
        vibor16 = input()
        while vibor16 != '1' and vibor16 != '2':
            print("Надо поднимать бизнес!")
            vibor16 = input()
        if vibor16 == '1':
            print("Вы успешно наняли персонал и заказали продукты, а толку если нету бензина?")
            print("У вас нет денег на бензин, вы банкрот!")
            bankrot = 1  # 1 - банкрот
        else:
            print("Хоть и один без какой либо помощи, но", name, 'поднял(а) бизнес из грязи.')
else:
    print("Бизнеса нет.")
