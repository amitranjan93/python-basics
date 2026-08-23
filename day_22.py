# Recursion
# sum of digits
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n//10)

def power(base,exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half = power(base,exponent//2)
        return half * half
    else:
        return base * power(base,exponent - 1)

def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

def count_occurrences(arr, index, target):
    if index == len(arr):
        return 0
    return (1 if arr[index] == target else 0) + count_occurrences(arr,index+1,target)

def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[:1]

def is_sorted(arr, index):
    if index == len(arr) - 1:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted(arr, index + 1)

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,left,mid-1)
    else:
        return binary_search(arr,target,mid+1,right)

def first_occurence(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        result = first_occurence(arr, target, left, mid - 1)
        if result != -1:
            return result
        return mid
    elif arr[mid] > target:
        return first_occurence(arr,target,left,mid-1)
    else:
        return first_occurence(arr,target,mid+1,right)

def last_occurrence(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        result = last_occurrence(arr, target, mid+1, right)
        if result != -1:
            return result
        return mid
    elif arr[mid] > target:
        return last_occurrence(arr,target,left,mid-1)
    else:
        return last_occurrence(arr,target,mid+1,right)
        
arr = [2, 3, 5, 5, 5, 8, 12, 16, 23, 38, 45, 50]
print(last_occurrence(arr,5,0,len(arr)-1))