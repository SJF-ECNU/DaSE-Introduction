#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 检查数组是否已排序
int isSorted(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i]) {
            return 0; // 数组未排序
        }
    }
    return 1; // 数组已排序
}

// 猴子排序算法
void monkeySort(int arr[], int n) {
    int attempts = 0;
    
    clock_t start_time = clock();
    
    while (!isSorted(arr, n)) {
        // 随机打乱数组
        for (int i = 0; i < n; i++) {
            int j = rand() % n;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        
        attempts++;
    }
    
    clock_t end_time = clock();
    double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    
    printf("times:%d\n", attempts);
    printf("time_cost:%f second\n", execution_time);
}

int main() {
    srand(time(NULL)); // 使用时间作为随机数种子
    int n;
    
    printf("size: ");
    scanf("%d", &n);
    
    int arr[n];
    
    printf("please input %d nums: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    monkeySort(arr, n);
    
    printf("success: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
