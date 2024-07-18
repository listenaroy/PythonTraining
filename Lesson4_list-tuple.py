
#有序可變動列表List
grades=[12,60,15,70,90]
print(grades)
print(grades[0])

grades[0]=55
print(grades)

#連續刪除列表中1到4(不包含)的資料
grades[1:4]=[]
print(grades)

grades = grades+[12,33]
print(grades)

#取得列表的長度len(列表資料)
length = len(grades)
print(length)

#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data)
print(data[0][0:2])

data[0][0:2] = [5,5]
print(data[0])
print(data)

#有序不可變動列表：Tuple
data=(3,4,5)
print(data[0:2])

#錯誤：Tuple的資料不可變動
data[0]=5