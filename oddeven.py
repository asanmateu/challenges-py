def oddeven(lst):
    odds = [i for i in lst if i % 2]
    evens = [i for i in lst if not i % 2]
    return len(odds) > len(evens)


print(oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(oddeven([1, 2, 3, 4, 5, 6, 7, 9]))
