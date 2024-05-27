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


def randoms():

    words_list = ['apple']
    random_word = rn.choice(words_list)

    return random_word


randoms()


def wonder_field():
    random_value = randoms()

    number_of_attempts = int(input('How many attempts do you want? Enter number:'))

    while number_of_attempts:

        word_or_letter = input('Enter a word or letter: ').lower()

        if word_or_letter == random_value:
            print(f'You guessed {random_value}')
            break
        elif len(word_or_letter) > 1 and word_or_letter != random_value:
            print('Try again')
            number_of_attempts -= 1

        if len(word_or_letter) == 1:
            if word_or_letter in random_value:
                guessed_word.append(word_or_letter)
                print('You guessed letter ')
                number_of_attempts -= 1
            else:
                number_of_attempts -= 1

        elif number_of_attempts == 0:
            return 'You lost'


guessed_word = []

wonder_field()


def word(guessed_word):

    return ''.join(letter if letter in guessed_word else '*' for letter in guessed_word)


print(word(guessed_word))




