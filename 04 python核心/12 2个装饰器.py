'''在未调用函数时，就已经进行装饰'''
'''定义函数：完成包裹数据'''

def makeBold(fn):
    def wrapped():
        print("----1---")
        return "<b>" + fn() + "</b>"
    return wrapped

'''定义函数：完成包裹数据'''
def makeItalic(fn):
    def wrapped():
        print("----2---")
        return "<i>" + fn() + "</i>"
    return wrapped


'''先使用makeitalic 装饰test后 再使用makecold装饰 test3'''

'''相当于test3 = makeBold(test3)'''
'''相当于test3 = makeItatic(test3)'''
@makeBold
@makeItalic
def test3():
    print("----3---")
    return "hello world-3"

ret = test3()
print(ret)
