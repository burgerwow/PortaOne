import bz2
import statistics

bz_file = bz2.BZ2File('10m.txt.bz2')
line_list = bz_file.readlines()
a = []

for i in line_list:
    a.append(int(i.decode('utf8')))


def max_item():
    print('Найбільше число у списку: ', max(a))


def min_item():
    print('Найменше число у списку: ', min(a))


def mediana():
    long = len(a)
    index = long // 2
    if long % 2 == 0:
        return sum(sorted(a)[index - 1: index + 1]) / 2
    elif long % 2 == 1:
        return sorted(a)[index]


def mediana_stat():
    print('Медіана статистика: ', statistics.median(sorted(a)))


def middle():
    print('Середнє арефметичне: ', sum(a) / (len(a)))


def c_increase():
    c_plus = []  # список який збільшується
    cmax = []
    for i in range(0, len(a) - 1):
        if a[i] < a[i + 1]:
            c_plus.append(a[i])
        elif a[i] >= a[i + 1]:
            if len(c_plus) > len(cmax):
                cmax = c_plus.copy()
            c_plus.clear()
    return (cmax)


def c_decreases():
    c_minus = []  # список який зменшується
    cmin = []
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            c_minus.append(a[i])
        elif a[i] <= a[i + 1]:
            if len(c_minus) > len(cmin):
                cmin = c_minus.copy()
            c_minus.clear()
    return (cmin)


max_item()
min_item()
print('Медіана (функція): ', mediana())
mediana_stat()
middle()
print('Найбільша послідовність, яка збільшується: ', c_increase())
print('Найбільша послідовність, яка зменшується ', c_decreases())
