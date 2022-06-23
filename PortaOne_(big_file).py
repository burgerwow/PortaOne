import bz2

txt_file = bz2.open('D:\PYTHON PROJECTS\PortaOne/10m.txt.bz2')

max_item = 0
min_item = 0
sum = 0
score = 0
for line in txt_file:
    line1 = int(line.decode('utf8'))
    if line1 > max_item:
        max_item = line1
    if line1 < min_item:
        min_item = line1
    sum += line1
    score += 1

txt_file.close()

print('Max: ', max_item)
print('Min: ', min_item)
print('Середнє арефметичней: ', sum / score)
