import random

def MCSS(a):
    end, largest, acc, i = 0, 0, 0, 0
    starts = [0]
    for j in range(len(a)):
        acc += a[j]
        if acc > largest:
            largest = acc
            end = j
        elif acc < 0:
            i = j + 1
            if i < len(a):
                starts.append(i)
            acc = 0

    start = end
    for k in starts:
        if k <= end:
            start = k

    return largest, [start, end]

def main():
    nums = []
    for i in range(10):
        nums.append(random.randint(-500, 500))
    #nums = [-247, 466, -353, -445, -452, 188, -37, 421, -52, -63]
    #nums = [-2, 4, -4, -4,-5, 2, 0, 4, -1, -1]
    #nums = [-2, 11, -4, 13, -20, 16, -5]
    #nums = [-440, -417, 292, 294, 368, 196, -495, -464, -421, -341]
    #nums = [-4, -3, 3, 3, 4, 2, -5, -5, -4, -3]



    print("The array is :", nums)
    value, indices = MCSS(nums)
    print("The value is", value, "at indices", indices)

main()
