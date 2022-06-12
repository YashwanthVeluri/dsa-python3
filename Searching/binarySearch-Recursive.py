'''
Binary search for a target number in a given sorted list.

Complexity: O(logn)
'''
def binarySearch(nums, low, high, target):
    if low > high:
        return 0
    mid = (low + high)//2
    if nums[mid] == target:
        print(f'Target number found at list index: {mid}')
        return 1
    elif nums[mid] < target:
        return binarySearch(nums, mid+1, high, target)
    else:
        return binarySearch(nums, low, mid-1, target)

if __name__ == '__main__':
    nums = list(map(int, input('Enter the sorted list elements separated by spaces: ').split(' ')))
    target = int(input('Enter the target element: '))

    if binarySearch(nums, 0, len(nums)-1, target) == 0:
        print('Target not found in the list')
