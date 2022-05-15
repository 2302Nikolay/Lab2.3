#!/usr/bin/env python3
# -*- coding: utf-8 -*-

word = input("Введите слово: ")
char = input("Введите букву: ")
num = int(input("Введите номер: "))

s = (word[0:num]+char+word[num:])
print(s)
