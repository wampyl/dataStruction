# -*- coding: UTF-8 -*-
 
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 2
        self.publicCount += 3
        print(self.__secretCount)
        # print(self.publicCount)
 
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter._JustCounter__secretCount)  # 报错，实例不能访问私有变量
