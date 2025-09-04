import random

def MCSS(a):
    """
    Finds the largest sum of a subsequence in the array.
    Finds the starting and ending indices of the subsequence of the largest sum
    """
    end, largest, acc, i = 0, 0, 0, 0
    starts = [0]    # Starts is a list that will store the starting index of each subsequence in the array
    for j in range(len(a)):
        acc += a[j]
        if acc > largest:
            largest = acc
            end = j     # setting the ending index to the element that increases largest
        elif acc < 0:
            i = j + 1
            if i < len(a):  # Sets a condition to append i to the starts list so we do not get a out of bound index
                starts.append(i)
            acc = 0
    """
    At this point we will know the ending index of the subsequence
    So now, we can iterate through all the starting indices of each subsequence and find the index that is closest to the end.
    """
    start = end
    for k in starts:
        if k <= end:
            start = k

    return largest, [start, end]

def main():
    nums = []
    for i in range(1000):
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
