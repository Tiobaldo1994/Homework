# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def qive_card():
    card = input('Введите номер карты')
    print('**** **** ****',card[-4:])
qive_card()

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom():
    word = input('Напишите проверочное слово')
    if word == word[::-1]:
        print(f'Слово: "{word}" палиндром')
    else:
        print(f'Слово: "{word}" не палиндром')
palindrom()

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:

    states = {0: 'цветок', 1:'зеленый', 2:'созревающий', 3:'спелый'}#статическое свойство

    def __init__(self, index):
        self._index = index #индекс томата из списка томатов?
        self._state = 0

    def grow(self):
        if self._state <= 2:
            print(f'Этот помидор еще дозревает, он находится на стадии:{self.states[self._state]}')
            self._state+=1
            print(f'Но мы его полили, теперь он уже {self.states[self._state]}')
        else:
            print('Этот томат уже спелый')

    def is_ripe(self):
        if self._state == 3:
            print('Ваш томат созрел')
        else:
            print('Томату нужно дозреть')

tomat_1 = Tomato(1)
tomat_1.grow()
tomat_2 = Tomato(2)
tomat_2.grow()
tomat_2.grow()
tomat_3 = Tomato(3)
tomat_3.grow()
tomat_3.grow()
tomat_3.grow()
tomat_4 = Tomato(2)
tomat_4.grow()
tomat_4.grow()
tomat_5 = Tomato(1)
tomat_5.grow()
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(0,count)]

    def grow_all(self):
        for pomidor in self.tomatoes:
            return pomidor.grow()

    def all_are_ripe(self):
        for pomidor in self.tomatoes:
            return pomidor.is_ripe()

    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes.clear()
bush_1 = TomatoBush(8)
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству
class Gardener:

    def __init__(self, name):
        self.name = name
        self._plant = Tomato(1)#принимает объект класса томатооооо

    def work(self):
        self._plant.grow()#по идеее должен раститььььь томааааатыыыыыы ааааааааа

    def harvest(self):
        if self._plant.is_ripe():
            self._plant.give_away_all()

    def knowledge_base(self):
        print(f'Мы выращиваем помидоры. Работает садовод {self.name}')

sadovnik = Gardener('Игорь')
sadovnik.knowledge_base()

# tomat_1.is_ripe()
# tomat_2.is_ripe()
# tomat_3.is_ripe()
# tomat_4.is_ripe()
# tomat_5.is_ripe()
kust = TomatoBush(9)
kust.grow_all()
kust.grow_all()
kust.grow_all()
kust.grow_all()
kust.all_are_ripe()
kust.give_away_all()
sadovnik.work()
sadovnik.harvest()
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
