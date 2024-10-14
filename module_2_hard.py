def rebus(num):
    rebus = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                rebus += str(i) + str(j)
    return rebus

print('Введите число: ')
print(rebus(int(input())))