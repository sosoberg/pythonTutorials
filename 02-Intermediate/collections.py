#  collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaaabbbbccc"

my_counter = Counter(a)

print(my_counter.items())