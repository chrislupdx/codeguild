from operator import itemgetter
import datetime

def open_text(taborrain, enc='utf-8'):
    with open(taborrain, 'r', encoding='utf-8') as f:
        return f.readlines()

dates = []

lst = open_text('taborrain.txt')
for i in lst[11:20]:
    dates.append(datetime.datetime.strptime(i[:11], '%d-%b-%Y'))

for i in dates:
    print(i.year)
    print(i.month)

# data = datetime.datetime.strptime('')
