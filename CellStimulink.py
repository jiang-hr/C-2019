import random
from matplotlib import pyplot as plt
# 轮盘赌,猜测回归到那个指针数值 指针内容为概率


def Roulette_wheel(pro_list):
    for i in range(1, len(pro_list)):
        pro_list[i] += pro_list[i-1]
    # print(pro_list)
    randnum = random.randint(1, 10000)/10000
    # print(randnum)
    for i in range(len(pro_list)):
        if randnum <= pro_list[i]:
            # print(i)
            return i
        else:
            pass


class TaxiCell():
    def __init__(self, lamda, mu, length=10000):
        '''
        :param lamda:到达速率
        :param mu:平均服务时间的倒数
        :param length:蓄车池容量上限
        '''
        self.state = 0
        self.lamda = lamda
        self.mu = mu
        self.length = length
    # 用于显示元宝状态(车数量)

    def get_state(self):
        return self.state

    # 用于对元宝状态进行更新
    def renew_state(self):
        if self.state == 0:
            pro_list = [self.lamda, 1-self.lamda]
            if Roulette_wheel(pro_list) == 0:
                self.state += 1
            else:
                pass

        elif self.state == self.length:
            pro_list = [1-self.mu, self.mu]
            if Roulette_wheel(pro_list) == 0:
                pass
            else:
                self.state -= 1

        else:
            pro_list = [self.lamda, 1-self.lamda-self.mu, self.mu]
            guess_result = Roulette_wheel(pro_list)
            if guess_result == 0:
                self.state += 1
            elif guess_result == 1:
                pass
            else:
                self.state -= 1


# Roulette_wheel([0.1,0.3,0.5,0.1])
taxiqueue = TaxiCell(0.3, 0.2, 50)
t_list = list(range(500))
state_list = []
for t in t_list:
    state_list.append(taxiqueue.get_state())
    print('当前出租车序列长度为:{}'.format(taxiqueue.get_state()))
    taxiqueue.renew_state()

plt.figure(1)
plt.plot(t_list, state_list)
plt.show()
