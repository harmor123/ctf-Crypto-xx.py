# Time: 2023/4/25 19:58
import quopri

message = input("需要解密的内容：")
result = quopri.decodestring(message).decode('u8')
print (result)


