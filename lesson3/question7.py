def gcd(x,y):
    if y==0:
        return x
    else :
        return gcd(y,x%y)

if __name__=="__main__":
    x=int(input("请输入第一个数："))
    y=int(input("请输入第二个数："))
    print(f"{x}和{y}的最大公约数是{gcd(x,y)}")