def fibonacci_search(arr, key):
    n = len(arr)
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1  
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i][0] < key:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        elif arr[i][0] > key:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        else:
            return i

    if fib_m1 and offset + 1 < n and arr[offset + 1][0] == key:
        return offset + 1

    return -1

def insert_in_phonebook(phonebook, name, mobile):
    phonebook.append((name, mobile))
    phonebook.sort()

phonebook = []
n = int(input("Enter the number of friends: "))

for _ in range(n):
    name = input("Enter friend's name: ")
    mobile = input("Enter friend's mobile number: ")
    phonebook.append((name, mobile))

phonebook.sort()

print("\nSorted Phonebook:")
for name, mobile in phonebook:
    print(f"{name}: {mobile}")
search_name = input("\nEnter the name of the friend to search: ")
index = fibonacci_search(phonebook, search_name)

if index != -1:
    print(f"Friend found: {phonebook[index][0]} - {phonebook[index][1]}")
else:
    print("Friend not found in the phonebook.")
    add = input("Do you want to add them to the phonebook? (yes/no): ").strip().lower()
    if add == 'yes':
        mobile = input("Enter their mobile number: ")
        insert_in_phonebook(phonebook, search_name, mobile)
        print("\nUpdated Phonebook:")
        for name, mobile in phonebook:
            print(f"{name}: {mobile}")
