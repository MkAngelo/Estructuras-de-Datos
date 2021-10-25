from node import Node


# Simple
idx = 1
head = Node(1, None)
probe = head

while idx < 10:
    probe.next = Node(idx + 1, None)
    probe = probe.next
    idx += 1

probe = head
while probe.next != None:
    val = probe.data
    probe = probe.next
    print(val)

print('*'*20)
# Circle
index = 1
new_item = 'ham'
head = Node('Hello', None);
head.next = head
probe = head

while index > 0 and probe.next != head:
    probe = probe.next
    index += 1

probe.next = Node(new_item, probe.next)
print(probe.next.data)
