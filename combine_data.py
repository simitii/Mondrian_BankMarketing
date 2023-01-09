#!/usr/bin/env python
# coding=utf-8

anonymized_data = dict()
with open('data/anonymized.data', 'rU') as anonymized_file:
    for line in anonymized_file:
        line = line.strip()
        temp = line.split(";")
        anonymized_data[int(temp[-1])] = temp[:-1]

final_data = []
with open('data/bank.csv', 'rU') as data_file:
    ii = 1
    for line in data_file:
        if line.startswith('"age"'):
            final_data.append(line)
        else:
            temp = line.split(";")
            anonymized_temp = anonymized_data[ii] + temp[7:]
            final_data.append(";".join(anonymized_temp))
            ii += 1

with open('data/final_anonymized.csv','w') as output:
    for line in final_data:
        output.write(line)


