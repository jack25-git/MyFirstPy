f=open("./test_file_data.txt","r",encoding="utf-8")
# line=f.readline()
# print(line)
# content=f.read()
# print(content)
w=open("./test_write_file.txt","w",encoding="utf-8")
lines=f.readlines()
for line in lines:
    print(line)
    w.write(line+"write")


f.close()