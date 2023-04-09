import random
# The random package is used in this program to generate a random integer and shuffle a list like shuffling a
# deck of cards
import time
# The time package is used in this program to time each sorting algorithm
import os
# The os package is used in this program to clear the terminal


def clear():
    """
	Used: https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    This function is used to clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def check(data_set):
    """
    Used to check if the data set is sorted or not.
    Returns -1 if isn't sorted
    """
    # This function is used to check if the data_set is sorted
    for i in range(1, len(data_set)):
        if data_set[i-1] > data_set[i]:  # Checks if the previous element is greater than the current element
            print("Sorting Failed.")
            return -1
    # prints if the procedure iterates through the list without having one element that is greater than the next element
    print("Sort Completed!")


def bogo_sort(data_set):
    """
	Wikipedia page: https://en.wikipedia.org/wiki/Bogosort
    This function shuffles the parameter data_set until it is sorted.
    returns end - time spent sorting

    Implements another function inside this function
        - Checks if the data_set is sorted by iterating through the data_set and checking
        if the previous element is smaller than the current element
    """
    print("This might take a while!")

    def _sorted():
        for i in range(1, len(data_set)):
            if data_set[i-1] > data_set[i]:
                return False
        return True  # After checking through the whole list, it will then return True because the list would be sorted

    start = time.time()

    while not _sorted():  # If _sorted returns False, it means that the list is not sorted, and shuffles the list again.
        random.shuffle(data_set)  # Randomly shuffles the data_set

    end = time.time() - start
    if check(data_set=data_set) == -1:
        return -1
    return end * 1000


def bubble_sort(data_set):  # Basic Bubble sort algorithm
    """
	Wikipedia: https://en.wikipedia.org/wiki/Bubble_sort

    Goes through the parameter data_set n^2 times
    Swaps the previous data_set element with the current one if the previous one is greater than the current one.
    returns end - time spent sorting
    """
    start = time.time()  # Starting the 'timer'
    for i in range(len(data_set)):
        for j in range(len(data_set)-i-1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]  # Swaps the two elements in the list
    end = time.time() - start  # Generate the time and subtract it from the starting time to get the time spent sorting
    if check(data_set=data_set) == -1:  # Checks whether if the data_set is sorted or not
        return -1
    return end * 1000


def merge_sort(data_set):
    """
	Wikipedia: https://en.wikipedia.org/wiki/Merge_sort

    Keeps splitting the parameter data_set into two halves until it is sorted.

    Returns end - time spent sorting when done
    """
    start = time.time()

    def _merge_sort(ds):
        if len(ds) > 1:  # if length of ds is already 2
            # First half of the list being fed into the same function to be split it up and sorted
            mid = len(ds) // 2
            left = ds[:mid]
            right = ds[mid:]

            # First half of the list being fed into the same function to be split
            _merge_sort(left)
            # Second half of the list being fed into the same function to be split it up and sorted
            _merge_sort(right)

            # Merging the left list and right list and making a sorted list
            l, r, i = 0, 0, 0  # l will be for left, and r will be for right, and variable i will be for the current
            # index
            # output = []  # This will be the final output
            while len(left) > l and len(right) > r:
                if left[l] < right[r]:
                    ds[i] = left[l]
                    l += 1
                else:
                    ds[i] = right[r]
                    r += 1
                i += 1
            # Puts the rest of the list (that is not done merging) into output
            while len(left) > l:
                ds[i] = left[l]
                l += 1
                i += 1
            while len(right) > r:
                ds[i] = right[r]
                r += 1
                i += 1

    _merge_sort(data_set)  # This requires recursion, so it is written as a separate procedure

    end = time.time() - start

    if check(data_set=data_set) == -1:
        return -1
    return end * 1000


def counting_sort(data_set):
    """
	Wikipedia: https://en.wikipedia.org/wiki/Counting_sort

    Sorts the parameter data_set using the counting sort algorithm. Uses counting (literally) to compress and
    decompress the data_set array

    Very fast, but takes a lot of space (space depends on the largest value in data_set)
    """
    start = time.time()  # Starting the 'timer'

    biggest = max(data_set)  # Finds the biggest number in the data_set list
    count = [0] * (biggest+1)  # Creates a list of 0's; the size will depend on the biggest number (plus 1)
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
    return end * 1000


def generate_data_set(size):
    """
    Generates a random list with a size of variable size. Value of each element will be between 0 and 100,000

    Determines if size is bigger than 1,000 and smaller than 10,00,000
        - If it is, then it will call the function again and prompts the user for another number
    """
    if 1000 <= size <= 1000000:
        ds = []
        for _ in range(size):
            ds.append(random.randint(0, 10000))
        return ds
    print("Must enter a number that is greater than 1000 and less than 1,000,000!")
    clear()
    # Recursion so main() only needs to call this function once without while loop
    return generate_data_set(int(input("Enter the size of data set (from 1000 to 1,000,000): ")))


def get_user_sort(ds):
    """
    This function gets the user's input to display the time spent sorting the parameter ds using different sorting
    algorithms.

    For bogosort, to improve the time spent running, the size of the data_set is reduced 100 times, but is multiple
    back when determining the time required to sort the data set

    Clears the terminal after everytime the time is displayed and the user presses enter

    If the user presses enter for type_sort variable, then it will exit this function
    """
    bogo_avg = []
    bubble_avg = []
    merge_avg = []
    counting_avg = []
    while True:
        timing = -1
        # Expanded for better readability
        type_sort = input(
            "1. Bogo Sort - Time Complexity: O((n-1)n!)\n"  # Incredibly inefficient, pinnacle of brute force
            "2. Bubble Sort - Time Complexity: O(n^2)\n"  # Most basic and straight forward sorting algorithm
            "3. Merge Sort - Time Complexity: O(n*log(n))\n"  # Very fast and light
            "4. Counting Sort - Time Complexity: O(n+K)\n"  # Very fast, but requires a lot of computational space
            "Enter the number of the sort you want to time (Enter to quit): "
        )
        if not type_sort:
            break

        if int(type_sort) == 1:
            # Since bogosort takes a long time, we can shorten the time the algorithm spends running
            timing = bogo_sort(data_set=ds[:len(ds) // 100]) * 100
            bogo_avg.append(timing)
        elif int(type_sort) == 2:
            timing = bubble_sort(data_set=ds)
            bubble_avg.append(timing)
        elif int(type_sort) == 3:
            timing = merge_sort(data_set=ds)
            merge_avg.append(timing)
        elif int(type_sort) == 4:
            timing = counting_sort(data_set=ds)
            counting_avg.append(timing)
        else:
            print("That is an invalid choice!")
        if timing != -1:
            print(f"Time Required: {timing}ms")
        input("Press Enter to continue...")
        clear()
    clear()
    if input("Do you want to see sorting averages (Y or N): ").lower() == 'y':
        if bogo_avg:
            print(f"Bogo Sort Avg: {sum(bogo_avg) / len(bogo_avg)}ms")
        if bubble_avg:
            print(f"Bubble Sort Avg: {sum(bubble_avg) / len(bubble_avg)}ms")
        if merge_avg:
            print(f"Merge Sort Avg: {sum(merge_avg) / len(merge_avg)}ms")
        if counting_avg:
            print(f"Counting Sort Avg: {sum(counting_avg) / len(counting_avg)}ms")
        input("Press Enter to quit...")
    print("Exiting...")


def main():
    """
    Clears the terminal, so it is easier for the user to read and focus on the program

    Prompts the user to enter an integer that represents the size of the data set.

    The user will then be prompted to select the sorting algorithm. After the function is exited, the main function
    will also exit
    """
    clear()
    print("Welcome to Sorting Simulator!\nPress Enter to quit anytime!")
    # Getting a range of numbers to generate a list of random numbers (1,000 - 10,000,000)
    ds = generate_data_set(size=int(input("Enter the size of data set (from 1000 to 1,000,000): ")))
    # Gets the input of the user and is put into the argument of the function
    clear()
    get_user_sort(ds)
    time.sleep(0.5)


if __name__ == "__main__":
    main()
    clear()
    print("Thank you for using this program!")
