def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_list = my_list.copy()
mergeSort(sorted_list)
x_values = range(len(my_list))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x_values, my_list, 'ro-', linewidth=2, markersize=6)
ax1.set_title("Original Data")
ax1.set_xlabel('Index', fontsize=12)
ax1.set_ylabel('Value', fontsize=12)
ax1.spines[['top', 'right']].set_visible(False)
ax2.plot(x_values, sorted_list, 'go-', linewidth=2, markersize=6)
ax2.set_title("Sorted Data")
ax2.set_xlabel('Index', fontsize=12)
ax2.set_ylabel('Value', fontsize=12)
ax2.spines[['top', 'right']].set_visible(False)
plt.show()
