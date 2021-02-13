# CS 5381 Algorithms: Project 1


def sum_merge_sort(sum_list, source_list):
    """
    Sorts the list of sums and puts the source files, which are in a single list, in the same order, ensuring that each
    line of the source files remains in the same index as its corresponding sum

    Parameters:
    sum_list (list): A list of integers that is the summed values of all the source files
    source_list(list): A list of the source files, which are lists of integers
    """
    if len(sum_list) == 1:
        return sum_list, source_list
    else:
        q = len(sum_list) // 2

        left = sum_list[:q]
        left_source = []
        for i in range(0, len(source_list)):
            left_source.append(source_list[i][:q])

        right = sum_list[q:]
        right_source = []
        for i in range(0, len(source_list)):
            right_source.append(source_list[i][q:])

        (left, left_source) = sum_merge_sort(left, left_source)
        (right, right_source) = sum_merge_sort(right, right_source)
        return sum_merge(left, right, left_source, right_source)


def sum_merge(left, right, left_source, right_source):
    """
    Merges the items in ascending order from left and right,
    as well as the items in the lists in left_source and right_source in the same order

    Parameters:
    left (list): A list of integers representing the left half of a list to be sorted
    right (list): A list of integers representing the right half of a list to be sorted
    left_source(list): A list of the left halves of source files, which are lists of integers
    right_source(list): A list of the right halves of source files, which are lists of integers
    """
    total = []
    total_source = [[], [], [], [], []]

    l_length = len(left)
    r_length = len(right)
    l_increment = 0
    r_increment = 0
    while l_increment < l_length and r_increment < r_length:
        if left[l_increment] <= right[r_increment]:
            total.append(left[l_increment])
            for i in range(0, len(total_source)):
                total_source[i].append(left_source[i][l_increment])
            l_increment += 1
        else:
            total.append(right[r_increment])
            for i in range(0, len(total_source)):
                total_source[i].append(right_source[i][r_increment])
            r_increment += 1
    if not(l_increment > l_length and r_increment > r_length):
        if l_increment >= l_length:
            for i in range(r_increment, r_length):
                total.append(right[i])
                for j in range(0, len(total_source)):
                    total_source[j].append(right_source[j][i])
        elif r_increment >= r_length:
            for i in range(l_increment, l_length):
                total.append(left[i])
                for j in range(0, len(total_source)):
                    total_source[j].append(left_source[j][i])
    return total, total_source


def inversions_merge_sort(input_list, inversion_count):
    if len(input_list) == 1:
        return input_list, inversion_count
    else:
        q = len(input_list) // 2
        left = input_list[:q]
        right = input_list[q:]
        (left, inversion_count) = inversions_merge_sort(left, inversion_count)
        (right, inversion_count) = inversions_merge_sort(right, inversion_count)
        return inversions_merge(left, right, inversion_count)


def inversions_merge(left, right, inversion_count):
    total = []
    l_length = len(left)
    r_length = len(right)
    l_increment = 0
    r_increment = 0
    while l_increment < l_length and r_increment < r_length:
        if left[l_increment] <= right[r_increment]:
            total.append(left[l_increment])
            l_increment += 1
        else:
            total.append(right[r_increment])
            r_increment += 1
            inversion_count += l_length - l_increment
    if not(l_increment > l_length and r_increment > r_length):
        if l_increment >= l_length:
            for i in range(r_increment, r_length):
                total.append(right[i])
        elif r_increment >= r_length:
            for i in range(l_increment, l_length):
                total.append(left[i])

    return total, inversion_count


def inversions_quick(current_list, inversion_count):
    if len(current_list) <= 1:
        return current_list, inversion_count
    else:
        piv = current_list[0]  # pivot is the first element
        less = []
        greater = []
        equal = []

        for i in range(0, len(current_list)):
            if current_list[i] < piv:
                less.append(current_list[i])
                inversion_count += len(equal) + len(greater)  # One inversion for each element in equal and greater
            elif current_list[i] > piv:
                greater.append(current_list[i])
            else:
                equal.append(current_list[i])
                inversion_count += len(greater)  # One inversion for each element in greater

        (less, inversion_count) = inversions_quick(less, inversion_count)
        (greater, inversion_count) = inversions_quick(greater, inversion_count)

        return (less + equal + greater), inversion_count


def inversions_insertion(source_list):
    count = 0
    sorted_list = source_list.copy()
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        jj = i
        while jj > 0 and sorted_list[jj - 1] > key:
            sorted_list[jj] = sorted_list[jj - 1]
            jj = jj - 1
            count += 1
        sorted_list[jj] = key
    return sorted_list, count


def get_quality(input_files, sorting_algorithm):
    """
    Finds the normalized quality value in each entry in input_files according to the algorithm designated by
    sorting_algorithm

    Parameters:
    input_files (list): A list of integers of length 5 representing the source files
    sorting_algorithm (string): Can be 'merge', 'quick', or 'insertion'; Designates which sorting algorithm to adapt to
        count inversions
    """
    source_files = input_files.copy()
    max_increment = 1
    weights = [1, 1, 1, 1, 1]
    while max_increment > 0.0001:
        sum_files = []
        for i in range(0, len(source_files[0])):
            sum_files.append(source_files[0][i] * weights[0]
                             + source_files[1][i] * weights[1]
                             + source_files[2][i] * weights[2]
                             + source_files[3][i] * weights[3]
                             + source_files[4][i] * weights[4])

        (sum_files, source_files) = sum_merge_sort(sum_files, source_files)

        inversions_count = [None] * 5
        quality = []
        for i in range(0, len(inversions_count)):
            if sorting_algorithm == "merge":
                (temp, inversions_count[i]) = inversions_merge_sort(source_files[i], 0)
            elif sorting_algorithm == "quick":
                (temp, inversions_count[i]) = inversions_quick(source_files[i], 0)
            elif sorting_algorithm == "insertion":
                (temp, inversions_count[i]) = inversions_insertion(source_files[i])

            quality.append(1 / (1 + inversions_count[i]))

        sum_quality = sum(quality)
        length_quality = len(quality)
        quality_normal = []
        for i in range(0, length_quality):
            quality_normal.append(length_quality * quality[i] / sum_quality)

        increments = []
        for i in range(0, len(weights)):
            increments.append(abs(weights[i] - quality_normal[i]))
        weights = quality_normal
        max_increment = max(increments)

    return quality_normal


f1 = open("Source1.txt", 'r')
nums_file1 = f1.readlines()
nums_file1 = [int(i) for i in nums_file1]

f2 = open("Source2.txt", 'r')
nums_file2 = f2.readlines()
nums_file2 = [int(i) for i in nums_file2]

f3 = open("Source3.txt", 'r')
nums_file3 = f3.readlines()
nums_file3 = [int(i) for i in nums_file3]

f4 = open("Source4.txt", 'r')
nums_file4 = f4.readlines()
nums_file4 = [int(i) for i in nums_file4]

f5 = open("Source5.txt", 'r')
nums_file5 = f5.readlines()
nums_file5 = [int(i) for i in nums_file5]

source_files_list = [nums_file1, nums_file2, nums_file3, nums_file4, nums_file5]

print("Merge Sort")
print(get_quality(source_files_list, "merge"))
print("-----------------------------------------------------------------------------------------------\nQuick Sort")
print(get_quality(source_files_list, "quick"))
print("-----------------------------------------------------------------------------------------------\nInsertion Sort")
print(get_quality(source_files_list, "insertion"))
