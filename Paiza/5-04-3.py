# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:02:01 2018

@author: Takuto
"""

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for i in points:
    sum += points[i]
print(int(sum))