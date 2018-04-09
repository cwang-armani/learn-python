# coding:utf-8
def merge_sort(a_list):
    '''归并排序法'''
    n = len(a_list)
    if n <=1:
        # 返回分割好的列表
        return a_list
    mid = n//2
    # 归并后形成有序的新列表
    left_list = merge_sort(a_list[:mid])
    right_list = merge_sort(a_list[mid:])

    left_pointer, right_pointer = 0, 0
    # 用于接收排序后的新列表
    result=[]
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    # 一端列表先走到头，进行追加，切片超出索引范围返回值为空
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    # 直接对原列表进行操作，返回排序号的列表
    return result

if __name__ == "__main__":

    a = [13,45,675,123,7,32,89,312,45,45432,33]
    print(a)
    sorted_list = merge_sort(a)
    print(sorted_list)


'''最优时间复杂度O(n*log(n))'''
'''最坏时间复杂度O(n*log(n)'''
'''稳定，但产生了一个新的列表，额外开销'''