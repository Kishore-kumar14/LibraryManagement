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
# Student Registration Module
def register_student(name):
    print(f"Student {name} has been registered.")
print("Update to check daily change check")
print("check")
# Login Feature
def login(username, password):
    if username == "admin" and password == "secret":
        print("Login successful")
    else:
        print("Login failed")
print("This line is a mistake and should be deleted")