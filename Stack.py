class Stack:
    def __init__(self):
        self.__items: list[any] = []
        self.__size: int = 0

    def __str__(self) -> str:
        return str(self.__items) + " <- Cima"

    def empty(self) -> bool:
        return self.__size == 0

    def push(self, item):
        self.__items.append(item)
        self.__size += 1

    def pop(self) -> any:
        assert not self.empty(), "empty stack"
        self.__size -= 1
        return self.__items.pop()

    def peek(self) -> any:
        assert not self.empty(), "empty stack"
        return self.__items[self.__size - 1]

    def __len__(self) -> int:
        return self.__size


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(3)
    my_stack.push(12)
    print(my_stack)
    print(my_stack.peek())
    my_stack.pop()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    print(my_stack)
    print(my_stack.peek())

