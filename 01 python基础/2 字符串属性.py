my_str="hello world itcast and itcastxxxcpp"
print(my_str.find("laowang"))
print(my_str.find("world"))
print(my_str.rfind("itcast"))
print(my_str.count("itcast"))
print(my_str.replace("xxx","666"))
print(my_str.split(" ")) #啥也不填 包括\t 拆分
print(my_str.capitalize())
print(my_str.lower())
print(my_str.upper())
print(my_str.title())
file_name="laowang.txt"
print(file_name.endswith(".txt"))
print(file_name.startswith("laowang"))
lyric="想要陪你一起看大海"
print(lyric.center(60))
print(lyric.ljust(60))
print(lyric.rjust(60))
test=lyric.center(50)
print(test.lstrip())
print(test.rstrip())
