# Time: 2023/4/25 19:58
'''
学习网址：https://blog.csdn.net/as604049322/article/details/120399475
'''
import quopri

message = input("需要加密的内容：")
result = quopri.encodestring(message.encode('u8'),quotetabs= True)
print (result)