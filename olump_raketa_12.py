import time
from random import randint
import os

times = time.time()
speed = 0
enduranc = 100
fuel = 1000
scrap = 'нету'

def menu():
    global fuel
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                           ┃         _          ┃
    ┃                           ┃        ╱ ╲         ┃
    ┃                           ┃       ╱   ╲        ┃
    ┃                           ┃      ╱ ( ) ╲       ┃
    ┃                           ┃      │     │       ┃
    ┃    1 - НАЧАТЬ ИГРУ        ┃      | ( ) |       ┃
    ┃                           ┃      |     |       ┃
    ┃    2 - ЗАКОНЧИТЬ ИГРУ     ┃      | ( ) |       ┃
    ┃                           ┃      |     |       ┃
    ┃                           ┃     /       \      ┃
    ┃                           ┃    /         \     ┃
    ┃                           ┃   /           \    ┃
    ┃                           ┃  ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_menu = input('Что выбераем? ')
    if option_menu == '1':
        start_game()
    if option_menu == '2':
        print('Игра окончена')
        exit()

def event_meteorite():
    os.system('cls')
    global fuel
    print('О нет, на вас летят метеориты, чтобы отбить их правильно отвечай на вопросы')
    time.sleep(2)
    answer_1 = input('Вопрос 1: сколько будет если -6*12? ')
    if answer_1 == '-72':
        fuel -= 100
        print('Молодец!')
        time.sleep(2)
        answer_2 = input('Вопрос 2: сколько будет если 1005/5? ')
        if answer_2 == '201':
            fuel -= 100
            print('Молодец!')
            time.sleep(2)
            answer_3 = input('Вопрос 2: сколько будет 20% от 15? ')
            if answer_3 == '3':
                fuel -= 100
                print('Молодец! Ты смог отбить метеориты')
                time.sleep(1)
                print('Топливо - ', fuel)
                time.sleep(2)
                planet_ice_ball()
            else:
                print('Ты ответил неверно, двигатель повреждён и ты отправляешься на ближаюшую планету')
                time.sleep(1.5)
                print('К сожалению двигатель взорвался во время полёта :(')
                finish()
        else:
            print('Ты ответил неверно, двигатель повреждён и ты отправляешься на ближаюшую планету')
            time.sleep(1.5)
            print('К сожалению двигатель взорвался во время полёта :(')
            finish()
    else:
        print('Ты ответил неверно, двигатель повреждён и ты отправляешься на ближаюшую планету')
        time.sleep(1.5)
        print('К сожалению двигатель взорвался во время полёта :(')
        finish()

def event_aliens():
    os.system('cls')
    print('Во время полёта вы наткнулись на НЛО')
    print('''
          1 - Улететь
          2 - Подлететь ближе
          3 - Атаковать из пистолетов
          ''')
    option = input('Выберите что вы будете делать 1/2/3')
    if option == '1':
        print('Вы улетели и прилетели домой, на этом всё')
        print('конец')
        exit()
    if option == '2':
        print('Вы подлетели ближе к НЛО и они запустили по вам огонь')
        print('Ракета взорвалась')
        exit()
    if option == '3':
        print('Вы стали стрелять по НЛО и они запустили по вам огонь')
        print('Ракета взорвалась')
        exit()

def planet_ice_ball():
    os.system('cls')
    print('Вы приземлились на планету "Ледяной шар"')
    time.sleep(2)
    print('''
               Характеристики
           Климат - очень сурововый
        Средняя температура - -150'с 
         живые существа - неизвестно

               Цель прибывания
            1. Иследовать планету
            2. Добыть топливо
            3. Найти ресурсы

            Текущее время 14:00
''')
    input('Готовы отправиться на исследовние? Да/Нет ')
    print('В любом случае мы отправляемся')
    time.sleep(2)
    os.system('cls')
    planet_ice_ball_cave()

def planet_ice_ball_cave():
    global scrap
    option = input('По пути вы встретили 3 пещеры, в какую пойдем? 1/2/3 ')
    if option == '1':
        option = input('Поздравляю вы нашли в этой пещере ящик, будете вскрывать? Да/Нет ')
        if option == 'Да':
            print('В ящике был лом и вы его забрали')
            scrap = 'есть'
            planet_ice_ball_village()
        if option == 'Нет':
            time.sleep(2)
            planet_ice_ball_village()
    if option == '2':
        print('Из пещеры доносятся какие то звуки')
        option = input('Пойдем? Да/Нет ')
        if option == 'Да':
            print('В пещере был людоед который вас съел')
            exit()
        if option == 'Нет':
            print('Вы ушли, но одному из ваших товарищей стало интересно что там')
            print('оказалось , что там был людоед который мог вас съесть')

def planet_ice_ball_village():
    global scrap
    print('Вы вышли из пещер и наткнулись на деревню')
    print('кажется она уже давно заброшена')
    houses = 0
    while houses <= 4:
        house_number = input('В какой дом пойдем? от 1 до 7 ')
        if house_number == '1':
            houses += 1
            print('В 1 доме на стенах вы увидели чью-то слизь, больше в этом доме ничего не было')
            continue
        if house_number == '2':
            houses += 1
            print('Во 2 доме были фотографии семьи которая скорее всего когда-то тут жила')
            continue
        if house_number == '3':
            houses += 1
            print('В 3 доме ничего не было')
            continue
        if house_number == '4':
            houses += 1
            print('В 4 доме было топливо для ракеты')
            continue
        if house_number == '5':
            houses += 1
            print('В 5 доме ничего не было, но был спуск в подвал')
            print('Дверь заперта и чтобы её открыть нужен лом')
            if scrap == 'есть':
                option = input('будем открывать дверь? Да/Нет ')
                if option == 'Да':
                    print('Лом был потрачен, а в подвале был мутирующий пёс который загрыз вас')
                    exit()
                if option == 'Нет':
                    print('Вы вышли из дома так и не узнав что там было')
                    continue
            if scrap == 'нету':
                print('Вы вышли из дома так и не узнав что там было')
                continue
        if house_number == '6':
            houses += 1
            print('В 6 доме ничего не было')
            continue
        if house_number == '7':
            houses += 1
            print('Принт в доме было растение, которое плевалось льдом и вы были заморожены насмерть')
            exit()
    print('Поздравляю! Вы изучили планету, а теперь отправляетесь обратно домой, миссия выполнена')
    event_aliens()
    
    
def pusk():
    num = 5
    for i in range(6):
        print('До взлёта', num)
        num = num - 1
        time.sleep(1)

def start_game():
    name = input('Назовите ваше имя ')
    print(f'Привет {name}, ты и команда взлетаете и отпрявляетесь на планету под названием "Ледяной шар"')
    input('нажми Enter для начала')
    pusk()
    print('вы взлетели')
    time.sleep(2)
    os.system('cls')
    event_meteorite()
        
def finish():
    print('Конец')
    exit()

menu()