def sum_2_nums(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)   #enpty tuple
    print(kwargs) #enpty tuple

A=(33,44,55)
B={"name":"laowang","age":48}

sum_2_nums(11,2,*A,**B) #带名字以字典的形式保存于**kwargs中