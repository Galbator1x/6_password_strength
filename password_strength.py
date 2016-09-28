import string
import os


def check_pass_is_date_or_digits(password):
    return not set(password).difference(set(string.digits), set(string.punctuation))


def check_pass_is_letters(password):
    return not set(password).difference(set(string.ascii_letters))


def check_pass_is_punctuation(password):
    return not set(password).difference(set(string.punctuation))


def check_pass_in_blacklist(password, path_to_blacklist):
    with open(path_to_blacklist) as blacklist:
        for passw in blacklist:
            if password == passw.rstrip():
                return True
    return False


def check_pass_contains_lower_and_upper_case(password):
    lowercase_letters = set(string.ascii_lowercase)
    uppercase_letters = set(string.ascii_uppercase)
    return bool(set(password).intersection(lowercase_letters)) and bool(set(password).intersection(uppercase_letters))


def check_pass_contains_punctuation(password):
    return bool(set(password).intersection(string.punctuation))


def check_pass_contains_digits(password):
    return bool(set(password).intersection(string.digits))


def get_password_strength(password, path_to_blacklist):
    strength = 1
    if check_pass_is_date_or_digits(password):
        return strength
    if check_pass_is_letters(password):
        return strength
    if check_pass_is_punctuation(password):
        return strength
    if check_pass_in_blacklist(password, path_to_blacklist):
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
    path_to_blacklist = '10_million_password_list_top_1000000.txt'
    if not os.path.exists(path_to_blacklist):
        os.system('wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000000.txt')
    password = input('Enter the password: ')
    print(get_password_strength(password, path_to_blacklist))
