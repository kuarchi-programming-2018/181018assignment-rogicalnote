# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:48:07 2018

@author: Takuto
"""

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self,target):
        print(self.msg +" " + target)
        


player = Hello()
player.say_hello("python")