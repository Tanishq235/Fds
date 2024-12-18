perc = []
t = int(input("Enter the number of students: "))
for i in range(1, t + 1):
    n = float(input(f"Enter the percentage for student {i}: "))
    perc.append(n)

print("Original List:", perc)
def percpar(perc, start, end):
    pivot = perc[start]
    lower_bound = start + 1
    upper_bound = end

    while True:
        while lower_bound <= upper_bound and perc[lower_bound] <= pivot:
            lower_bound += 1
        while lower_bound <= upper_bound and perc[upper_bound] >= pivot:
            upper_bound -= 1

        if lower_bound <= upper_bound:
        
            perc[lower_bound], perc[upper_bound] = perc[upper_bound], perc[lower_bound]
        else:
            break


    perc[start], perc[upper_bound] = perc[upper_bound], perc[start]

    return upper_bound


def quick_sort(perc, start, end):
    if start < end:
        partition = percpar(perc, start, end)
        quick_sort(perc, start, partition - 1)
        quick_sort(perc, partition + 1, end)

quick_sort(perc, 0, len(perc) - 1)
print("Sorted List:", perc)
