def rotate(arr):
    temp = 0

    for i in range(len(arr)):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1]
        arr[len(arr) - 1] = temp


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5]
    rotate(num)
    print(num)
