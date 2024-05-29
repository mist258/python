# Створити програму - гру "Поле чудес".
# 1. Програма буде брати зі списку слів одне рандомне слово.
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число, якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові, та якщо є, виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає"
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.
# 7. Спроби які являється вірними не мають враховуватись в лічильнику
#
# Приклад: Програмою обрано слово "apple"
# Input:10  #(10 спроб вгадати слово)
# Input:"a"
# Output:"a****"
# Input:"d"
# Output:"Такої літери немає"
# Input:"l"
# Output:"a**l*"
# Input:"e"
# Output:"a**le"
# Input:"p"
# Output:"apple"
# Output:"Вітаю, ви вгадали слово"

import random as rn


words = ['linux']
random_word = rn.choice(words)


def wonder_field():

    guessed_letters = list()

    numbers_of_attempts = int(input('How many attempts do you want? Enter number:'))

    while numbers_of_attempts > 0:

        word_or_letter = input('Enter a word or letter: ').lower()

        if word_or_letter == random_word:
            print(f'You\'ve guessed word - {random_word}')
            break
        elif word_or_letter != random_word and len(word_or_letter) > 1:
            print('You don\'t guessed the word')
            numbers_of_attempts -= 1

        if len(word_or_letter) == 1:

            if word_or_letter not in random_word:
                print(f'{word_or_letter} is wrong letter, try next time')
                numbers_of_attempts -= 1

            if word_or_letter in random_word:
                guessed_letters.append(word_or_letter)
                print(f'You\'ve  guessed letter - {word_or_letter}')
                numbers_of_attempts -= 1

        guessed_word = ''.join([letters if letters in guessed_letters else '*' for letters in random_word])
        print(guessed_word)

        if guessed_word == random_word:
            print(f'You\'ve guessed the word - {random_word}')
            break

        if numbers_of_attempts == 0 and guessed_word != random_word:
            print('Try another one')


wonder_field()
