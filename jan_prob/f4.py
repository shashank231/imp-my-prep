a = set([1, 2, 3, 4])
b = set([1, 2, 5])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

print(a.isdisjoint(b))  # Return True if two sets have a null intersection.
