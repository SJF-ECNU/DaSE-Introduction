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
        num_list = RandomNumsCreater(1000,10000,1)#生成1000个1-10000的随机数
        BubbleSort_time += MeasureTime(BubbleSort,num_list)
        SelectionSort_time += MeasureTime(SelectionSort,num_list)
        InsertSort_time += MeasureTime(InsertSort,num_list)
        QuickSort_time += MeasureTime(QuickSort,num_list)
        HeapSort_time += MeasureTime(HeapSort,num_list)
        MergeSort_time += MeasureTime(MergeSort,num_list)
        CountingSort_time += MeasureTime(CountingSort,num_list)
        RadixSort_time += MeasureTime(RadixSort,num_list)
        BucketSort_time += MeasureTime(BucketSort,num_list)
    print("冒泡排序平均时间：",BubbleSort_time/times)
    print("选择排序平均时间：",SelectionSort_time/times)
    print("插入排序平均时间：",InsertSort_time/times)
    print("快速排序平均时间：",QuickSort_time/times)
    print("堆排序平均时间：",HeapSort_time/times)
    print("归并排序平均时间：",MergeSort_time/times)
    print("计数排序平均时间：",CountingSort_time/times)
    print("基数排序平均时间：",RadixSort_time/times)
    print("桶排序平均时间：",BucketSort_time/times)    