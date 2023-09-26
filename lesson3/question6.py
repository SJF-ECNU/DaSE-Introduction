if __name__=="__main__":
    score = int(input("请输入您的成绩："))
    if(score>=90):
        print("优秀")
    elif(score>=75):
        print("良好")
    elif(score>=60):
        print("合格")
    else:
        print("不合格")