import matplotlib.pyplot as plt

def assignment(new_list, new_index, old_list, old_index):
    """
    Weist einen Wert von einer Liste zu einer anderen zu.
    
    Args:
        new_list: Zielliste
        new_index: Index in der Zielliste
        old_list: Quellliste
        old_index: Index in der Quellliste
    """
    new_list[new_index] = old_list[old_index]


def merge_sort(list_to_sort_by_merge):
    """
    Sortiert eine Liste mit dem Merge-Sort-Algorithmus 
    und überschreibt dise in der sortierten Version
    
    Args:
        list_to_sort_by_merge: Die zu sortierende Liste
    """

    # Ueberpruefen ob es der uebergebene Wert eine Liste ist
    if not isinstance(list_to_sort_by_merge, list):
        raise TypeError("Input muss eine Liste sein")
    
    #Listen mit 0 oder 1 Element sind bereits sortiert
    if (
        len(list_to_sort_by_merge) > 1
    ):
        # Divide: Liste in zwei Hälften teilen
        midpoint = len(list_to_sort_by_merge) // 2
        left_list = list_to_sort_by_merge[:midpoint]
        right_list = list_to_sort_by_merge[midpoint:]

        # Rekursiv beide Hälften sortieren
        merge_sort(left_list)
        merge_sort(right_list)
        # Combine: Sortierte Hälften zusammenführen
        # Index Variabeln, zum durchgehen der linken, rechten und sortierten Liste
        left_index = 0
        right_index = 0
        sorted_index = 0

        # Merge-Phase: Vergleiche Elemente aus beiden Listen
        # Das kleinere Element wird in die ursprüngliche Liste eingefügt
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] <= right_list[right_index]:
                assignment(
                    new_list=list_to_sort_by_merge, 
                    new_index=sorted_index, 
                    old_list=left_list, 
                    old_index=left_index
                )
                left_index += 1
            else:
                assignment(
                    new_list=list_to_sort_by_merge, 
                    new_index=sorted_index, 
                    old_list=right_list, 
                    old_index=right_index
                )
                right_index += 1
            sorted_index += 1

        # Restliche Elemente zur orginalen Liste hinzufügen, 
        # falls eine der beiden Listen noch Elemente hat
        while left_index < len(left_list):
            assignment(
                new_list=list_to_sort_by_merge, 
                new_index=sorted_index, 
                old_list=left_list, 
                old_index=left_index
            )
            left_index += 1
            sorted_index += 1

        while right_index < len(right_list):
            assignment(
                new_list=list_to_sort_by_merge, 
                new_index=sorted_index, 
                old_list=right_list, 
                old_index=right_index
            )
            right_index += 1
            sorted_index += 1

# Liste wird mit Werten sortiert und eine weitere Liste, x_values, wird erstellt,
# sodass diese die einzelnen Indizes der andren Liste enthält. Ein Plot wird erstellt 
# welcher die Liste als y-Werte animmt und die x_values als x-Werte
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x_values = range(len(my_list))
plt.plot(x_values, my_list)
plt.show()

# Die Liste wird sortiert und es wird erneut ein Plot erstellt
merge_sort(my_list)
x_values = range(len(my_list))
plt.plot(x_values, my_list)
plt.show()
