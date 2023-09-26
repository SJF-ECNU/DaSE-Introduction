def integer_binary_converter(integer_part):
    binary_number=[]
    while integer_part>0:
        binary_number.append(integer_part%2)
        integer_part=integer_part//2
    binary_number.reverse()
    return binary_number


def decimal_binary_converter(decimal_part):
    binary_number=[]
    while decimal_part>0:
        decimal_part*=2
        if decimal_part>=1:
            binary_number.append(1)
            decimal_part-=1
        else:
            binary_number.append(0)
    return binary_number

if __name__=="__main__":
    input_num=float(input("Enter a number: "))
    integer_part=int(input_num)
    decimal_part=input_num-integer_part
    integer_binary_number=integer_binary_converter(integer_part)
    decimal_binary_number=decimal_binary_converter(decimal_part)
    result=integer_binary_number
    result.append('.')
    result.extend(decimal_binary_number)
    print(f"{input_num}转化为二进制的结果为{result}")
