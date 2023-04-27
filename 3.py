import random
import math

#1
def ramka(text):
    s = len(text)
    print(f"""+ {s* '-'} +\n| {text} |\n+ {s * '-'} +
                """)
ramka(input())

#2
def function(a,b):
    suma = a + b
    print('Всього', suma, 'шт.')
    return a,b

print('Скільки бананів і ананасів для мавп?')
function(int(input()), int(input()))
print('Скільки жуків і червяків для їжаків?')
function(int(input()), int(input()))
print('Скільки риб і молюсків для видр?')
function(int(input()), int(input()))

#3
def piramida():
    a = float(input('Введіть довжину сторони основи: '))
    h = float(input('Введіть висоту піраміди: '))
    S = (3 * math.sqrt(3) / 2) * (a ** 2)
    V = (3/2) * S * h
    return V
print(round(piramida(),2))

#4
symb1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb2 = '~!@#$%^&*()_-+={}[]|\<>,.?/'
symb3 = '0123456789'
variant = int(input('Введіть рівень складності пароля від 1 - 3: '))
if variant < 1 or variant > 3:
    print('Помилка!')
elif variant == 1:
    def level_1(l):
        l4 = symb1.lower() + symb3
        print("Ваш пароль: ",''.join([random.choice(l4) for i in range(l)]))
    level_1(abs(int(input('Введіть довжину пароля: '))))

elif variant == 2:
    def level_2(l):
        l4 = symb1.lower() + symb3 + symb2
        print("Ваш пароль: ",''.join([random.choice(l4) for i in range(l)]))
    level_2(abs(int(input('Введіть довжину пароля: '))))

elif variant == 3:
    def level_3(l):
        l4 = symb1.lower() + symb1.upper() + symb3 + symb2
        print("Ваш пароль: ",''.join([random.choice(l4) for i in range(l)]))
    level_3(abs(int(input('Введіть довжину пароля: '))))

