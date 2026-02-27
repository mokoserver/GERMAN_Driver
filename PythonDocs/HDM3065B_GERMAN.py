import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# RU: Тут собраны  команды для драйвера HDM3065B_GERMAN
#    RU: Команда инициализации драйвера HDM3065B_GERMAN
MOKO.Driver('HDM3065B_GERMAN', 'init')

MOKO.Driver('HDM3065B_GERMAN', 'set', 'Timeout = 1000')

#     RU: Команда установки функции измерения драйвера HDM3065B_GERMAN ("Func" или "Function")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = VDC')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = VAC')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = IDC')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = IAC')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = R')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = R2')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = R2WI')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = R4')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = R4WI')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = F')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = C')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Function = CAP')

#     RU: Команда установки диапазона измерений HDM3065B_GERMAN
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Range = 100')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Range = Auto')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Range = MIN')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Range = MAX')

#     RU: Команда установки разрешения HDM3065B_GERMAN ("Res" или "Resolution")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Resolution = 100')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Resolution = MAX')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Resolution = MIN')

#     RU: Команда установки времени измерения HDM3065B_GERMAN ("Aper", "Aperture" или "MeasTime")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Aperture = 1')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Aperture = OFF')

#     RU: Команда установки времени интеграции HDM3065B_GERMAN ("IntegrationTime", "IntTime" или "NPLC")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'IntegrationTime = 1')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'IntegrationTime = MAX')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'IntegrationTime = MIN')

###################################################### ("ACBand", "ACBandwidth", "Band" или "Bandwidth")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Bandwidth = 1')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Bandwidth = MAX')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Bandwidth = MIN')

###################################################### ("AutoZero" или "ZERO")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'AutoZero = ON')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'AutoZero = OFF')
MOKO.Driver('HDM3065B_GERMAN', 'set', 'AutoZero = ONCE')

###################################################### ("LOWPOWER")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'LOWPOWER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'LOWPOWER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("VOLTAGELIMITED")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'VOLTAGELIMITED = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'VOLTAGELIMITED = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("FILT" или "FILTER")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'FILTER = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'FILTER = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

###################################################### ("SND" или "Sound")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Sound = ON')  # (допустимы значения "ON" "1", "EN", "ENABLE")
MOKO.Driver('HDM3065B_GERMAN', 'set', 'Sound = OFF') # (допустимы значения "OFF" "0", "DIS", "DISABLE")

#    RU: Команда сброса настроек прибора HDM3065B_GERMAN
MOKO.Driver('HDM3065B_GERMAN', 'set', 'RESET')

#    RU: Данная команда считывает значение из прибора HDM3065B_GERMAN и возвращает его в строчном виде
Value = MOKO.Driver('HDM3065B_GERMAN', 'get', 'READ')

Timeout = MOKO.Driver('HDM3065B_GERMAN', 'get', 'TIMEOUT')


