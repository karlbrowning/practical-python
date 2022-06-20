# pcost.py
#
# Exercise 1.27

# from asyncore import read

from pickletools import read_float8


total_cost = 0.0

with open('C:\\Users\\browningk\\Documents\\GitHub\\practical-python\\Work\\Data\\portfolio.csv', 'rt') as read_data_file:
    headers = next(read_data_file)
    for line in read_data_file:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price

print('Total cost', total_cost)
