print("="*40)
print("name management system")
print("1.append new name")
print("2.del name")
print("3.modify name")
print("4.vlook name")
print("5.all")
print("6.exit")
print("="*40)
names=["laoli","laozhao","shabi"]

card_infor=[] #存储名片
while True:
    num = int(input("please input you act:"))
    if num==1:
        new_name = input("添加新名字:")
        new_qq=input("添加新qq:")
        new_wechat = input("添加新wechat:")
        new_addr = input("添加新住址:")
        #定义新字典 存储名片
        new_infor={}
        new_infor["name"]=new_name
        new_infor["qq"] = new_qq
        new_infor["wechat"] = new_wechat
        new_infor["addr"] = new_addr
        #字典添加到列表中,字典是没有顺序的
        card_infor.append(new_infor)
        #print(card_infor) for test

    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        find_name=input("write name you wanna find:")
        find_flag=0 #默认没找到名字
        for temp in card_infor:
            if find_name==temp['name']:
                print("%s \t%s \t%s \t%s" %(temp['name'],temp['qq'],temp['wechat'],temp['addr']))
                find_flag=1 #找到了
                break
        if find_flag==0:
            print("not find")
    elif num == 5:
        print("name\tqq\twechat\taddr")
        for temp in card_infor:
            print("%s \t%s \t%s \t%s" %(temp['name'],temp['qq'],temp['wechat'],temp['addr']))
    elif num == 6:
        break
    else:
        print("your input is wrong")