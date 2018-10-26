from tree import Node
from suffix_tree import SuffixNode

a = Node(5)
b = Node(3)
c = Node(1)

a = SuffixNode('a', 1, 1)
b = SuffixNode('b', 2, 5)
c = SuffixNode('c', 6)

b.start = 4, 'd'
b.end = 4

print(a.get_string('Happyyness'))
print(b.get_string('Happyyness'))
print(c.get_string('Happyyness'))

a.add_child(b)
a.add_child(c)
# a.add_child(b)
print(b.parent)
