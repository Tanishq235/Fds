def binary_search(phonebook, name):
    """Binary search to find a friend by name in the sorted phonebook."""
    low, high = 0, len(phonebook) - 1
    while low <= high:
        mid = (low + high) // 2
        if phonebook[mid][0] == name:
            return mid
        elif phonebook[mid][0] < name:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    phonebook = []
    while True:
        choice = input("\n1. Add Friend\n2. Search Friend\n3. Display Phonebook\n4. Exit\nEnter choice: ")
        if choice == "1":
            name, number = input("Enter name: "), input("Enter mobile number: ")
            if binary_search(phonebook, name) == -1:
                phonebook.append((name, number))
                phonebook.sort()
                print(f"{name} added.")
            else:
                print(f"{name} is already in the phonebook.")
        elif choice == "2":
            name = input("Enter name to search: ")
            idx = binary_search(phonebook, name)
            if idx != -1:
                print(f"Found: {phonebook[idx][0]}, Mobile: {phonebook[idx][1]}")
            else:
                print("Friend not found.")
        elif choice == "3":
            print("\nPhonebook:")
            for name, number in phonebook:
                print(f"Name: {name}, Mobile: {number}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
