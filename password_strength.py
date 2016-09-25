import string
import os


def check_pass_is_date_or_digits(password):
    password = ''.join(ch for ch in password if ch not in string.punctuation)
    password = ''.join(ch for ch in password if ch not in string.digits)
    return not password


def check_pass_is_letters(password):
    password = ''.join(ch for ch in password if ch not in string.ascii_letters)
    return not password


def check_pass_is_punctuation(password):
    password = ''.join(ch for ch in password if ch not in string.punctuation)
    return not password


def check_pass_in_blacklist(password):
    with open('10_million_password_list_top_1000000.txt') as blacklist:
        for passw in blacklist:
            if password == passw.rstrip():
                return True
    return False


def check_pass_contains_lower_and_upper_case(password):
    lower_case, upper_case = False, False
    for ch in password:
        if ch.isupper():
            upper_case = True
        if ch.islower():
            lower_case = True
    return lower_case and upper_case


def check_pass_contains_punctuation(password):
    for ch in password:
        if ch in string.punctuation:
            return True
    return False


def check_pass_contains_digits(password):
    for ch in password:
        if ch in string.digits:
            return True
    return False


def get_password_strength(password):
    strength = 1
    if check_pass_is_date_or_digits(password):
        return strength
    if check_pass_is_letters(password):
        return strength
    if check_pass_is_punctuation(password):
        return strength
    if check_pass_in_blacklist(password):
        return strength
    if len(password) < 8:
        return strength

    if len(password) >= 8:
        strength += 1
    if len(password) >= 14:
        strength += 1
    if len(password) >= 20:
        strength += 1
    if check_pass_contains_lower_and_upper_case(password):
        strength += 2
    if check_pass_contains_punctuation(password):
        strength += 2
    if check_pass_contains_digits(password):
        strength += 2

    return strength


if __name__ == '__main__':
    if not os.path.exists('10_million_password_list_top_1000000.txt'):
        os.system('wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000000.txt')
    print('Введите пароль: ')
    password = input()
    print(get_password_strength(password))
