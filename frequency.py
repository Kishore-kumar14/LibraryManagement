#finding frequency of string
def char_freq(s):
    dict1={}
    for i in s:
        if i not in dict1:
            dict[i]=1
        else:
            dict[i]+=1
    return(dict.items())
str1="kishorekumar23MIS0171"
dict1=char_freq(str1)
print(dict1)

#binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
sorted_list = [1, 5, 10, 15, 20, 25]
print(f"Index of 10 is: {binary_search(sorted_list, 10)}")
print("completed")