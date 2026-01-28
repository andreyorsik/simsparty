import time
import random

# 1. Базовый класс

class Sim:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.is_alive = True

    def eat(self):
        if self.hunger >= 100:
            print(f'{self.name} не хочет есть.')
        else:
            self.hunger += 20
            self.energy -= 5
            print(f'{self.name} поел(а). Голод: {self.hunger}.')

    def live_day(self):
        self.hunger -= 10
        self.energy -= 10
        if self.energy <= 0:
            self.is_alive = False
            print(f'{self.name} не выдержал суровой жизни и покинул чат.')

    def status(self):
        return f'{self.name} | Голод: {self.hunger} | Энергия: {self.energy}.'


# 2.Наследственный класс

class Human(Sim):
    def __init__(self, name, job):
        super(). __init__(name)
        self.job = job
        self.money = 50

    def work(self):
        self.energy -= 30
        self.hunger -= 20
        self.money += 100
        print(f'{self.name} сходил на работу ({self.job}). +100$. Энергия: {self.energy}.')

# Взаимодействие: человек кормит кого-то(Связь объектов!)

    def feed_pet(self, pet):
        if self.money >= 20:
            print(f'{self.name} покупает корм и кормит {pet.name}.')
            self.money -= 20
            pet.eat()
        else:
            print(f'У {self.name} нет денег на корм! Иди работай!')

    def repair_robot(self, robot):
        print(f'{self.name} чинит {robot.name}')
        self.energy -= 20
        robot.energy = 100
        print(f'{robot.name} полностью заряжен!')


class Dog(Sim):
    def eat(self):
        self.hunger += 30
        print(f'{self.name} жадно грызет кость!')

    def play(self, human):
        print(f'{self.name} приносит мячик {human.name}')
        self.energy -= 20
        human.energy += 10
        print(f'{human.name} повеселел!')


class Robot(Sim):
    def __init__(self, name):
        super().__init__(name)
        self.is_alive = True
        self.battery = 100

    def live_day(self):
        self.energy -= 5

    def eat(self):
        print(f'{self.name} заряжается.')
        self.energy = 100

    def cook_dinner(self, human):
        if self.energy > 20:
            print(f'{self.name} готовит ужин для {human.name}')
            self.energy -= 20
            human.eat()
        else:
            print(f'{self.name}: БАТАРЕЯ РАЗРЯЖЕНА! НЕ МОГУ ГОТОВИТЬ!')


class Computer(Robot):
    def repair_computer(self):
        self.energy = 100
        print(f'{self.name} зарядил ноутбук')

    def use(self):
        self.battery -= 20
        print('\n Что хотите  сделать?')
        print('Скачать новую игру(1)')
        print('Удалить игру(2)')
        print('Поиграть в игру(3)')
        print('Посмотреть сериал(4)')
        print('Заняться программированием(5)')
        print('Встать из-за компьютера(0)')

        choice1 = input('Твой выбор:')
    if choice1 == '1':
        energy -= 10
        print(f'{self.name} скачал новую игру')
    elif choice1 == '2':
        energy -= 5
        print(f'{self.name} удалил игру')
    elif choice1 == '3':
        energy -= 10
        print(f'{self.name} начал играть в игру')
    elif choice1 == '4':
        energy -= 10
        print(f'{self.name} начал смотреть сериал')
    elif choice1 == '5':
        energy -= 10
        print(f'{self.name} пишет код')


# 3. Игровой мир(сценарий)

player = Human('Алекс', 'Программист')
doggo = Dog('Бобик')
robot = Robot('Пожиратель гипервселенных')
comp = Computer('Компьютер Алекса')


household = [player, doggo, robot, comp]
day = 1

print('ДОБРО ПОЖАЛОВАТЬ В SIMS')


# 4. Игровой цикл(game loop)
while True:
    print(f'\n ДЕНЬ {day}')

    game_over = False
    for Sim in household:
        if not Sim.is_alive:
            print(f'Игра окончена: {Sim.name} погиб.')
            game_over = True
    if game_over:
        break

    print(f'Денги: {player.money}')
    for sim in household:
        print(sim.status())

    print('\n Что будет делать Алекс?')
    print('1.Пойти на работу')
    print('2.Поесть самому')
    print('3.Покормить Бобика')
    print('4.Поиграть с Бобиком')
    print('5.Попросить робота приготовить ужин')
    print('6.Починить робота')
    print('7.Сесть за компьютер')
    print('8.Выход')


    choice = input('Твой выбор:')

    if choice == '1':
        player.work()
    elif choice == '2':
        if player.money >= 20:
            player.money -= 20
            player.eat()
        else:
            print('Нет денег!')
    elif choice == '3':
        player.feed_pet(doggo)
    elif choice == '4':
        doggo.play(player)
    elif choice == '5':
        robo.cook_dinner(player)
    elif choice == '6':
        player.repair_robot(robot)
    elif choice == '7':


            print('\n Что хотите  сделать?')
            print('Скачать новую игру(1)')
            print('Удалить игру(2)')
            print('Поиграть в игру(3)')
            print('Посмотреть сериал(4)')
            print('Заняться программированием(5)')
            print('Встать из-за компьютера(0)')

            choice1 = input('Твой выбор:')

            if choice1 == '1':
                energy -= 10
                print(f'{self.name} скачал новую игру')
            elif choice1 == '2':
                energy -= 5
                print(f'{self.name} удалил игру')
            elif choice1 == '3':
                energy -= 10
                print(f'{self.name} начал играть в игру')
            elif choice1 == '4':
                energy -= 10
                print(f'{self.name} начал смотреть сериал')
            elif choice1 == '5':
                energy -= 10
                print(f'{self.name} пишет код')

        break
    else:
        print('Неверная команда, день прошел впустую...')

    print('\n Наступает ночь...Все показатели падают.')
    time.sleep(1)
    for Sim in household:
        Sim.live_day()

    day += 1














