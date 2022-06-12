'''
Linear search for a target number in a given list.

Complexity: O(n)
'''

nums = list(map(int, input('Enter the list elements separated by spaces: ').split(' ')))
target = int(input('Enter the target element: '))
flag = 0
for i in range(len(nums)):
    if nums[i] == target:
        print(f'Target number found at list index: {i} ')
        flag = 1
        break
if flag == 0:
    print('Target not found in the list')