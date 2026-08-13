numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(40)
print("After remove:", numbers)

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

print("Length of List:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
