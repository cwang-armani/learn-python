class Deque(object):
    '''定义一个栈'''
    def __init__(self):
        self.__item = []

    def is_empty(self):
        # 判断列表是否为空
        return self.__item == []

    def add_front(self,item):
        # 入队
        self.__item.insert(0,item)
        return item

    def add_rear(self,item):
        # 入队
        self.__item.append(item)
        return item

    def pop_front(self):
        # 出队
        return self.__item .pop(0)

    def pop_rear(self):
        # 出队
        return self.__item .pop()

    def size(self):
        return len(self.__item)

if __name__ == "__main__":
    q = Deque()

    print(q.add_rear(1))
    print(q.add_rear(4))
    print(q.add_front(5))
    print(q.add_front(6))
    print(q.add_rear(1))
    print(q.add_rear(4))
    print("-"*20)
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_front())