import fileReader
import time


t1 = time.time()


def partition(last, r, nums):

    pivot, ptr = nums[r], last
    for i in range(last, r):
        if nums[i] <= pivot:

            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1

    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(last, r, nums):
    if len(nums) == 1:
        return nums
    if last < r:
        pi = partition(last, r, nums)
        quicksort(last, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums


example = fileReader.file_read("cem.txt")
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
# As you can see, it works for duplicates too
print(quicksort(0, len(example)-1, example))
tf = time.time() - t1
print(tf)
