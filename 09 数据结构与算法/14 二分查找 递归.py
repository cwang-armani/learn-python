# coding:utf-8
def binary_search(a_list,item):
    '''递归二分法查找'''
    n = len(a_list)
    if n > 0:
        mid = n//2
        if a_list[mid] == item:
            return True
        elif item < a_list[mid]:
            return binary_search(a_list[:mid],item)
        else:
            return binary_search(a_list[mid+1:],item)

    return False

if __name__ == "__main__":

    a = [17,23,35,45,59,61,75,82,91]
    print(binary_search(a,59))