f = open('task_4.txt')
line = 0
for i in f:
    line += 1
    print(i, len(i), 'симв.')
print(line, 'стр.')
f.close()

