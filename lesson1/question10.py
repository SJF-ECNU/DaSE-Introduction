def repeation_test(input_string):
    dic={}
    for ch in input_string:
        if ch in dic:
            return True
        dic[ch]=1
    return False
input_str = input()
flag = repeation_test(input_str)
if(flag):
    print("Yes")
else:
    print("No")
