#-*- coding: utf-8-*-
#调用参数
from sys import argv
#给参数命名
script, filename = argv
#提示要进行擦除的文件
print "We're going to erase %r." % filename 
#提示’不同意‘操作
print "If you don't want that ,hit CTER-C (^C) "
#提示‘同意’操作
print "If you do want that, hit ENTER."
#提示输入符号
raw_input ("?")
#提示将打开文件
print "Opening the file..."
#定义打开文件实体参数
target = open (filename, 'w')
#提示删除操作
print "Truncating the file.  Goodbye!"
#进行删除操作
target.truncate
#说明接下来的问题
print "Now I'm going to ask you for three lines."
#定义输入的问题
line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input("line 3 :")
#提示将回答放入文件中
print "I'm going to write these to the file."
#进行写入文件操作
target.write(line1+'\n'+line2+'\n'+line3)
#提示将关闭文件
print "And finally ,we colse it."
#进行关闭文件操作
target.colse()
