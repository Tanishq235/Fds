def selection_sort():
    a = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        a.append(num)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        # Swap the elements
        a[i], a[min_index] = a[min_index], a[i]
    print("The sorted list is:", a)
selection_sort()
def bubble_sort():
    n = int(input("Enter the number of elements in the list: "))
    num = []
    for i in range(n):
        a = int(input(f"Enter number {i + 1}: "))
        num.append(a)
    print("Original list:", num)
    for a in range(0, n - 1):
        for i in range(0, n - 1):
            if num[i] > num[i + 1]:
                temp = num[i]
                num[i] = num[i + 1]
                num[i + 1] = temp

    print("Sorted list:", num)
bubble_sort()
