name = input("请输入需要备份的文件名字(加后缀名)")
f = open(name,"r")
content = f.read()

f1 = open("备份.txt","w")
f1.write (content)

f.close()
f1.close()
