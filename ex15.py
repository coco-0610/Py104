#-*- coding: utf-8-*-
# 获取文件名
from sys import argv
script, filename = argv
# 定义文件的变量名
txt = open (filename)
print "Here's your file %r:" % filename
# 打开文件
print txt.read()
print "Type the filename again:"
# 提示变量输入字符
file_again = raw_input(">")
# 文件的一个变量名
txt_again = open(file_again) 
# 输出文件内容
print txt_again.read()
print txt.close()
print txt_again.colse()
