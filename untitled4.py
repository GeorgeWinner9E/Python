# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AJys7ZDWxsrPNZ6YUKkJIAhXOCnATay9
"""

class fraction(object):
  def __init__(self, num, denom):
    self.num = num
    self.denom = denom
  
  def SUM(self,fract):
    res = fraction
    res.num = self.num*fract.denom+fract.num*self.denom
    res.denom = self.denom*fract.denom
    return res
  
  def DIF(self,fract):
    res = fraction
    res.num = self.num*fract.denom-fract.num*self.denom
    res.denom = self.denom*fract.denom
    return res
  
  def MULT(self,fract):
    res = fraction
    res.num = self.num*fract.num
    res.denom = self.denom*fract.denom
    return res
  
  def DIV(self,fract):
    res = fraction
    res.num = self.num*fract.denom
    res.denom = self.denom*fract.num
    return res
  
  def print(self):
    a=self.num
    b=self.denom
    if b == 0:
      print('недопустимая операция')
    else:
      while a != 0 and b != 0:
        if a > b:
          a = a % b
        else:
          b = b % a
      self.num = self.num/(a+b)
      self.denom = self.denom/(a+b)
      if (self.num % self.denom) == 0:
        print(int(self.num//self.denom))
      else:
        if (self.num//self.denom) == 0:
          print(str(int(self.num % self.denom))+'/'+str(int(self.denom)))
        else:
          print(str(int(self.num//self.denom))+' '+str(int(self.num % self.denom))+'/'+str(int(self.denom)))

def sort()

a=fraction(5,0)
den=fraction(1,4)

SUMM = a.SUM(den)
fraction.print(SUMM)

DIFF = a.DIF(den)
fraction.print(DIFF)

MULTI = a.MULT(den)
fraction.print(MULTI)

DIVI = a.DIV(den)
fraction.print(DIVI)