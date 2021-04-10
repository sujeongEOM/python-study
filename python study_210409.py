class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class FourCal:
    pass

a=FourCal()
print(type(a))

class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result

a=FourCal(2, 4)
print(a.add())


class MoreFourCal(FourCal):
    pass

a=MoreFourCal(4, 5)
print(a.mul())

class ChildFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else: 
            return self.first /self.second

a=ChildFourCal(2, 6)
print(a.div())

import sys
sys.path.append("C:\\eomcoding\\subFolder")
import mod1
print(mod1.add(3, 4))

import game.sound.echo
game.sound.echo.echo_test()

from game.sound.echo import echo_test as e
e()

from game.sound import *
echo.echo_test()

from game import *
sound.echo.echo_test()


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradCalculator(Calculator):
    def minus(self, val):
        self.value = self.value - val

cal = UpgradCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value+= val
        if self.value > 100:
            self.value=100

su = MaxLimitCalculator()
su.add(50)
su.add(60)
su.add(-20)
su.add(50)

print(su.value)

print(all([1, 2, abs(-3)-3]))

print(abs(-3)-3)

print(chr(ord('a'))=='a')

print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))

print(int('0xea', 16))

print(list(map(lambda x: x*3, [1, 2, 3, 4])))

print(int(max([-8, 2, 7, 5, -3, 5, 0, 1])+(min([-8, 2, 7, 5, -3, 5, 0, 1]))))

print(round(5.666666666666667, 4))