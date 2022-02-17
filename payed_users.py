def check(login):
    file = open('payed.txt')
    if login in file.read():
        return True
    else:
        return False