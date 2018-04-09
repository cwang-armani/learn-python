class Queue(object):
    '''定义一个栈'''
    def __init__(self):
        self.__item = []

    def is_empty(self):
        # 判断列表是否为空
        return self.__item == []

    def enqueue(self,item):
        # 入队
        self.__item.append(item)
        return item

    def dequeue(self):
        # 出队
        return self.__item .pop(0)

    def size(self):
        return len(self.__item)

if __name__ == "__main__":
    q = Queue()

    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print("-"*20)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())