import time
import threading

# 定义一个函数用于输出数字
def output_number(number):
    time.sleep(number/10)  # 休眠时间与数字大小成正比
    print(number)

# 待排序的数字列表
numbers = [3,2,1,5,10,9,7,8,6,4]

# 创建线程列表
threads = []

# 记录排序开始时间
start_time = time.time()

# 创建并启动每个线程
for number in numbers:
    thread = threading.Thread(target=output_number, args=(number,))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 记录排序结束时间
end_time = time.time()

# 输出排序结果和排序时间
sorted_numbers = sorted(numbers)
print("排序结果:", sorted_numbers)
print("排序时间:", end_time - start_time, "秒")