# coding:utf-8
def quick_sort(a_list,start,end):
	'''快速排序法'''
	if start >= end:
		return

	mid_value = a_list[start]
	low = start
	high = end
	while low != high:
		# 移动high游标向左
		while low < high and a_list[high] >= mid_value:
			high -= 1
		a_list[low] = a_list[high]
		# 移动low游标向右
		while low < high and a_list[low] < mid_value:
			low += 1
		a_list[high] = a_list[low]

	# 循环退出时 low == high
	a_list[high] = mid_value

	# 嵌套调用，传输原有的列表
	# low左端
	quick_sort(a_list,start,high-1)
	# low右端
	quick_sort(a_list,high+1,end)

if __name__ == "__main__":

	a = [13,45,675,123,7,32,89,312,45,45432]
	print(a)
	quick_sort(a,0,len(a)-1)
	print(a)


'''最优时间复杂度O(n*log(n))'''
'''最坏时间复杂度O(n^2),每次只分出一个部分'''
'''不稳定'''