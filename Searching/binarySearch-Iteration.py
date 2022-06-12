'''
Binary search for a target number in a given sorted list.

Complexity: O(logn)
'''

nums = list(map(int, input('Enter the sorted list elements separated by spaces: ').split(' ')))
target = int(input('Enter the target element: '))
low = 0
high = len(nums) - 1
flag = 0
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print(f'Target number found at list index: {mid}')
        flag = 1
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if flag == 0:
    print('Target not found in the list')