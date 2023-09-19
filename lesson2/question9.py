import math
import random

def Fx(num_input):
    return num_input**2+4*num_input*math.sin(num_input)


def Monte_Carlo(times=1000):
    count_in=0
    count_out=0

    for i in range(0,times):
        random_x=random.uniform(2,3)
        random_y=random.uniform(0,13)
        if random_y<= Fx(random_x):
            count_in+=1
        else:
            count_out+=1

    return 13*count_in/times


if __name__=="__main__":
    print(f"求解定积分为：{Monte_Carlo()}")