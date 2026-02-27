import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# RU: Тут собраны  команды для драйвера HP34401A_GERMAN
#    RU: Команда инициализации драйвера HP34401A_GERMAN
MOKO.Driver('HP34401A_GERMAN', 'init')

#    RU: Команда иутсановки таймаута для прибора HP34401A_GERMAN
MOKO.Driver('HP34401A_GERMAN', 'set', 'Timeout = 1000')

#    RU: Команда сброса настроек прибора HP34401A_GERMAN
MOKO.Driver('HP34401A_GERMAN', 'set', 'RESET')

#     RU: Команда установки функции измерения драйвера HP34401A_GERMAN ("Func" или "Function")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = VDC')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = VAC')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = IDC')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = IAC')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = R')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = R2')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = R2WI')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = R4')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = R4WI')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = F')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = TC')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = P')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = Perio')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = RTD')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = PRT')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = C')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Function = CAP')

#     RU: Команда установки диапазона измерений HP34401A_GERMAN
MOKO.Driver('HP34401A_GERMAN', 'set', 'Range = 100')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Range = Auto')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Range = MIN')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Range = MAX')

#     RU: Команда установки разрешения HP34401A_GERMAN ("Res" или "Resolution")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Resolution = 100')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Resolution = MAX')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Resolution = MIN')

#     RU: Команда установки времени измерения HP34401A_GERMAN ("Aper", "Aperture" или "MeasTime")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Aperture = 1')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Aperture = OFF')

#     RU: Команда установки времени интеграции HP34401A_GERMAN ("IntegrationTime", "IntTime" или "NPLC")
MOKO.Driver('HP34401A_GERMAN', 'set', 'IntegrationTime = 1')
MOKO.Driver('HP34401A_GERMAN', 'set', 'IntegrationTime = MAX')
MOKO.Driver('HP34401A_GERMAN', 'set', 'IntegrationTime = MIN')

###################################################### ("ACBand", "ACBandwidth", "Band" или "Bandwidth")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Bandwidth = 1')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Bandwidth = MAX')
MOKO.Driver('HP34401A_GERMAN', 'set', 'Bandwidth = MIN')

###################################################### ("AutoZero" или "ZERO")
MOKO.Driver('HP34401A_GERMAN', 'set', 'AutoZero = ON')
MOKO.Driver('HP34401A_GERMAN', 'set', 'AutoZero = OFF')
MOKO.Driver('HP34401A_GERMAN', 'set', 'AutoZero = ONCE')

###################################################### ("LOWPOWER")
MOKO.Driver('HP34401A_GERMAN', 'set', 'LOWPOWER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HP34401A_GERMAN', 'set', 'LOWPOWER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("VOLTAGELIMITED")
MOKO.Driver('HP34401A_GERMAN', 'set', 'VOLTAGELIMITED = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HP34401A_GERMAN', 'set', 'VOLTAGELIMITED = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("FILT" или "FILTER")
MOKO.Driver('HP34401A_GERMAN', 'set', 'FILTER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HP34401A_GERMAN', 'set', 'FILTER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("SND" или "Sound")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Sound = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HP34401A_GERMAN', 'set', 'Sound = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

#    RU: Команда сброса настроек прибора HP34401A_GERMAN
MOKO.Driver('HP34401A_GERMAN', 'set', 'RESET')

#    RU: Данная команда считывает значение из прибора HP34401A_GERMAN и возвращает его в строчном виде
Value = MOKO.Driver('HP34401A_GERMAN', 'get', 'READ')

Timeout = MOKO.Driver('HP34401A_GERMAN', 'get', 'TIMEOUT')


