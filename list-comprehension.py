# Lists in Python can be defined as a collection of arbitrary objects.
# Written as a comma-separated sequence of objects in square brackets.
a = ['foo', 'bar', 'baz', 'qux']
print(a)

# Important characteristics of lists:
# - lists are ordered
a = ['foo', 'bar', 'baz', 'qux'] 
b = ['baz', 'qux', 'bar', 'foo']
print(a == b)
print(a is b)
print([1, 2, 3, 4] == [4, 1, 3, 2])

# - lists can contain any arbitrary object
a = [2, 4, 6, 8]
print(a)
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)
# Lists can contain complex objects like functions, classes, and modules.
def foo():
    pass
import math
a = [int, len, foo, math]
print(a)


# - list elements can be accessed by index
# - lists can be nested to arbitrary length
# - lists are mutable
# - lists are dynamic
