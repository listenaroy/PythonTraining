# break:    強制結束迴圈
n=1
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print("last: ",n)

#continue:  強制繼續下一圈
print("")
n=0 
for x in range(0,4):
    if x%2==0:
        continue
    n+=1
print(n)

#eles: 迴圈結束前執行動作
n=1
while n<5:
    print(n)
    n+=1
else:
    print("hi")

print("")
for c in "Hello":
    print(c)
else:
    print("end")

print("")
sum=0
for n in range(11): #range(11)=1~10
    sum+=n
else:
    print(sum)


#綜合範例：找出整數平方根

n=input("輸入整數: ")
n=int(n)
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break   #break 強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")