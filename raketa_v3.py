import os 


def menu():
    os.system("cls")
    print('''   
    ┏━━━━━━━━━━━━━━━━┓
    ┃                ┃
    ┃   1 - играть   ┃
    ┃                ┃
    ┃   2 - уйти     ┃
    ┃                ┃
    ┗━━━━━━━━━━━━━━━━┛
    ''')
    option = input('Что выбрать? ')
    if option == '1':
        start_game()
    
    elif option == '2':
        finish()

def start_game():
    os.system("cls")
    print('вы сели в ракету и она взлетела')
    print('Похоже двгатель перегревается. Что нужно зделать?')
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  1 - ничего     2 - отключить двигатель     3 - отсоединить двигатель ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_engine = input( 'Что нужно зделать? ')

    if option_engine == '1':
        os.system("cls")
        print('вы решили ничего не делать')
        print('двигатель слишком сильно перегрелся и взорвался вместе с ракетой')
        print('конец № 1')
        repeat()
    if option_engine == '2':
        planet()
    elif option_engine == '3':
        os.system("cls")
        print('отсоединив двигатель вам стало не хватать мощности')
        print('''   
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃  1 - включить полную мощность     2 - использовать слабую мощность   ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        ''')
        option_power = input('что зделать? ')
    if option_power == '1':
        os.system("cls")
        print('похоже топливо кончилось')
        print('весь экипаж застрял в космосе')
        print('конец № 3')
        repeat()
    elif option_power == '2':
        os.system("cls")
        print('на слабой мощности вы смогли долететь до планеты')
        pause()
        planet()

def planet():
    os.system("cls")
    print('вы отключили двигатель')
    print('он остыл и герой продолжил полет')
    print('наконец вы долетели до планеты')
    print('Капитан говорит проверить планету')
    path()

def path():
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  1 - влево     2 - прямо     3 - вправо ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_planet = input('куда идти? ')
    os.system("cls")
    if option_planet == '1':
        option_1()
    elif option_planet == '2':
        print('вы вышли к пустой деревне')
        print('неужели здесь есть жизнь!?')
        print('вым сказали обыскать поселение')
        option_2()

def option_1():
    print('пройдя влево под вами провалилась земля')
    print('очнувшись вы были в пещере')
    print('пройдя дальше вы обнаружили сундук')
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  1 - открыть         2 - не открывать   ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_chest = input('что зделать? ')
    if option_chest == '1':
        os.system("cls")
        print('открыв сундук пещера сразу разрушилась')   
        print('похоже это ловушка')
        print('конец № 4')
        repeat()
    elif option_chest == '2':
        os.system("cls")
        print('пройдя мимо вы нашли выход')         
        print('вернувшись вы решили пойти в другое место')
        pause()
        path()

def option_2():
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  1 - дома        2 - шахту ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_village = input('что обыскать? ')
    if option_village == '1':
        os.system("cls")
        print('зайдя в один из домов вы увидели жителя')
        print('''   
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃  1 - жестами показать  2 - начать драку ┃
        ┃      что не настроен                    ┃
        ┃      воинственно                        ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        ''')
        action = input('что делать? ')
        if action == '1':
            print('житель все понял но показал что лучше уходить от сюда')
            print('рассказав всё капитану ,не поверив жителю он приказал обыскивать дальше')
            pause()
            print('спустя время в деревню вернулись жители')
            print('поняв что их дома грабятони связали всю команду')
            print('врятли вы уже выберитесь')
            print('конец № 5')
            repeat()
        elif action == '2':
            os.system("cls")
            print('житель смог отбится и закрыть вас в клетке')
            print('нужно выбратся пока остальные жители не пришли')
            print('''   
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃  1 - позвать остальную команду    2 - попытаться выбраться самому   ┃
            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            ''')
            option_preson = input('что делать')
            os.system("cls")
            if option_preson == '1':
                print('каманда вас не слышит')
                print('вы слишком далеко')
                print('последнее что вы поняли прежде чем потерять сознание')
                pause()
                os.system("cls")
                print('проснувшись вы вышли из здания')
                print('неужели вас отпустили?')
                print('"неувидев никого рядом вы пошли к ракете"')
                pause()
                os.system("cls")
                print('но её не было')
                print('вас бросили?!')
                pause()
                os.system("cls")
                print('вы очнулись')
                print('это был сон?')
                pause()
                os.system("cls")
                print('вы решили что лучше вернуться на землю')
                print('конец "№ 6')
                repeat()
            elif option_preson == '2':
                print('вы смогли выбратся')
                print('нужно проверить команду')
                print('издали вы увидели что их окружили')
                pause()
                os.system("cls")
                print('''   
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃  1 - оставить их     2 - спасти их   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                ''')                                
                option_command = input('что делать')
                if option_command == '1':
                    print('вы бросились со всех ног к кораблю')
                    print('зайдя в нутрь вам нужно было узнать как включить ракету')
                    print('''   
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃  1 - поискать подсказку     2 - использовать на угад   ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    ''') 
                    option = input('что делать')
                    if option == '1':
                        print('вы нашли подсказку и смогли вернутся на землю')
                        print('конец "№ 7')
                    elif option == '2':
                        print('похоже вы использовали не то что нужно')
                        print('ракета вышла из строя')
                        print('вы не сможете вернутся')
                        print('конец "№ 8')
            elif option_preson == '2':
                pass
    elif option_village == '3':
        os.system("cls")
        print('шахта завалена')
        pause()
        option_2()

def finish():
    os.system("cls")
    print('вы решили уйти')
    print('конец № 2')
    repeat()

def pause():
    input('---нажмите ENTER чтобы продолжить---')

def repeat():
    input('---нажмите ENTER чтобы начать заново---')
    menu()
menu()