import random
# The random package is used in this program to generate a random integer
import time
# The time package is used in this program to time each sorting algorithm
import os
# The os package is used in this program to clear the terminal


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check(data_set):
    # This function is used to check if the data_set is sorted
    for i in range(1, len(data_set)):
        if data_set[i-1] > data_set[i]:  # Checks if the previous element is greater than the current element
            print("Sorting Failed.")  # This should never happen
            return -1


def bubble_sort(data_set):  # Basic Bubble sort algorithm
    start = time.time()  # Starting the 'timer'
    for i in range(len(data_set)):
        for j in range(len(data_set)-i-1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]
    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=data_set) == -1:
        return
    print("Sort Completed!")
    return end


def selection_sort(data_set):  # Selection sort algorithm. Space complexity is O(1)!
    start = time.time()  # Starting the 'timer'
    for i in range(len(data_set)):
        smallest_ind = i
        for j in range(i+1, len(data_set)):
            if data_set[smallest_ind] > data_set[j]:
                smallest_ind = j
        data_set[smallest_ind], data_set[i] = data_set[i], data_set[smallest_ind]
    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=data_set) == -1:
        return
    print("Sort Completed!")
    return end


def insertion_sort(data_set):
    # Divides the list into halves until it is not able to divide anymore (until 1 element is left)
    ...


def quick_sort(data_set):
    ...


def counting_sort(data_set):  # Counting sort algorithm using dictionaries (hashmap)
    start = time.time()  # Starting the 'timer'
    max_num = 0
    for i in range(len(data_set)):
        if max_num < data_set[i]:
            max_num = data_set[i]

    count = [0] * (max_num + 1)
    for i in range(len(data_set)):
        count[data_set[i]] += 1

    output = []
    for i in range(len(count)):
        while count[i] != 0:
            output.append(i)
            count[i] -= 1
    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=data_set) == -1:
        return
    print("Sort Completed!")
    return end


def generate_data_set(size):  # Generates a random list depending on the parameter
    if 500 <= size <= 1000000:
        ds = []
        for _ in range(size):
            ds.append(random.randint(0, 10000000))
        return ds
    print("Must enter a number that is greater than 500 and less than 1,000,000!")


def main():  # Manages basic user inputs
    print("Welcome to Sorting Simulator!\nPress Enter to quit anytime!")
    while True:  # Getting a range of numbers to generate a list of random numbers (0 - 10,000,000)
        ds = generate_data_set(size=int(input("Enter the size of data set (from 500 to 1,000,000): ")))
        # Gets the input of the user and is put into the argument of the function
        if ds != -1:
            break
    while True:  # Getting user's input to display which sorting algorithm to use
        timing = -1
        type_sort = input(
            "1. Bubble Sort - Time Complexity: O(n^2)\n"
            "2. Selection Sort - Time Complexity: O(n^2)\n"
            "3. Insertion Sort - Time Complexity: O(n^2)\n"
            "4. Quick Sort - Time Complexity: O(n*log(n))\n"
            "5. Counting Sort - Time Complexity: O(n+K)\n"
            "Enter the number of the sort you want to time (Enter to quit): "
        )
        if not type_sort:
            return 0

        if int(type_sort) == 1:
            timing = bubble_sort(data_set=ds)
        elif int(type_sort) == 2:
            timing = selection_sort(data_set=ds)
        elif int(type_sort) == 3:
            timing = insertion_sort(data_set=ds)
        elif int(type_sort) == 4:
            timing = quick_sort(data_set=ds)
        elif int(type_sort) == 5:
            timing = counting_sort(data_set=ds)
        else:
            print("That is an invalid choice!")
        if timing != -1:
            print(f"Time Required: {timing * 1000} ms")
            input("Press Enter to continue...")
            clear()


if __name__ == "__main__":
    main()
    print("Thank you!")
