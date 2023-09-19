# 拆分函数，用于将一个数字二分
def divide(input_num):
    if input_num % 2 == 0:
        return int(input_num / 2)
    else:
        return int((input_num + 1) / 2)


# 不断调用拆分函数直到拆分为2和3
def max_list(input_num):
    my_dict = {}
    my_dict[input_num] = my_dict.get(input_num, 0) + 1  # 通过字典记录输入的数值

    while True:  # 通过循环来实现而不是递归，递归的时间开销更大
        max_key = max(my_dict.keys())  # 找到字典中最大的键值
        if max_key <= 3:  # 检测这个键值是否大于3，如果没有大于3的，说明已经分解完成
            break

        new_input = divide(max_key)
        my_dict[new_input] = my_dict.get(new_input, 0) + 1
        my_dict[max_key - new_input] = my_dict.get(max_key - new_input, 0) + 1
        my_dict[max_key] -= 1

        if my_dict[max_key] == 0:
            del my_dict[max_key]
    return my_dict


num_to_divide = int(input("请输入要拆分的数字："))
return_dict = max_list(num_to_divide)

# 输出函数
while True:
    max_key = max(return_dict.keys())
    print(max_key, end='')
    return_dict[max_key] -= 1
    if return_dict[max_key] == 0:
        del return_dict[max_key]
    if not return_dict:
        break
    else:
        print("*", end='')
