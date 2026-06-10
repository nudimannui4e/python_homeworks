#!/usr/bin/env python
#-*-coding:UTF-8 -*-n
################################################
# File Name: for_example_2.py
# Author : Ivliev Dmitry
# Email: ivliev@tutu.ru
# Created Time: вторник, 19 мая 2026 г. 15:31:15
#################################################

users = {
        'Dmitry': 'active',
        'Anastasia': 'active',
        'Bob': 'inactive',
        }

for user, status in users.items():
    if status == 'active':
        print(user, status)
