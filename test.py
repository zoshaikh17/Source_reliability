from project import inversions_merge_sort
from project import inversions_quick
from project import inversions_insertion

testList = [8, 9, 11, 1, 8, 2]

# (sortedList, inversionCount) = inversions_merge_sort(testList, 0)

# (sortedList, inversionCount) = inversions_quick(testList, 0)

(sortedList, inversionCount) = inversions_insertion(testList)

print("Array is:")
print(testList)
print("Inversion Count is:")
print(inversionCount)
print("Sorted array is:")
print(sortedList)
# should be 9 inversions
