import random
# The random package is used in this program to generate a random integer and shuffle a list like shuffling a
# deck of cards
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
    print("Sort Completed!")


def bogo_sort(data_set):
    print("This might take a while!")
    start = time.time()

    def _sorted():
        for i in range(1, len(data_set)):
            if data_set[i-1] > data_set[i]:
                return False
        return True

    while not _sorted():  # If _sorted returns False, it means that the list is not sorted, and shuffles the list again.
        random.shuffle(data_set)

    end = time.time()-start
    if check(data_set=data_set) == -1:
        return -1
    return end


def bubble_sort(data_set):  # Basic Bubble sort algorithm
    start = time.time()  # Starting the 'timer'
    for i in range(len(data_set)):
        for j in range(len(data_set)-i-1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]
    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=data_set) == -1:
        return -1
    return end


def merge_sort(data_set):
    start = time.time()
    end = time.time() - start

    def _merge_sort(ds):
        if len(ds) > 2:  # if list ds is already 2 (which is in a pair)
            return ds  # Then return ds so it could be merged and sorted
        # First half of the list being fed into the same function to be split it up and sorted
        mid = len(ds) // 2
        left = _merge_sort(ds[:mid])
        # Second half of the list being fed into the same function to be split it up and sorted
        right = _merge_sort(ds[mid:])

        if not len(left) or not len(right):
            if len(left):
                return right
            return left

        # Merging the left list and right list and making a sorted list
        x, y = 0, 0  # x will be for left, and y will be for right
        output = []  # This will be the final output
        while len(left) + len(right) > len(output):
            if left[x] < right[y]:
                output.append(left[x])
                x += 1
            else:
                output.append(right[y])
                y += 1
            if len(left) == x or len(right) == y:  # Sees if either list is done merging
                # Puts the rest of the list (that is not done merging) into output
                if len(left) - x:
                    output.extend(right[y:])
                else:  # elif len(right) - y
                    output.extend(left[x:])
                break

        return output

    data_set = _merge_sort(data_set)  # This requires recursion

    if check(data_set=data_set) == -1:
        return -1
    return end


def counting_sort(data_set):  # Counting sort algorithm
    # Very fast but uses quit a lot of space.
    start = time.time()  # Starting the 'timer'

    biggest = max(data_set)  # Finds the biggest number in the data_set list
    count = [0] * (biggest + 1)  # Creates a list of 0's; the size will depend on the biggest number (plus 1)
    for i in range(len(data_set)):
        count[data_set[i]] += 1

    output = []  # This is the list of output
    for i in range(len(count)):
        while count[i] != 0:  # Appends the index for count[i] number of times
            output.append(i)
            count[i] -= 1

    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=output) == -1:
        return -1
    return end


def generate_data_set(size):  # Generates a random list depending on the parameter
    if 500 <= size <= 1000000:
        ds = []
        for _ in range(size):
            ds.append(random.randint(0, 10000))
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
            "1. Bogo Sort - Time Complexity: O((n+1)!)\n"  # Incredibly inefficient, pinnacle of brute force
            "2. Bubble Sort - Time Complexity: O(n^2)\n"  # Most basic and straight forward sorting algorithm
            "3. Merge Sort - Time Complexity: O(n*log(n))\n"  # Very fast and light
            "4. Counting Sort - Time Complexity: O(n+K)\n"  # Very fast, but requires a lot of computational space
            "Enter the number of the sort you want to time (Enter to quit): "
        )
        if not type_sort:
            return 0

        if int(type_sort) == 1:
            # TODO: MAKE IT SO THAT THERE IS A NUMBER LIMIT FOR BOGOSORT
            timing = bogo_sort(data_set=ds)
        elif int(type_sort) == 2:
            timing = bubble_sort(data_set=ds)
        elif int(type_sort) == 3:
            # TODO: FIX MERGE SORT
            timing = merge_sort(data_set=ds)
        elif int(type_sort) == 4:
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
