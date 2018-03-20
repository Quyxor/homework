class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, *args):
        self.first = None
        self.last = None
        self.length = 0
        if args:
            for item in args:
                self.add(item)


    def add(self, value):
        if self.first is None:
            self.first = self.last = ListNode(value)
            self.length = 0
        else:
            tmp = self.last
            self.last = tmp.next = ListNode(value)
            self.length += 1


    def __get_by_index(self, index):
        if index < 0:
            return None
        counter = 0
        item = self.first

        while item.next is not None:
            if counter == index:
                break
            counter += 1
            item = item.next
        return item


    def insert(self, index, value):
        if index >= self.length:
            self.add(value)
            return
        item = self.__get_by_index(index-1)
        if not item:
            new_item = self.first = ListNode(value, self.first)
        else:
            new_item = ListNode(value, item.next)
            item.next = new_item


    def get(self, index):
        if index > self.length:
            raise IndexError
        return self.__get_by_index(index).data


    def remove(self, value):
        if self.first is None:
            return
        prev = curr = self.first
        if value == self.first.data:
            self.first = self.first.next
            return
        while curr is not None:
            if curr.data == value:
                if curr.next == self.last:
                    curr = self.last
                    break
                else:
                    prev.next = curr.next
                    break
            prev = curr
            curr = curr.next


    def remove_at(self, index):
        if index == 0:
            value = self.first.data
            self.first = self.first.next
        elif index < self.length:
            prev = self.__get_by_index(index - 1)
            value = prev.next.data
            prev.next = prev.next.next
        else:
            raise IndexError

        return value


    def clear(self):
        self.__init__()


    def contains(self, value):
        if self.first is None:
            return False
        prev = curr = self.first
        if value == self.first.data:
            return True
        while curr is not None:
            if curr.data == value:
                return True
                break
            prev = curr
            curr = curr.next
        return False


    def len(self):
        if self.first is None:
            return 0
        return self.length + 1


    def is_empty(self):
        return self.first is None


    def __iter__(self):
        return LinkedListIterator(self.first)


    def print_it(self):
        item = self.__get_by_index(0)
        print('----------------')
        while item:
            print(item.data)
            item = item.next


class LinkedListIterator(object):
    def __init__(self, head):
        assert isinstance(head, ListNode)
        self.__current = head


    def __next__(self):
        if self.__current is None:
            raise StopIteration

        value = self.__current.data
        self.__current = self.__current.next

        return value


if __name__ == '__main__':
    ll = LinkedList(1, 2, 3, 4, 5)
    ll.print_it()
    ll.insert(0, 10)
    ll.print_it()
    ll.insert(3, -10)
    ll.remove_at(3)
    ll.print_it()
    print(ll.is_empty())
