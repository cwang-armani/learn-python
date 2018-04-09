# coding:utf-8
def shell_sort(a_list):
	'''希尔排序法'''
	n = len(a_list)
	# 对gap取整
	gap = n//2
	# gap==1为普通的插入排序
	while gap >= 1:
		# 从右边无序序列取出多少个元素执行这样的过程
		for j in range(gap,n):
			i = j
			# 内层循环，从右侧无需序列取出元素，插入前面序列正确位置
			while i > 0:
				if a_list[i] < a_list[i-gap]:
					a_list[i], a_list[i-gap] = a_list[i-gap] , a_list[i]
					i -= gap
				# 拿出的元素大于等于左端最大数，执行
				else:
					break
		# 缩短gap步长
		gap = gap // 2

	print(a_list)

if __name__ == "__main__":

	a = [13,45,675,123,7,32,89,312,45,45432]
	print(a)
	shell_sort(a)


'''最优时间复杂度O(n^1.3)'''
'''最坏时间复杂度O(n^2),此时gap==1'''
'''不稳定，拆分后的部分无关'''