'''
2. Длина МКАД – 109 километров. Байкер Вася стартует с нулевого километра МКАД и едет со скоростью 𝑣 километров в час. 
На какой отметке он остановится через 𝑡 часов? Значения скорости и времени считаются целыми числами.
'''

V = int(input('Скорость байка (км/ч): '))
S = 109 #км МКАД
t = int(input('Через сколько часов байк остановится: '))
bike_S = V * t % S # пройденное расстояние + учет возможности проезда нескольких кругов

print('Спустя', t, 'ч. байк остановится на', bike_S, 'км')