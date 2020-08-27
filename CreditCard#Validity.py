#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:04:52 2020


def verify(number) : # do not change this line!

  if number[0] != "4":
    print("return 1")
  elif int(number[3]) < int(number[5])+1:
    print("passes Rule #1, return 2")
  elif (int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[5])+int(number[6])+int(number[7])+int(number[8])+int(number[10])+int(number[11])+int(number[12])+int(number[13]))%4 != 0:
    print("passes Rules #1-2, return 3")
  elif (int(number[0]+number[1]) + int(number[7]+number[8])) != 100:
    print("passes Rules #1-3, return 4")
  else:
    return("return True")

numberinput = input("Please type in 12 digits credit card number in XXXX-XXXX-XXXX format:")
verify(numberinput) 

