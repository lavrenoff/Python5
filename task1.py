#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data="Python абв Delphi абв"
print(data)
res=[i for i in data.split() if "абв" not in i]
print(" ".join(res))