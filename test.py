import random

def MCSS(a):
    start, end, largest, acc, i = 0, 0, 0, 0, 0
    for j in range(len(a)):
        acc += a[j]
        if acc > largest:
            largest = acc
            end = j
        elif acc < 0:
            i = j + 1
            start = i
            acc = 0
    return largest, [start, end]
            

def main():
    nums = []
    for i in range(10):
        nums.append(random.randint(-500, 500))
    
    print(nums)
    value, indeces = MCSS(nums)
    print("The value is", value, "at indeces", indeces)

main()
