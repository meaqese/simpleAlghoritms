class SelectionSort:
    @classmethod
    def find_smallest(cls, array: list) -> int:
        smallest, smallest_index = array[0], 0

        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index

    def sort(self, array: list) -> list:
        new_list = []

        for i in range(len(array)):
            smallest_index = self.find_smallest(array)
            new_list.append(array.pop(smallest_index))
        return new_list


list_for_test = [56, 25, 4, 32, 6]

sorter = SelectionSort()
print(sorter.sort(list_for_test))
