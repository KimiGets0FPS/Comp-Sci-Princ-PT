import random
# The random package is used in this program to generate a random integer
import time
# The time package is used in this program to time each sorting algorithm


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

    def counting_sort(self):
        data_set = self.data_set
        start = time.time()
        end = time.time() - start
        if check(data_set=data_set) == -1:
            return
        print("Sort Completed!")
        return end


def main():  # Manages basic user inputs
    print("Welcome to Sorting !\nPress Enter to quit anytime!")
    while True:
        size_of_data_set = int(input("Enter the size of data set (from 500 to 1,000,000): "))
        if 500 <= size_of_data_set <= 1000000:
            ds = []
            for _ in range(size_of_data_set):
                ds.append(random.randint(0, 10000000))
            sorting = Sorting(data_set=ds)
            break
    while True:
        type_sort = input(
            "1. Bubble Sort - O(n^2)\n"
            "2. Counting Sort - O(n+K)\n"
            "3. \n"
            "4. \n"
            "Enter the number of the sort you want to time (Enter to quit): "
        )
        if not type_sort:
            return 0

        if int(type_sort) == 1:
            timing = sorting.bubble_sort()
        elif int(type_sort) == 2:
            timing = ...
        elif int(type_sort) == 3:
            timing = ...
        else:
            timing = ...
        if timing != -1:
            print(f"Time Required: {timing * 1000} ms")


if __name__ == "__main__":
    main()
    print("Thank you!")
