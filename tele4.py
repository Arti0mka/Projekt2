import random
num = input('login ')
pas = ''
length = input('длина пароля?'+ "\n")
length = int(length)
for x in range(length): #Количество символов (length)
    pas = pas + random.choice(list('1234567890abcdefghijklmnopqrstuvwxyz')) #Символы, из которых будет составлен пароль
    pas = input('Введите символы которые хотите использовать?'+ "\n")
    pas = (pas) 
print('Hello, ', num, 'your password is: ', pas) 

