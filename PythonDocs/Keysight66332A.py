import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# RU: Тут собраны  команды для драйвера Keysight66332A
#    RU: Команда инициализации драйвера Keysight66332A
MOKO.Driver('Keysight66332A', 'init')

MOKO.Driver('Keysight66332A', 'set', 'Timeout = 1000')

#    RU: Данная команда выставляет диапазон установки в драйвере Keysight66332A
MOKO.Driver('Keysight66332A', 'set', f'VDC = {"Value"}') # диапазон 0..20
MOKO.Driver('Keysight66332A', 'set', f'Voltage = {"Value"}')

MOKO.Driver('Keysight66332A', 'set', f'IDC = {"Value"}')
MOKO.Driver('Keysight66332A', 'set', f'CURRENT = {"Value"}')

MOKO.Driver('Keysight66332A', 'set', 'OUTPUT = ON')
MOKO.Driver('Keysight66332A', 'set', 'OUTPUT = OFF')

MOKO.Driver('Keysight66332A', 'set', 'RESET')
MOKO.Driver('Keysight66332A', 'set', 'RST')

#    RU: Данная команда считывает значение из прибора Keysight66332A и возвращает его в строчном виде
VDC = MOKO.Driver('Keysight66332A', 'get', 'VDC')
VDC = MOKO.Driver('Keysight66332A', 'get', 'VOLTAGE')

IDC = MOKO.Driver('Keysight66332A', 'get', 'IDC')
IDC = MOKO.Driver('Keysight66332A', 'get', 'CURRENT')


