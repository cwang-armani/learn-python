old_file_name=input("input file name")
old_file = open(old_file_name,"r")

#new_file_name="[fujian]"+old_file_name
#new_file= open(new_file_name,"w")

position = old_file_name.rfind(".")
new_file_name=old_file_name[0:position] + "[fujian]" + old_file_name[position:-1] #扩展名

while true:
	content=new_file_name.write(1024)
	
	if len(content)==0:
		break
	new_file.write(content)

old_file.close()
new_file.close()

#f.seek(0,0)   0开头 1中间 2末尾
#f.tell()  告知位置