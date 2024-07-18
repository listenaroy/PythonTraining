#---數字運算---

#加法
x=3+6
print(x)

#乘法
x=3*6
print(x)

#小數除法
x=3/6
print(x)

#整數除法
x=3//6
print(x)

#次方
x=2**0.5
print(x)

#取餘數
x=7%3
print(x)

#x=x+1 #將變數中的數字+1
#x=x-1 #將變數中的數字-1
#x=x*1 #將變數中的數字*1
x+=1
print(x)


#---字串運算---
s="Hello"
print(s)

s= "Hell\"o"
print(s)

#字串串接
s = "Hello"+"Word"
print(s)
#Python特有語法
s = "Hello" "Word"
print(s)

#多行字
s = "Hello\nWord"
print(s)
#Python特有語法
s = """Hello
Word"""
print(s)

#字串重複計算
s = "Hello"*3+"Word"
print(s)

#字串會對內部的字元進行編號(索引)，從0開始算起
s="Hello"
print(s[0])
print(s[1:4])
print(s[1:])
print(s[:4])
