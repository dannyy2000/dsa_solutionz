def arrange(arr):
    start = 0
    end = len(arr) - 1
    temp1 = []
    temp2 = []
    # temp = []

    for i in range(len(arr)):
        if arr[i] < 0:
            start = arr[i]
            temp1.append(start)

        if arr[i] > 0:
            end = arr[i]
            temp2.append(end)
    print(temp1 + temp2)


if __name__ == '__main__':
    nums = [10, -1, 20, 4, 5, -9, -6]
    arrange(nums)




