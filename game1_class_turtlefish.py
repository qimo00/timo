import random

class Turtle():
    def __init__(self):
        self.life = 100
        #体力为100
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)
        #初始化位置，xy在[0,10]之间
    def move(self):
        # 随机x，y方向移动1或2
        new_x = self.x + random.choice([1, 2, -1, -2])
        new_y = self.y + random.choice([1, 2, -1, -2])

        # 判断是否超出边线
        if new_x > 10:
            self.x = 10 - (new_x - 10)
        elif new_x < -10:
            self.x = -10 + (-10 - new_x)
        else:
            self.x = new_x
        if new_y > 10:
            self.y = 10 - (new_y - 10)
        elif new_y < -10:
            self.y = -10 + (-10 - new_y)
        else:
            self.y = new_y

        self.life -= 1

    def eat(self):
        self.life += 20
        if self.life > 100:
            self.life = 100
    def point(self):
        #现在位置
        return [self.x, self.y]


class Fish():
    def __init__(self):
        #初始化位置
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)

    def move(self):
        #随机移动1
        new_x = self.x + random.choice([1, -1])
        new_y = self.y + random.choice([1, -1])
        # 判断是否超出边线
        if new_x > 10:
            self.x = 10 - (new_x- 10)
        elif new_x < -10:
            self.x = -10 + (-10 - new_x)
        else:
            self.x =new_x
        if new_y > 10:
            self.y = 10 - (new_y - 10)
        elif new_y < -10:
            self.y = -10 + (-10 - new_y)
        else:
            self.y = new_y
    def point(self):
        # 现在位置
        return [self.x, self.y]
#初始化乌龟和鱼
turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)
#当体力=0 或鱼被吃完时，结束循环
while turtle.life or fish == []:
    #每次循环移动一次，判断位置
    turtle.move()
    turtle_point = turtle.point()
    fish_point = []
    #移动fish列表中的各项，并将位置存在fish_point中，和fish中顺序相同
    for each_fish in fish:
        each_fish.move()
        each_fish_p = each_fish.point()
        fish_point.append(each_fish_p)
    #位置相同，乌龟吃鱼，在鱼列表中删除被吃项
    if turtle_point in fish_point:
        delnum = fish_point.index(turtle_point) #定位与乌龟位置相同的鱼下标
        turtle.eat()
        del fish[delnum]
    for each in fish:
        print(each.point(), end='')
    print(len(fish))
    print('鱼在%s 体力为%s' % (turtle.point(), turtle.life))

print('鱼在%s 体力为%s' % (turtle.point(), turtle.life))
print('game over')



