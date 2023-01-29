
def insertion_sort(array): 
    # array[:i+1] shall be a sorted array and array[i+1:] 
    for i in range(1, len(array)):
        # we need to keep -2 because we were having problems searching in sorted array upto 0th element
        # since we are inserting at (j + 1)th position 
        # its just a small fix, nothing to worry about
        for j in range(i, -2 , -1):
            if array[i] > array[j]:
                break
        # insert after the element thats smaller than current element
        array.insert(j + 1, array.pop(i))
    print("Insertion sort result:", array)


def selection_sort(nums):
    for i in range(0, len(nums)): 
        min_i = i 
        # find minimmum element in the unsorted array and move it to the end of the sorted array
        for j in range(i, len(nums)):
            min_i = j if nums[min_i] > nums[j] else min_i
        nums[i], nums[min_i] = nums[min_i], nums[i]

    print("Selection sort result:", nums)


def bubble_sort(nums):
    
    while True:
        swapping = False 
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i - 1]:
                # swap
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapping = True  
            print(nums)

        if not swapping:
            break

    print("Bubble sort result:", nums)

        
def counting_sort(nums):
    print("Input array:", nums);
    # since counting sort assumes a range  
    # for our implementation's purposes lets assume our nums are in range [1, 10] inclusive

    # indices of list 'count' represent num in nums and element at that index represents freq
    count = [0 for i in range(10 + 1)]
    for i in range(len(nums)):
        count[nums[i]] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i]*count[i])

    print("Counting sort result:", result)


def merge_sort(array):
    def merge(left, right):
        l = r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        if len(left)- l > 0:
            result.extend(left[l:])
        elif len(right) - r > 0:
            result.extend(right[r:])

        return result
    
    def solve(nums): 
        if len(nums) == 1:
            return nums 
        
        mid = len(nums) // 2
        left = solve(nums[:mid])
        right = solve(nums[mid:])
        result = merge(left, right)

        return result

    return solve(array)


def bucket_sort(array):
    pass

def radix_sort(array):
    pass


if __name__ == '__main__':
    array = [2, 4, 1, 6, 5, 3, 7, 8]
    # print("input:", array) 
    # insertion_sort(array[:])
    # selection_sort(array[:])
    # bubble_sort(array[:])
    # for counting sort our elements of the array have to be in a range 
    # counting_sort([1, 1, 2, 2, 3, 3, 3, 1, 3, 1, 4, 5, 6, 4, 5, 7])
    print(merge_sort(array[:]))
    # bucket_sort(array[:])
    # radix_sort(array[:])




