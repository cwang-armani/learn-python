infor={"age":18,"addr":"jiznhou","qq":38776358}

infor['name']='wanj'
del infor["age"]
infor.get("qq")

print(infor.keys())
print(infor.values())
print(len(infor))
# if "qq" in infor.keys()

infor2={"age":18,"addr":"jiznhou","qq":38776358,"qq2":3476358}

#for temp in infor2.keys():
    #print(temp)
#for temp in infor2.values():
    #print(temp)
for temp in infor2.items():
    print(temp)

for a,b in infor2.items():
    print("keys=%s values=%s"%(a,b))