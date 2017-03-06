#!/usr/bin/python
# pylint: disable=I0011,C0103,C0111
__author__ = "Tomás Sironi"
__email__ = "sironitomas@gmail.com"
__license__ = "GPL"
__version__ = "1.0.0"


def calculate(in_number):
    numberlist = []
    maximum = in_number
    iters = 0
    for j in range(0, 101):
        digits = [int(char) for char in str(maximum)]
        for d in digits:
            if d not in numberlist:
                numberlist.append(d)

        if len(numberlist) == 10:
            break

        iters = j
        maximum = maximum + in_number

    return maximum, iters


if __name__ == "__main__":
    try:
        f = open('c-input.in', 'r')
    except FileNotFoundError:
        exit('File not found')

i = 1
for line in f:
    n = int(line)
    x, iterations = calculate(n)
    print('Case #' + str(i) + ': ', end='')
    if iterations < 100:
        print(str(x))
    else:
        print('INSOMNIA')
    i += 1
