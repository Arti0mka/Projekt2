import random
num = input('login ')
pas = ''
length = input('длина пароля?'+ "\n")
length = int(length)
for x in range(length): #Количество символов (length)
    passSymbols = '1234567890abcdefghijklmnopqrstuvwxyz' #Символы, из которых будет составлен пароль 
print('Hello, ', num, 'your password is: ', pas) 

