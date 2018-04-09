# coding:utf-8
def selection_sort(a_list):
	'''冒泡排序法'''
	n = len(a_list)
	# 需进行比较的循环次数
	for i in range(n-1):
		min_index = i
		for j in range(i+1,n):
			if a_list[min_index] > a_list[j]:
				min_index = j
		a_list[i], a_list[min_index] = a_list[min_index] , a_list[i]

	print(a_list)

if __name__ == "__main__":
	a = [13,45,675,123,7,32,89,312,45,45432]
	print(a)
	selection_sort(a)

'''最优时间复杂度O(n^2)，没有最优的方式'''
'''最坏时间复杂度O(n^2)'''
'''不稳定'''