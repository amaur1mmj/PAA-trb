import fileReader
import time


t1 = time.time()


def bubbleSort(alist):
    troca = 0
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                troca += 1
    return troca


alist = fileReader.file_read("cem.txt")

a1 = bubbleSort(alist)

tf = time.time() - t1
print(alist)
print("\n")
print(a1)
print(tf)
