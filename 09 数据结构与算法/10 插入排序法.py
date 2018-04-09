# coding:utf-8
def insert_sort(a_list):
	'''插入排序法'''
	n = len(a_list)
	# 从右边无序序列取出多少个元素执行这样的过程
	for j in range(1,n):
		i = j
		# 内层循环，从右侧无需序列取出元素，插入前面序列正确位置
		while i > 0:
			if a_list[i] < a_list[i-1]:
				a_list[i], a_list[i-1] = a_list[i-1] , a_list[i]
				i -= 1
			# 拿出的元素大于等于左端最大数，执行
			else:
				break

	print(a_list)

if __name__ == "__main__":

	a = [13,45,675,123,7,32,89,312,45,45432]
	print(a)
	insert_sort(a)

'''最优时间复杂度O(n)，没有最优的方式'''
'''最坏时间复杂度O(n^2)'''
'''稳定'''