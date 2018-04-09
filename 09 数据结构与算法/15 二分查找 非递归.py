# coding:utf-8
def binary_search(a_list,item):
    '''归并排序法'''
    n = len(a_list)
    start= 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if a_list[mid] == item:
            return True
        elif a_list[mid] < item:
            start = mid +1
        else:
            end = mid -1
    return False

if __name__ == "__main__":

    a = [17,23,35,45,59,61,75,82,91]
    print(binary_search(a,45))