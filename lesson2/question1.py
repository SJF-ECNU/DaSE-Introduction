def max_list(input_num):
    num_undivide = input_num
    count_2 = 0
    count_3 = 0
    while True:
        if num_undivide == 4:
            count_2 += 2
            break
        if num_undivide == 2:
            count_2 += 1
            break
        if num_undivide == 3:
            count_3 += 1
            break
        count_3 += 1
        num_undivide -= 3
    return {2: count_2, 3: count_3}


if __name__ == "__main__":
    num_to_divide = int(input("请输入要拆分的数字："))
    my_dict=max_list(num_to_divide)
    for i in range(0,my_dict[3]):
        print(3,end=" ")
        if(i!=my_dict[3]-1):
            print("*",end="")
    if my_dict[2]!=0:
        print("*",end="")
    for i in range(0,my_dict[2]):
        print(2,end="")
        if(i!=my_dict[2]-1):
            print("*",end="")
        
        
