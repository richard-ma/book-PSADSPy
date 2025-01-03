#!/usr/bin/env python3

from math import gcd # import python math library's gcd function


class Fraction:
    # 练习1.8 5题：确保分子分母均为整数
    def __init__(self, top: int, bottom: int) -> None:
    # 练习1.8 2题：在创建分数时约分
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    # 练习1.8 6题：解决分母为负的问题
        if self.den < 0:
            self.num = -self.num
            self.den = abs(self.den)

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self) -> str:
        return str(self.num) + '/' + str(self.den)
    # 练习1.8 9题：__repr__，当__str__方法没有实现，则用于返回字符串，相当于__str__

    def __add__(self, otherfraction):
        new_num = self.num * otherfraction.den + \
                self.den * otherfraction.num
        new_den = self.den * otherfraction.den

        return Fraction(new_num, new_den)
    # 练习1.8 7题：当__add__方法没有实现，对象又在加号右侧，尝试调用__radd__函数
    # 练习1.8 8题：__iadd__对应+=运算符

    # 练习1.8 3题：添加方法
    def __sub__(self, otherfraction):
        new_num = self.num * otherfraction.den - \
                self.den * otherfraction.num
        new_den = self.den * otherfraction.den

        return Fraction(new_num, new_den)

    def __mul__(self, otherfraction):
        new_num = self.num * otherfraction.num
        new_den = self.den * otherfraction.den

        return Fraction(new_num, new_den)

    def resiprocal(self): # 将本分数变为倒数
        return Fraction(self.den, self.num)

    def __truediv__(self, otherfraction):
        return self.__mul__(otherfraction.resiprocal())

    # 获得通分后self和other的分子，分母相同，比较分子即可得到分数大小
    # 这是一个helper函数，作为类内部使用
    def _getFristSecond(self, other):
        firstnum = self.num * other.den
        secondsum = self.den * other.num

        return (firstnum, secondsum)

    def __eq__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum == secondsum

    # 练习1.8 4题：添加__ne__, __gt__, __lt__, __ge__, __le__方法

    def __ne__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum != secondsum

    def __gt__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum > secondsum

    def __ge__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum >= secondsum

    def __lt__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum < secondsum

    def __le__(self, other):
        firstnum, secondsum = self._getFristSecond(other)
        return firstnum <= secondsum

    # 练习1.8 1题：添加getNum和getDen方法
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den