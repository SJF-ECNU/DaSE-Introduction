def factorail(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result
x=int(input("请输入一个正整数："))
print(f"计算结果为:{factorail(x)}")