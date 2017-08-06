# 提示输入文件名
print "Type your filename:"
# 输入文件名
filename = raw_input(">")
# 定义打开文件函数
txt = open (filename)
# 输出文件内容
print txt.read()
