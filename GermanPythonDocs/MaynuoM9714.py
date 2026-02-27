import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# RU: Тут собраны команды для драйвера MaynuoM9714
#    RU: Команда инициализации драйвера MaynuoM9714
MOKO.Driver('MaynuoM9714', 'init')

#    RU: Данная команда выставляет диапазон установки в драйвере MaynuoM9714
MOKO.Driver('MaynuoM9714', 'set', f'V = {"Value(Значение)"}') # диапазон 1..10
MOKO.Driver('MaynuoM9714', 'set', f'Voltage = {"Value(Значение)"}') # диапазон 1..10
MOKO.Driver('MaynuoM9714', 'set', f'UFIX = {"Value(Значение)"}') # диапазон 1..10

MOKO.Driver('MaynuoM9714', 'set', f'I = {"Value(Значение)"}')
MOKO.Driver('MaynuoM9714', 'set', f'Current = {"Value(Значение)"}')
MOKO.Driver('MaynuoM9714', 'set', f'IFIX = {"Value(Значение)"}')

MOKO.Driver('MaynuoM9714', 'set', f'R = {"Value(Значение)"}') 
MOKO.Driver('MaynuoM9714', 'set', f'Resistance = {"Value(Значение)"}')
MOKO.Driver('MaynuoM9714', 'set', f'RFIX = {"Value(Значение)"}')

MOKO.Driver('MaynuoM9714', 'set', f'P = {"Value(Значение)"}')
MOKO.Driver('MaynuoM9714', 'set', f'PFIX = {"Value(Значение)"}')
MOKO.Driver('MaynuoM9714', 'set', f'Power = {"Value(Значение)"}') 

MOKO.Driver('MaynuoM9714', 'set', 'Input = ON')   # Включение нагрузки
MOKO.Driver('MaynuoM9714', 'set', 'Input = OFF')  # Выключение нагрузки

#    RU: Данная команда считывает значение из прибора MaynuoM9714 и возвращает его в строчном виде
V = MOKO.Driver('MaynuoM9714', 'get', 'V')
V = MOKO.Driver('MaynuoM9714', 'get', 'Voltage')

I = MOKO.Driver('MaynuoM9714', 'get', 'I')
I = MOKO.Driver('MaynuoM9714', 'get', 'Current')
I = MOKO.Driver('MaynuoM9714', 'get', 'A')

R = MOKO.Driver('MaynuoM9714', 'get', 'R')
R = MOKO.Driver('MaynuoM9714', 'get', 'Resistance')
R = MOKO.Driver('MaynuoM9714', 'get', 'Ohm')

P = MOKO.Driver('MaynuoM9714', 'get', 'P')
P = MOKO.Driver('MaynuoM9714', 'get', 'Power')
P = MOKO.Driver('MaynuoM9714', 'get', 'W')

