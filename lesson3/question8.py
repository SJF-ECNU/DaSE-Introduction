import random
import time
import sys
new_limit = 500000  # 设置新的递归深度限制
sys.setrecursionlimit(new_limit)


#随机数列表生成器
def RandomNumsCreater(size,max,min):
    return_nums_list = []
    for i in range(size):
        return_nums_list.append(random.randint(min,max))
    return return_nums_list

#冒泡排序
def BubbleSort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
    return num_list

#选择排序
def SelectionSort(num_list):
    for i in range(len(num_list)):
        min_location=i
        for j in range(i,len(num_list)):
            if num_list[j] < num_list[min_location]:
                min_location = j
        num_list[i],num_list[min_location] = num_list[min_location],num_list[i]
    return num_list

#插入排序
def InsertSort(num_list):
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i],num_list[j] = num_list[j],num_list[i]
    return num_list

#快速排序
def QuickSort(num_list):
    stack = [(0, len(num_list) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = num_list[low]
            left = low + 1
            right = high
            while True:
                while left <= right and num_list[left] <= pivot:
                    left += 1
                while left <= right and num_list[right] >= pivot:
                    right -= 1
                if left <= right:
                    num_list[left], num_list[right] = num_list[right], num_list[left]
                else:
                    break
            num_list[low], num_list[right] = num_list[right], num_list[low]
            stack.append((low, right - 1))
            stack.append((right + 1, high))
    return num_list


#堆排序
def HeapSort(num_list):
    def sift_down(start, end):
        # 最大堆调整，以start为根节点，end为尾节点的堆，从start开始调整使得start大于两个子节点，子节点分别为2*start+1和2*start+2
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and num_list[child] < num_list[child + 1]:
                child += 1
            if num_list[root] < num_list[child]:
                num_list[root], num_list[child] = num_list[child], num_list[root]
                root = child
            else:
                break
    # 创建最大堆
    for start in range((len(num_list) - 2) // 2, -1, -1):
        sift_down(start, len(num_list) - 1)
    # 堆排序
    for end in range(len(num_list) - 1, 0, -1):
        num_list[0], num_list[end] = num_list[end], num_list[0]
        sift_down(0, end - 1)
    return num_list

#归并排序
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))  # 从左边取出一个元素
        else:
            result.append(right.pop(0))  # 从右边取出一个元素
    if left:
        result += left
    if right:
        result += right
    return result

def MergeSort(num_list):
    if len(num_list) <= 12:
        return InsertSort(num_list)
    mid = len(num_list) // 2
    left = MergeSort(num_list[:mid])
    right = MergeSort(num_list[mid:])
    return merge(left, right)

#计数排序
def CountingSort(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    count_list = [0]*(max_num-min_num+1)
    for i in num_list:
        count_list[i-min_num] += 1
    num_list = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            num_list.append(i+min_num)
    return num_list

#基数排序
def RadixSort(num_list):
    max_num = max(num_list)
    max_digit = len(str(max_num))
    for i in range(max_digit):
        bucket_list = [[] for i in range(10)]
        for j in num_list:
            bucket_list[j//(10**i)%10].append(j)
        num_list = []
        for j in bucket_list:
            num_list += j
    return num_list

#桶排序
def BucketSort(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    bucket_size = 10
    bucket_count = (max_num-min_num)//bucket_size+1
    bucket_list = [[] for _ in range(bucket_count)]
    for i in num_list:
        bucket_list[(i-min_num)//bucket_size].append(i)
    num_list = []
    for i in bucket_list:
        num_list += InsertSort(i)
    return num_list

#时间测试函数
def MeasureTime(func,*args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time-start_time

if __name__=="__main__":
    numsize=10000
    times=100
    BubbleSort_time = 0
    SelectionSort_time = 0
    InsertSort_time = 0
    QuickSort_time = 0
    HeapSort_time = 0
    MergeSort_time = 0
    CountingSort_time = 0
    RadixSort_time = 0
    BucketSort_time = 0
    for i in range(times):
        num_list = RandomNumsCreater(numsize,10000,1)#生成1000个1-10000的随机数
        BubbleSort_time += MeasureTime(BubbleSort,num_list)
        SelectionSort_time += MeasureTime(SelectionSort,num_list)
        InsertSort_time += MeasureTime(InsertSort,num_list)
        QuickSort_time += MeasureTime(QuickSort,num_list)
        HeapSort_time += MeasureTime(HeapSort,num_list)
        MergeSort_time += MeasureTime(MergeSort,num_list)
        CountingSort_time += MeasureTime(CountingSort,num_list)
        RadixSort_time += MeasureTime(RadixSort,num_list)
        BucketSort_time += MeasureTime(BucketSort,num_list)
    print("numsize:",numsize)
    print("冒泡排序平均时间：",BubbleSort_time/times)
    print("选择排序平均时间：",SelectionSort_time/times)
    print("插入排序平均时间：",InsertSort_time/times)
    print("快速排序平均时间：",QuickSort_time/times)
    print("堆排序平均时间：",HeapSort_time/times)
    print("归并排序平均时间：",MergeSort_time/times)
    print("计数排序平均时间：",CountingSort_time/times)
    print("基数排序平均时间：",RadixSort_time/times)
    print("桶排序平均时间：",BucketSort_time/times)    
# numsize: 10
# 冒泡排序平均时间： 9.822845458984376e-06
# 选择排序平均时间： 2.018451690673828e-05
# 插入排序平均时间： 9.791851043701172e-06
# 快速排序平均时间： 0.0
# 堆排序平均时间： 1.9888877868652344e-05
# 归并排序平均时间： 0.0
# 计数排序平均时间： 0.0012812256813049317
# 基数排序平均时间： 9.99927520751953e-06
# 桶排序平均时间： 0.00020046472549438475

# numsize: 100
# 冒泡排序平均时间： 0.0008098506927490235
# 选择排序平均时间： 0.00044507980346679686
# 插入排序平均时间： 0.00030150651931762693
# 快速排序平均时间： 0.0005610513687133789
# 堆排序平均时间： 0.0001910114288330078
# 归并排序平均时间： 0.00014041423797607423
# 计数排序平均时间： 0.0019579100608825683
# 基数排序平均时间： 0.0001598358154296875
# 桶排序平均时间： 0.0003602266311645508

# numsize: 1000
# 冒泡排序平均时间： 0.07204222202301025
# 选择排序平均时间： 0.033865470886230466
# 插入排序平均时间： 0.03426355838775635
# 快速排序平均时间： 0.0421356201171875
# 堆排序平均时间： 0.0032747411727905274
# 归并排序平均时间： 0.001755058765411377
# 计数排序平均时间： 0.0019405150413513183
# 基数排序平均时间： 0.0011643457412719726
# 桶排序平均时间： 0.0007990407943725586

#可以发现，冒泡排序、插入排序、选择排序的时间复杂度都是O(n^2)，而快速排序、堆排序、归并排序的时间复杂度都是O(nlogn)，计数排序、基数排序、桶排序的时间复杂度都是O(n)，所以当数据量较大时，快速排序、堆排序、归并排序的效率最高，而当数据量较小时，计数排序、基数排序、桶排序的效率最高。