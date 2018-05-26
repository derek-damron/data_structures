class NodeDoubly:
    def __init__(self, value, prev=None, next=None):
        self.set_value(value)
        self.set_prev(prev)
        self.set_next(next)
        
    def set_value(self, value):
        self._value = value
        
    def set_prev(self, prev):
        self._prev = prev
        
    def set_next(self, next):
        self._next = next
        
class LinkedListDoubly:
    def __init__(self):
        self._head = None
        self._tail = None
        return
        
    def get_length(self):
        out = 0
        if self._head is not None:
            current_node = self._head
            out += 1
            while current_node._next is not None:
                current_node = current_node._next
                out += 1
        return out
        
    def as_list_forward(self):
        out = []
        if self._head is not None:
            current_node = self._head
            out += [current_node._value]
            while current_node._next is not None:
                current_node = current_node._next
                out += [current_node._value]
        return out
        
    def as_list_backward(self):
        out = []
        if self._tail is not None:
            current_node = self._tail
            out = [current_node._value] + out
            while current_node._prev is not None:
                current_node = current_node._prev
                out = [current_node._value] + out
        return out

    def put_head(self, value):
        node = NodeDoubly(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            prev_head = self._head
            prev_head.set_prev(node)
            node.set_next(prev_head)
            self._head = node
        return
        
    def put_tail(self, value):
        node = NodeDoubly(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            prev_tail = self._tail
            prev_tail.set_next(node)
            node.set_prev(prev_tail)
            self._tail = node
        return
        
    def put_index(self, value, index):
        index = int(index)
        self_len = self.get_length()
        if index < 0:
            raise ValueError("index must be >= 0")
        elif index == 0:
            self.put_head(value)
        elif index < self_len:
            node = NodeDoubly(value)
            current_node = self._head
            i = 0
            while i < index:
                current_node = current_node._next
                i += 1
            # Set previous
            prev_node = current_node._prev
            prev_node.set_next(node)
            node.set_prev(prev_node)
            # Set next
            node.set_next(current_node)
            current_node.set_prev(node)
        elif index == self_len:
            self.put_tail(value)
        if index > self_len:
            raise ValueError("index exceeds list length")
        return
            
x = LinkedListDoubly()
print(x.get_length())
x.put_head(1)
print(x.as_list_forward())
print(x.as_list_backward())
x.put_head(2)
print(x.as_list_forward())
print(x.as_list_backward())
x.put_head(3)
print(x.as_list_forward())
print(x.as_list_backward())
print(x.get_length())

x.put_tail(1)
print(x.as_list_forward())
print(x.as_list_backward())
x.put_tail(2)
print(x.as_list_forward())
print(x.as_list_backward())
x.put_tail(3)
print(x.as_list_forward())
print(x.as_list_backward())
print(x.get_length())