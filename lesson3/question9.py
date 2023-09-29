def ArrayMultiplication(input_list):
    return_list=[input_list[0]]
    if len(input_list)==1:
        return return_list
    for i in range(1,len(input_list)):
        return_list.append(input_list[i]*return_list[i-1])
    return return_list
if __name__=="__main__":
    input_list=[1,2,3,4,5]
    print(ArrayMultiplication(input_list))