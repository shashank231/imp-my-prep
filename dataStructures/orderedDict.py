
# Feature	                                dict (Python 3.7+)     OrderedDict
# Insertion order preserved?	               ✅ Yes	            ✅ Yes
# Methods for reordering (move_to_end)         ❌ No	                ✅ Yes
# Equality check includes order?	           ❌ No                 ✅ Yes
# Performance	                               🚀 Faster	         🐢 Slightly Slower

from collections import OrderedDict

# Usage
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])



# Normal vs Ordered
d1 = dict()
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
print(d1)
d1.popitem() # takes no arg
d1.pop('a')  # takes one arg
print(d1)



# Special Features of OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# move an item to end or beginning
od.move_to_end('b')  # Move 'b' to end
od.move_to_end('a', last=False)  # Move 'a' to beginning
# popitem: remove last/first inserted item
od.popitem(last=True)   # pop last item
od.popitem(last=False)  # pop first item



# LRU cache using OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # move to end as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used


