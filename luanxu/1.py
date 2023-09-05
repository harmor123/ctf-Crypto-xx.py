# -*- coding: utf-8 -*-
# Time: 2023/6/9 17:43
# Editor:harmor
# 读取乱序文件内容
with open("1.txt", "rb") as file:
    content = file.read()

# 按照要求进行分组和空格分隔
grouped_content = [content[i:i+8] for i in range(0, len(content), 8)]
formatted_groups = [group.decode() for group in grouped_content]

# 将内容按照每行4组进行分割，并添加空格分隔
lines = [formatted_groups[i:i+4] for i in range(0, len(formatted_groups), 4)]
formatted_lines = "\n".join([" ".join(line) for line in lines])

# 写入恢复内容到新文件
with open("recovered.hex", "w") as file:
    file.write(formatted_lines)

