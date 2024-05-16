import time
from random import randint
import os

times = time.time()
speed = 0
enduranc = 100
fuel = 1000
inv = []
events = ['event_meteorite', 'event_aliens']

def menu():
    global fuel
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                           ┃         _          ┃
    ┃                           ┃        ╱ ╲         ┃
    ┃                           ┃       ╱   ╲        ┃
    ┃     1 - НАЧАТЬ ИГРУ       ┃      ╱ ( ) ╲       ┃
    ┃                           ┃      │     │       ┃
    ┃                           ┃      | ( ) |       ┃
    ┃     2 - НАСТРОЙКИ         ┃      |     |       ┃
    ┃                           ┃      | ( ) |       ┃
    ┃                           ┃      |     |       ┃
    ┃     3 - ЗАКОНЧИТЬ ИГРУ    ┃     /       \      ┃
    ┃                           ┃    /         \     ┃
    ┃                           ┃   /           \    ┃
    ┃                           ┃  ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_menu = input('Что выбераем? ')
    if option_menu == '1':
        start_game()
    if option_menu == '2':
        settings()
    if option_menu == '3':
        print('Игра окончена')
        exit()

def event_meteorite():
    os.system('cls')
    global fuel
    print('О нет, на вас летят метеориты, чтобы отбить их правильно отвечай на вопросы')
    time.sleep(2)
    answer_1 = input('Вопрос 1: сколько будет если -6*12? ')
    if answer_1 == '-72':
        print('Молодец!')
        time.sleep(2)
        answer_2 = input('Вопрос 2: сколько будет если 1005/5? ')
        if answer_2 == '201':
            print('Молодец!')
            time.sleep(2)
            answer_3 = input('Вопрос 2: сколько будет 20% от 15? ')
            if answer_3 == '3':
                print('Молодец! Ты смог отбить метеориты')
                fuel -= 100
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
        planet()
    if option == '2':
        print('Вы подлетели ближе к НЛО и они запустили по вам огонь')
        print('Ракета взорвалась')
        exit()
    if option == '3':
        print('Вы стали стрелять по НЛО и они запустили по вам огонь')
        print('Ракета взорвалась')
        exit()

def event():
    global events 
    number_event = randint(0, len(events)- 1)
    next_event = (events[number_event])
    if next_event == 'event_meteorite':
        event_meteorite()
        index = events.index('event_meteotite')
        events.pop(index)
    elif next_event == 'event_aliens':
        event_aliens()
        index = events.index('event_aliens')
        events.pop(index)

def planet():
    planets = ['"Ледяной шар"', '"Огненная сфера']
    number_planet = randint(0, len(planets)- 1)
    next_planet = (planets[number_planet])
    if next_planet == '"Ледной шар"':
        planet_ice_ball()
        index = planet.index('Ледяной шар')
        planet.pop(index)

def planet_ice_ball():
    print('Вы приземлились на планету "Ледяной шар"')
    print('''
               Характеристики
           Климат - суровая зима
        Средняя температура - -150'с 
         живые существа - неизвестно
        
               Цель прибывания
            1. Иследовать планету
            2. Добыть топливо
            3. Найти ресурсы

            Текущее время 09:00
''')
    print('Да или Нет')
    input('Готовы отправиться на исследовние?')
    print('В любом случае мы отправляемся')
    os.system('cls')
    run = 'Да'
    num = 0
    while run == 'Да':
        option = input('По пути вы встретили 3 пещеры, в какую пойдем? 1/2/3')
        if option == '1':
            option = input('Поздравляю вы нашли в этой пещере ящик, будете вскрывать? Да/Нет')
            if option == 'Да':
                print('В ящике был лом и пистолет с 10 патронами')
                num += 1
                continue
            if option == 'Нет':
                print('Вы ушли ')
        
    
def start_game():
    name = input('Назовите ваше имя ')
    print(f'Привет {name}, прям сейчас ты и команда взлетаете и отпрявляетесь на планету под названием "Ледяной шар"')
    input('нажми Enter для начала')
    time.sleep(5)
    os.system('cls')
    event()


def settings():
    print('В разработке')

def finish():
    print('Конец')
    exit()

menu()