def sum_2_nums(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)   #enpty tuple
    print(kwargs) #enpty tuple
    
    result=a+b
    for num in args:
        result+=num
    print(result)

sum_2_nums(11,2,33,44,task=99,done=55) #带名字以字典的形式保存于**kwargs中