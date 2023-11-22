sec = input('Введите количество секунд')
sec = int(sec)

hour = sec // 3600
minute = sec % 3600 // 60
sec2 = sec % 3600 - (minute * 60)

print(f'В указанном количестве секунд ({float(sec)}):'
 f'\n Часов:{hour}'
 f'\n Минут:{minute}'
 f'\n Секунд:{sec2}')

cel = float(input('Введите температуру по Цельсию'))

calvin = cel * 274.15

far = cel * 33.8

reom = cel * 0.8

print (f'В указанном количестве градусов цельсия:{cel}°C:'
f'\n Градусов Кельвина: {round(calvin, 2)}К'
f'\n Градусов Фаренгейта: {round(far, 2)}°F'
f'\n Градусов Реомюра: {round(reom, 2)}°R')