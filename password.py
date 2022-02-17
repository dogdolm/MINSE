import hashlib


def create_account(login, password):
    passwdhash = hashlib.sha384(password.encode('utf-8'))
    del password
    file = open('passwd.txt', 'r+')
    file_was = file.read()
    if login in file_was:
        file.close()
        return 'LOGINREGISTERED:ERROR'
    else:
        file.write(' ')
        file.write(login)
        file.write(' ')
        file.write(passwdhash.hexdigest())
        file.close()
        return True


def check_password(login, entered_password):
    file = open('passwd.txt', 'r+')
    passwd_list = list(file.read().split())
    if login in passwd_list:
        true_passwdhash = passwd_list[passwd_list.index(login) + 1]
    else:
        return 'LOGINNOTREGISTERED:ERROR'
    entered_passwdhash = hashlib.sha384(entered_password.encode('utf-8'))  # Пароль, введенный пользователем
    if entered_passwdhash.hexdigest() == true_passwdhash:
        return True
    else:
        return 'PASSWDNOTRIGHT:ERROR'
