import random
# The random package is used in this program to generate a random integer
import time
# The time package is used in this program to time each sorting algorithm
import os
# The os package is used in this program to clear the terminal
import termcolor
# the termcolor package is used this program to make the output


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check(data_set):
    # This function is used to check if the data_set is sorted
    for i in range(1, len(data_set)):
        if data_set[i] < data_set[i-1]:
            print("Sorting Failed.")
            return -1


class Sorting:
    def __init__(self, data_set):  # This is used to "globalize" the data_set list to all functions in the class
        self.data_set = data_set

    def bubble_sort(self):  # Basic Bubble sort algorithm
        data_set = self.data_set
        start = time.time()
        for i in range(len(data_set)):
            for j in range(len(data_set)-i-1):
                if data_set[j] > data_set[j+1]:
                    data_set[j], data_set[j+1] = data_set[j+1], data_set[j]
        end = time.time() - start
        if check(data_set=data_set) == -1:
            return
        print("Sort Completed!")
        return end

    def counting_sort(self):  # Counting sort algorithm using dictionaries (hashmap)
        data_set = self.data_set
        start = time.time()
        max_num = 0
        for i in range(len(data_set)):
            if max_num < data_set[i]:
                max_num = data_set[i]
        # Counting the numbers
        count = [0] * (max_num + 1)
        for i in range(len(data_set)):
            count[data_set[i]] += 1
        # Getting the output
        output = []
        for i in range(len(count)):
            while count[i] != 0:
                output.append(i)
                count[i] -= 1
        end = time.time() - start
        if check(data_set=data_set) == -1:
            return
        print("Sort Completed!")
        return end

    def selection_sort(self):  # Selection sort algorithm. Space complexity is O(1)!
        data_set = self.data_set
        start = time.time()
        for i in range(len(data_set)):
            smallest_ind = i
            for j in range(i+1, len(data_set)):
                if data_set[smallest_ind] > data_set[j]:
                    smallest_ind = j
            data_set[smallest_ind], data_set[i] = data_set[i], data_set[smallest_ind]
        end = time.time() - start
        if check(data_set=data_set) == -1:
            return
        print("Sort Completed!")
        return end

    def merge_sort(self):
        ...


def main():  # Manages basic user inputs
    print("Welcome to Sorting Simulator!\nPress Enter to quit anytime!")
    while True:
        size_of_data_set = int(input("Enter the size of data set (from 500 to 1,000,000): "))
        if 500 <= size_of_data_set <= 1000000:
            ds = []
            for _ in range(size_of_data_set):
                ds.append(random.randint(0, 10000000))
            sorting = Sorting(data_set=ds)
            break
    while True:
        timing = -1
        type_sort = input(
            "1. Bubble Sort - O(n^2)\n"
            "2. Counting Sort - O(n+K)\n"
            "3. Selection Sort - O(n^2)\n"
            "4. Merge Sort - O(n*log(n))\n"
            "Enter the number of the sort you want to time (Enter to quit): "
        )
        if not type_sort:
            return 0

        if int(type_sort) == 1:
            timing = sorting.bubble_sort()
        elif int(type_sort) == 2:
            timing = sorting.counting_sort()
        elif int(type_sort) == 3:
            timing = sorting.selection_sort()
        else:
            print("That is an invalid choice!")
        if timing != -1:
            print(f"Time Required: {timing * 1000} ms")
            input("Press Enter to continue...")
            clear()


if __name__ == "__main__":
    main()
    print("Thank you!")
