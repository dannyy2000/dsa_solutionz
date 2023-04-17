if __name__ == '__main__':

    x = [1, 3, 4, 5]
    y = [2, 6, 7, 8]

    x.extend(y)
    for j in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

    print(x)








