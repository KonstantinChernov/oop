# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Чернов К.В.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    def __init__(self, capacity_volume=200, occupied_volume=0):
        if not isinstance(capacity_volume, (float, int)) or not isinstance(occupied_volume, (float, int)):
            raise TypeError('Invalid type')
        if capacity_volume < 0 or occupied_volume < 0:
            raise ValueError('Invalid value')
        if capacity_volume < occupied_volume:
            raise ValueError('The capacity_volume is less than occupied one')
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f"Glass of a capacity volume {self.capacity_volume} has occupied volume {self.occupied_volume}"

    def __repr__(self):
        return f"Glass ({self.capacity_volume}, {self.occupied_volume})"

    def add_water(self, value):
        free_space = self.capacity_volume - self.occupied_volume
        if free_space < value:
            self.occupied_volume = self.capacity_volume
            print(f'{value - free_space} of water did not fit the glasses free volume. the glass is full now')
            return value - free_space
        else:
            print(f'{self.occupied_volume} of water in the glass now')
            self.occupied_volume += value
            return 0

    def remove_water(self, value):
        if self.occupied_volume < value:
            self.occupied_volume = 0
            print('there was a less water in the glass than you wanted to remove. now the glass is empty')
            return 0
        else:
            print(f'{self.occupied_volume} of water left in the glass')
            return self.occupied_volume


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        if not isinstance(occupied_volume, (float, int)):
            raise TypeError('Invalid type')
        if occupied_volume < 0:
            raise ValueError('Invalid value')
        self.occupied_volume = occupied_volume


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
  
 
class GlassDefaultListArg:
    def __init__(self, capacity_volume=200, occupied_volume = []):
        self.occupied_volume = occupied_volume.copy()
        self.capacity_volume = capacity_volume


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.



# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.




# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.



# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
	def __init__(f, a=2):
		f.a = a

	def print_me(p):
		print(p.a)

if __name__ == '__main__':
    d.print_me(d())

# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a;	

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, value,  prev=None, next_=None):
        self.value = value
        self.__prev = prev
        self.__next = next_

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if not isinstance(next_, Node):
            raise TypeError
        self.next = next_

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        if not isinstance(prev, Node):
            raise TypeError
        self.__prev = prev

    def __str__(self):
        # return f'{self}'
        return f'({Node(self.value)})'
        
    def __repr__(self):
        # return f'{self}'
        return f'({Node(self.value)})'

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...
























