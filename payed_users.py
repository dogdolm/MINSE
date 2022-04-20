def check(login):
    file = open('payed.txt', 'r')
    filet = list(file.read().split())
    file.close()
    if login in filet:
        if filet[filet.index(login) + 1] == 'lite':
            return "lite"
        elif filet[filet.index(login) + 1] == "standart":
            return "standart"
        else:
            return "premium"
    else:
        return False