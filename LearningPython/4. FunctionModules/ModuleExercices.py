def fibonacci(term):
    if term == 1 or term == 2:
        return 1
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)


def numberCheck(number):
    perfect = 0
    aux = number - 1
    while aux >= 1:
        if number % aux == 0:
            perfect += aux

        aux -= 1

    if number == perfect:
        return True
    else:
        return False


def numberLimit(number):
    print('List of perfect numbers until %d :' % number)

    aux_number = 1
    while aux_number <= number:
        if numberCheck(aux_number):
            print(aux_number, end=' ')

        aux_number += 1
