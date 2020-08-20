# 元胞自动机对排队模型进行仿真
class PeopleList():
    def __init__(self, comenum):
        '''
        :param a:人流密度 一个时间段更新增加的人数
        '''
        self.a = comenum
        self.queue = []
    # 队伍是否为空
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    # 上车一次
    def go(self):
        self.queue.pop()
    # 更新顾客
    def add(self):
        for i in range(self.a):
            self.queue.append(1)
    def show(self):
        print(self.queue)
    def get_queue_len(self):
        return len(self.queue)


'''
list1=PeopleList(4)
list1.show()
list1.add()
list1.show()
list1.go()
list1.show()
print(list1.is_empty())
'''


class TaxiQueue():
    def __init__(self, n, comenum, d, length=10000):
        '''
        :param n: 初始出租车队列长度
        :param d: 一个时间段接客的出租车数
        :param comenum:单位时间来车数量
        :param length:蓄车池最大运载量
        '''
        self.comenum = comenum
        self.d = d
        self.length = length
        self.queue = []
        if n < length:
            for i in range(n):
                self.queue.append(0)
        else:
            for i in range(length):
                self.queue.append(0)
    # 出租车队列增长
    def add(self):
        for i in range(self.comenum):
            if self.is_full():
                pass
            else:
                self.queue.append(0)
    # 出租车队列删减(接客走人)
    def go(self):
        self.queue.pop(0)
    # 得到出租车队列长度
    def get_queue_len(self):
        return len(self.queue)
    # 判断出租车队列是否为空
    def is_empty(self):
        if self.get_queue_len() == 0:
            return True
        else:
            return False
    # 判断蓄车池是否满载
    def is_full(self):
        if len(self.queue) == self.length:
            return True
        else:
            return False


if __name__ == '__main__':
    person_queue = PeopleList(4)
    taxi_queue = TaxiQueue(0, 10, 5, 30)
    for t in range(10):
        print('{}时刻乘客队列数量:{}'.format(t, person_queue.get_queue_len()), end=' ')
        print('{}时刻出租车队列数量:{}'.format(t, taxi_queue.get_queue_len()))
        for i in range(taxi_queue.d):  # 单位时间走车 走人
            if person_queue.is_empty() or taxi_queue.is_empty():
                pass
            else:
                taxi_queue.go()
                person_queue.go()
        # 来车来人
        taxi_queue.add()
        person_queue.add()
