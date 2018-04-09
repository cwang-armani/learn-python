# coding:utf-8
def bubble_sort(a_list):
	'''冒泡排序法'''
	n = len(a_list)
	for i in range(n-1):
		count = 0
		# 中间的某次已经排序好了，直接跳出循环
		for j in range(n-i-1):  # 游标
			if a_list[j] > a_list[j+1]:
				a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
				count += 1
		if count == 0:
			break

	print(a_list)

if __name__ == "__main__":
	a = [13,45,675,123,7,32,89,312,45432]
	print(a)
	bubble_sort(a)

'''最优时间复杂度O(n),一次成型'''
'''最坏时间复杂度O(n^2)'''
'''稳定性好'''