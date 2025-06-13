import matplotlib.pyplot as plt

def assignment(new_list, new_index, old_list, old_index):
    new_list[new_index] = old_list[old_index]


def merge_sort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
    ):
        midpoint = len(list_to_sort_by_merge) // 2
        left_list = list_to_sort_by_merge[:midpoint]
        right_list = list_to_sort_by_merge[midpoint:]

        merge_sort(left_list)
        merge_sort(right_list)

        left_index = 0
        right_index = 0
        sorted_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] <= right_list[right_index]:
                assignment(new_list=list_to_sort_by_merge, new_index=sorted_index, old_list=left_list, old_index=left_index)
                left_index += 1
            else:
                assignment(new_list=list_to_sort_by_merge, new_index=sorted_index, old_list=right_list, old_index=right_index)
                right_index += 1
            sorted_index += 1

        while left_index < len(left_list):
            list_to_sort_by_merge[sorted_index] = left_list[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right_list):
            list_to_sort_by_merge[sorted_index] = right_list[right_index]
            right_index += 1
            sorted_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x_values = range(len(my_list))
plt.plot(x_values, my_list)
plt.show()
merge_sort(my_list)
x_values = range(len(my_list))
plt.plot(x_values, my_list)
plt.show()
