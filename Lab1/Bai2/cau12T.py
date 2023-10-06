from cmath import sqrt
import math
import sys
from operator import truediv
arr = [4, 2,59, 55, 45, 7, 1, 9, 3, 8, 63, 3, 3, 5,9,10, 35, 68, 29, 79, 5, 15]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isPerfectSquare(num):
    n = int(math.sqrt(num))
    return (n * n == num)
def checkFib(array, n):
    count = 0
    print("Dãy fibonacci là:")
    for i in range(n):
        if (isPerfectSquare(5 * array[i] * array[i] + 4) or
                isPerfectSquare(5 * array[i] * array[i] - 4)):
            print(array[i], " ", end="")
            count = count + 1
    if (count == 0):
        print("None present")

def product_odd_not_divisible_by_3(arr):
    product = 1
    for num in arr:
        if num % 2 != 0 and num % 3 != 0:
            product *= num
    return product

def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
def reverse_elements(arr):
    return arr[::-1]

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def count_occurrences(arr, target):
    return arr.count(target)

def numbers_appearing_n_times(arr, n):
    return [num for num in set(arr) if arr.count(num) == n]



# a) Xuất tất cả các số lẻ không chia hết cho 5
odd_not_divisible_by_5 = [num for num in arr if num % 2 != 0 and num % 5 != 0]
print("a) Các số lẻ không chia hết cho 5:", odd_not_divisible_by_5)

# b) Xuất tất cả các số Fibonacci
n = len(arr)
checkFib(arr, n)

# f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
product_of_odd_not_divisible_by_3 = product_odd_not_divisible_by_3(arr)
print("\nf) Tích các số lẻ không chia hết cho 3:", product_of_odd_not_divisible_by_3)

# g) Đổi chỗ 2 phần tử của danh sách
swap_elements(arr, 0, -1)
print("g) Danh sách sau khi đổi chỗ:", arr)

# h) Đảo ngược trật tự các phần tử của danh sách
reversed_arr = reverse_elements(arr)
print("h) Danh sách sau khi đảo ngược:", reversed_arr)

# j) Tính tổng các chữ số của tất cả các số trong danh sách
digit_sum_total = sum(digit_sum(num) for num in arr)
print("j) Tổng các chữ số:", digit_sum_total)

# k) Đếm số lần xuất hiện của một số trong danh sách
target = int(input("Nhập sô dể xem số lần xuất hiện của nó: "))
occurrences = count_occurrences(arr, target)
print(f"k) Số lần xuất hiện của {target}:", occurrences)

# l) Xuất các số xuất hiện n lần trong danh sách
n = int(input("Nhập sô xem số xuất hiện của nó: "))
numbers_with_n_occurrences = numbers_appearing_n_times(arr, n)
print(f"l) Số xuất hiện {n} lần:", numbers_with_n_occurrences)


