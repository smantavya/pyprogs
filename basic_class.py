# class Hello:
#     s = "hello"
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print("hello this is construtor ")
#
#     def hi(self):
#         print(self.x + self.y)
# x = 10
# y = 45
# t = Hello(x,y)
#
# t.hi()

#
# class Animal:
#     t = "hello"
#
# class Brid(Animal):
#     y = "fly"
#
#
# b = Brid()
# print(b.y)
# print(b.t)


class Bike:
    __maxspeed = 120


    def gtr(self):
        print(self.__maxspeed)

    def str(self,x ):
        self.__maxspeed = x

t = Bike()
# print(t.__maxspeed)

t.gtr()
t.str(150)
t.gtr()
