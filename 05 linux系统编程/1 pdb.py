import pdb
def avg(a,b):
	result = a + b
	print("result=%d"%result)
	return result

num1 = 1
num2 = 3
ret = avg(num1,num2)
print(ret)

'''linux系统调试'''
'''控制程序在哪个位置停止 需增加断点'''
#list l 显示当前代码 带箭头 l键有时候不好使 先按n执行一步代码
#next n 向下执行下一步代码
#continue c 继续执行代码(断点处继续向下执行，跟没调试时一样)
#break b 设置断点 continue命令时执行到该位置
#clear清除断点
#step s 进入到一个函数，先要设置一个断点
#quit q 退出调试

'''函数处设置断点，step，s进入到一个函数，print，p打印形参数值，arg打印所有形参数值'''