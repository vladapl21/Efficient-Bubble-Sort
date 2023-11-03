tosort = [36, 21, 13, 1, 3, 87, 20, 6, 4, 17, 15]


def bubblesort(arr):
    temp = 0  # Temporary storage of number
    j = 0
    swap = True
    while swap == True:
        swap = False
        j += 1
        for i in range(len(arr) - j):
            if arr[i] > arr[i + 1]:
                swap = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

    return arr


print(bubblesort(tosort))
