# Linear Search
def linearSearch(target):
    array = [1, 2, 3, 4, 5]
    for i in range(len(array)):
        if target == array[i]:
            print("Target Found at index:", i)
            return
    print("Target not found")

linearSearch(1)