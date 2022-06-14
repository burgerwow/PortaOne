import bz2

bz_file = bz2.BZ2File('10m.txt.bz2')
line_list = bz_file.readlines()
a = []

for i in line_list:
    a.append(int(i.decode('utf8')))

b = a.copy()  # медіана
b.sort()
long = len(b)

x = b[len(b) // 2]
y = b[len(b) // 2 - 1]

if long % 2 == 0:
    print('медіана: ', (x + y) * 0.5)
elif long % 2 == 1:
    print('медіана: ', x)

print('максимальне число в файлі: ', max(a))
print('мінімальне число в файлі: ', min(a))
print('середнє арифметичне значення: ', sum(a) / (len(a)))

c_plus = []  # список який збільшується
cmax = []
for i in range(0, len(a) - 1):
    if a[i] < a[i + 1]:
        c_plus.append(a[i])
    elif a[i] >= a[i + 1]:
        if len(c_plus) > len(cmax):
            cmax = c_plus.copy()
        c_plus.clear()

c_minus = []  # список який зменшується
cmin = []
for i in range(0, len(a) - 1):
    if a[i] > a[i + 1]:
        c_minus.append(a[i])
    elif a[i] <= a[i + 1]:
        if len(c_minus) > len(cmin):
            cmin = c_minus.copy()
        c_minus.clear()

print('Найбільша послідовність чисел, яка збільшується: ', cmax)
print('Найбільша послідовність чисел, яка зменшується: ', cmin)