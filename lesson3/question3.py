import re

def judge_length(s):
    if len(s) == 18:
        return True
    else:
        return False

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def judge_Administrative_Division_Code(s):
    region_codes = [
    '110',  # 北京市
    '120',  # 天津市
    '130',  # 河北省
    '140',  # 山西省
    '150',  # 内蒙古自治区
    '210',  # 辽宁省
    '220',  # 吉林省
    '230',  # 黑龙江省
    '310',  # 上海市
    '320',  # 江苏省
    '330',  # 浙江省
    '340',  # 安徽省
    '350',  # 福建省
    '360',  # 江西省
    '370',  # 山东省
    '410',  # 河南省
    '420',  # 湖北省
    '430',  # 湖南省
    '440',  # 广东省
    '450',  # 广西壮族自治区
    '460',  # 海南省
    '500',  # 重庆市
    '510',  # 四川省
    '520',  # 贵州省
    '530',  # 云南省
    '540',  # 西藏自治区
    '610',  # 陕西省
    '620',  # 甘肃省
    '630',  # 青海省
    '640',  # 宁夏回族自治区
    '650',  # 新疆维吾尔自治区
    '710',  # 台湾省
    '810',  # 香港特别行政区
    '820',  # 澳门特别行政区
    ]
    for i in region_codes:
        if i == s[:3]:
            return True
    return False

def judge_Birthday(s):
    if int(s[6:10]) < 1900 or int(s[6:10]) >= 2024:
        return False
    if int(s[10:12]) < 1 or int(s[10:12]) > 12:
        return False
    if int(s[10:12])==2:
        if is_leap_year(int(s[6:10])):
            if int(s[12:14])>29 or int(s[12:14])<1:
                return False
        elif int(s[12:14])>28 or int(s[12:14])<1:
            return False
    if int(s[10:12])==1 or int(s[10:12])==3 or int(s[10:12])==5 or int(s[10:12])==7 or int(s[10:12])==8 or int(s[10:12])==10 or int(s[10:12])==12:
        if int(s[12:14])>32 or int(s[12:14])<1:
            return False
    if int(s[10:12])==4 or int(s[10:12])==6 or int(s[10:12])==9 or int(s[10:12])==11:
        if int(s[12:14])>31 or int(s[12:14])<1:
            return False
    return True
def judge_checksum_digit(s):
    sum = 0
    flag=int(s[17])
    if s[17] == 'x' or s[17] == 'X':
        flag=int(10)
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum_chars = "10X98765432"
    for i in range(0,17):
        sum += int(s[i]) * weights[i]
    checksum_index = sum % 11
    checkflag = int(checksum_chars[checksum_index])
    if checkflag == flag :
        return True
    else:
        return False
if __name__=="__main__":
    IDNumber = input("请输入身份证号码：")
    if judge_length(IDNumber) and judge_Administrative_Division_Code(IDNumber) and judge_Birthday(IDNumber) and judge_checksum_digit(IDNumber):
        print("您输入的身份证号码是符合规则的。")
    else:
        print("您输入的身份证号码是不符合规则的。")
if __name__=="__method2__":

    def validate_id_num(id_num):
        # 正则表达式模式，用于匹配合规的身份证号码
        pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9xX])$'

        # 使用 re 模块进行匹配
        if re.match(pattern, id_num):
            return True
        else:
            return False

    id_num=input("请输入身份证号码：")
    if validate_id_num(id_num):
        print(f"{id_num} 是合规的身份证号码。")
    else:
        print(f"{id_num} 不是合规的身份证号码。")
   