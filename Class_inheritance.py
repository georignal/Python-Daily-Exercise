# 练习题：雪地里来了一群动物小画家，请根据动物的特征，让其绘制独有的图案。

class Animal(object):
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def paint(self):
        print(f'{self.name} {self.skill}')


class Chicken(Animal):
    pass


class Dog(Animal):
    pass


class Fog(Animal):
    def paint(self):
        print(f'{self.name} ，他在洞里睡着啦')

    def voice(self):
        print('来年再来啦')


chicken1 = Chicken('小鸡', '画枫叶')
dog1 = Dog('小狗', '画梅花')
fog1 = Fog('青蛙', None)

chicken1.paint()
dog1.paint()
fog1.paint()
fog1.voice()

