### 1 Напишіть функцію, яка приймає список чисел і повертає новий список, в якому всі числа помножені на 2.
def multiple_lst(lst1):
    lst2 = [el * 2 for el in lst1]
    return lst2


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(multiple_lst(lst1))

###2 Напишіть функцію, яка приймає рядок і повертає кількість голосних літер у цьому рядку.
def func_wolves(line):
    wolves = ('a','o','y','u','i','e')
    count = 0
    for ch in line:
        if ch in wolves:
            count += 1
    print(count)


line = 'hello world'
func_wolves(line)

### 3 Напишіть функцію, яка приймає список чисел і повертає список, що містить лише парні числа.
num_list = [2, 56, 5, 74, 33, 52, 45, 9, 8, 7, 23, 45]
filtering_list = filter(lambda x: x % 2 == 0, num_list)
print(list(filtering_list))

### 4 Напишіть функцію, яка приймає рядок і повертає його у зворотньому порядку (саме слова, як показано в прикладі).
def funct_reverse(str1):
    return str1.split()[::-1]


str1 = 'Hello world'
print(' '.join(funct_reverse(str1)))

###  У вас є список чисел, вам потрібно створити новий список, який буде мати лише унікальні значення зі списку 1
list_num = [5,4,23,58,69,25,22,22,7,5,5,9,3,1,5,1]
unique_num = list({elem for elem in list_num})
print(unique_num)


### У вас є два словники, dict1 і dict2, кожен з яких містить інформацію про людей. dict1 має ключі ім'я, прізвище та вік, а dict2 має ключі телефон, email та стать.
# # Напишіть программу, яка об'єднує ці два словники в один словник для кожної людини, зберігаючи всю інформацію в одному місці.

dict1 = {'ім\'я': 'Іван', 'прізвище': 'Петров', 'вік': 25}
dict2 = {'телефон': '123-456-7890', 'email': 'ivan@example.com', 'стать': 'чоловіча'}
union_dict = {**dict1, **dict2}
print(union_dict)


###У вас є 2 кортежи, ваша задача повернути кортеж у якому є лише ті елементи, які є у першому кортежі та немає у другому

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
uniq_tuple = ()
for element in tuple1:
    if element not in tuple2:
        uniq_tuple += (element,)
print(uniq_tuple)

###Напишіть програму, яка отримує на вхід рядок і перевіряє, чи є він паліндромом.
# # Паліндром - це рядок який читається однаково з початку до кінця і з кінця у початок. Реєстр літер потрібно ігнорувати, вам допоможе метод .lower()
palindrome = input("Enter a palindrome: ").lower()
is_palindrome = palindrome[::-1]

if is_palindrome == palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


####Напишіть програму яка приймає на вхід рядок і повертає рядок де кожен символ з першого рядка буде продубльовано.
word = 'something'
double_word = [char * 2 for char in word]
print(''.join(double_word))

###Напишіть програму, яка запитує у користувача число і виводить усі числа від 1 до цього числа. Однак, якщо число ділиться на 3, виведіть "Fizz" замість числа. Якщо число ділиться на 5,
# # виведіть "Buzz" замість числа. Якщо число ділиться і на 3, і на 5, виведіть "FizzBuzz" замість числа. Рішення цієї задачі має бути за допомогою циклу while!

num = int(input("Enter a number: "))

while num > 0:
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
        num -= 1

###Написати программу яка буде виводити сумму всіх чисел з 1 до 100 які діляться на ціло на 3 але не діляться на 5

add_num = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        add_num += i
    else:
        continue
print(add_num)


###Напишіть програму, яка запитує у користувача серію чисел і виводить підсумкову суму введених чисел. Програма повинна зупинятися, коли користувач вводить від'ємне число, і виводити остаточну суму.
num = int(input("Enter a number: "))
add_num = 0
while num >= 0:
    add_num += num
    num = int(input("Enter a number: "))
    print(add_num)
print(add_num)

###Напишіть програму, яка отримує на вхід рядок і видаляє з нього усі розділові знаки. Методом replace користуватись не можна!

str1 = (' If you’ve ever wondered, “Do I need a comma here?” or “Does punctuation go inside quotations?”— \n '
        'if you’re just looking for a free grammar and punctuation checker—this page is for you.')
str2 = []

for elem in str1:
    if elem.isalnum() or elem.isspace():
        str2.append(elem)
    else:
        continue
print(''.join(str2))
