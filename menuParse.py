import csv

fin = open('./input/Saminboon_notes - 메뉴.csv', 'r', encoding='utf-8')
fout = open('./input/menuList.txt', 'w', encoding='utf-8')

reader = csv.reader(fin)

menuList = []
for line in reader:
    fout.write('{0}, {1}, {2}, {3}\n'.format(line[1], line[3], line[4], line[5]))

fin.close()
fout.close()