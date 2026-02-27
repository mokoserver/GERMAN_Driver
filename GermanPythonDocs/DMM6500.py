import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# RU: Тут собраны  команды для драйвера DMM6500
#    RU: Команда инициализации драйвера DMM6500
MOKO.Driver('DMM6500', 'init')

#    RU: Команда иутсановки таймаута для прибора DMM6500
MOKO.Driver('DMM6500', 'set', 'Timeout = 1000')

#    RU: Команда сброса настроек прибора DMM6500
MOKO.Driver('DMM6500', 'set', 'RESET')

#     RU: Команда установки функции измерения драйвера DMM6500 ("Func" или "Function")
MOKO.Driver('DMM6500', 'set', 'Function = VDC')
MOKO.Driver('DMM6500', 'set', 'Function = VAC')
MOKO.Driver('DMM6500', 'set', 'Function = IDC')
MOKO.Driver('DMM6500', 'set', 'Function = IAC')
MOKO.Driver('DMM6500', 'set', 'Function = R')
MOKO.Driver('DMM6500', 'set', 'Function = R2')
MOKO.Driver('DMM6500', 'set', 'Function = R2WI')
MOKO.Driver('DMM6500', 'set', 'Function = R4')
MOKO.Driver('DMM6500', 'set', 'Function = R4WI')
MOKO.Driver('DMM6500', 'set', 'Function = F')
MOKO.Driver('DMM6500', 'set', 'Function = C')
MOKO.Driver('DMM6500', 'set', 'Function = CAP')

#     RU: Команда установки диапазона измерений DMM6500
MOKO.Driver('DMM6500', 'set', 'Range = 100')
MOKO.Driver('DMM6500', 'set', 'Range = Auto')
MOKO.Driver('DMM6500', 'set', 'Range = MIN')
MOKO.Driver('DMM6500', 'set', 'Range = MAX')

#     RU: Команда установки разрешения DMM6500 ("Res" или "Resolution")
MOKO.Driver('DMM6500', 'set', 'Resolution = 100')
MOKO.Driver('DMM6500', 'set', 'Resolution = MAX')
MOKO.Driver('DMM6500', 'set', 'Resolution = MIN')

#     RU: Команда установки времени измерения DMM6500 ("Aper", "Aperture" или "MeasTime")
MOKO.Driver('DMM6500', 'set', 'Aperture = 1')
MOKO.Driver('DMM6500', 'set', 'Aperture = OFF')

#     RU: Команда установки времени интеграции DMM6500 ("IntegrationTime", "IntTime" или "NPLC")
MOKO.Driver('DMM6500', 'set', 'IntegrationTime = 1')
MOKO.Driver('DMM6500', 'set', 'IntegrationTime = MAX')
MOKO.Driver('DMM6500', 'set', 'IntegrationTime = MIN')

###################################################### ("ACBand", "ACBandwidth", "Band" или "Bandwidth")
MOKO.Driver('DMM6500', 'set', 'Bandwidth = 1')
MOKO.Driver('DMM6500', 'set', 'Bandwidth = MAX')
MOKO.Driver('DMM6500', 'set', 'Bandwidth = MIN')

###################################################### ("AutoZero" или "ZERO")
MOKO.Driver('DMM6500', 'set', 'AutoZero = ON')
MOKO.Driver('DMM6500', 'set', 'AutoZero = OFF')
MOKO.Driver('DMM6500', 'set', 'AutoZero = ONCE')

###################################################### ("LOWPOWER")
MOKO.Driver('DMM6500', 'set', 'LOWPOWER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('DMM6500', 'set', 'LOWPOWER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("VOLTAGELIMITED")
MOKO.Driver('DMM6500', 'set', 'VOLTAGELIMITED = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('DMM6500', 'set', 'VOLTAGELIMITED = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("FILT" или "FILTER")
MOKO.Driver('DMM6500', 'set', 'FILTER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('DMM6500', 'set', 'FILTER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("SND" или "Sound")
MOKO.Driver('DMM6500', 'set', 'Sound = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('DMM6500', 'set', 'Sound = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

#    RU: Команда сброса настроек прибора DMM6500
MOKO.Driver('DMM6500', 'set', 'RESET')

#    RU: Данная команда считывает значение из прибора DMM6500 и возвращает его в строчном виде
Value = MOKO.Driver('DMM6500', 'get', 'READ')

Timeout = MOKO.Driver('DMM6500', 'get', 'TIMEOUT')


