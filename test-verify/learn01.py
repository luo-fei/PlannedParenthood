#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(input("please input a number:"))
tail_num = num
count = 0
while True:
    print(num % 10)
    num = num//10
    count += 1
    if num == 0:
        print('you input {} numbers'.format(count))
        break
print('---------', tail_num, count, '----------')
for i in range(count, 0, -1):
    digit = 10**(i-1)
    head_num = tail_num//digit
    tail_num -= head_num*digit
    print(head_num, tail_num)
