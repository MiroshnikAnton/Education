
__author__ = 'Мирошник Антон Владимирович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#def my_round(number, ndigits):     <- это обязательно использовать или в качестве примера дано?
    #pass


#print(my_round(2.1234567, 5))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))

def a(b=float(input("Введите число: "))):
    if float(b) - int(b) > 0.5:
        print(int(b) + 1)
    else:
        print(int(b))
a()

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#def lucky_ticket(ticket_number):     <- это обязательно использовать или в качестве примера дано?
    #pass


#print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))

def lucky_ticket(ticket_number):
    ticket_number_1 = list(str(ticket_number))
    sum_1 = int(ticket_number_1[0]) + int(ticket_number_1[1]) + int(ticket_number_1[2])
    sum_2 = int(ticket_number_1[3]) + int(ticket_number_1[4]) + int(ticket_number_1[5])
    if sum_1 == sum_2:
        return 'Билет %s счастливый' %ticket_number
    else:
        return 'Билет %s несчастливый' %ticket_number

a = int(input('Введите номер билета:'))
print(lucky_ticket(a))