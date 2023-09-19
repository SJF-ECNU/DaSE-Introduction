import random


# 蒙特卡洛方法
def distance(x, y):
    return pow(x ** 2 + y ** 2, 1 / 2)


def method_1(method_1_times=1000000):
    count_in = 0.0
    count_out = 0.0
    for i in range(0, method_1_times):
        random_dot_x = random.uniform(-1, 1)
        random_dot_y = random.uniform(-1, 1)
        if distance(random_dot_x, random_dot_y) <= 1:
            count_in += 1
        else:
            count_out += 1
    return count_in / method_1_times * 4


# 莱布尼茨级数
def method_2(times_method_2=1000):
    num_method_2 = 0
    for i in range(1, times_method_2 + 1):
        num_method_2 += 1 / (2 * i - 1) * (-1) ** (i + 1)
    return 4 * num_method_2


# 欧拉级数
def method_3(method_2_times=1000):
    num = 0
    for i in range(1, method_2_times + 1):
        num += 1 / i**2
    return pow(6 * num,1/2)


if __name__ == "__main__":
    print(f"the answer through method_1 is {method_1()}")
    print(f"the answer through method_2 is {method_2()}")
    print(f"the answer through method_3 is {method_3()}")
