'''   Kiểu dữ liệu
'''
#
print("="*20,"Lương Trọng Huấn","="*20)
'''
nam = 2023
x = 2.5
lop = "KHMT 20A"

print(type(nam))
print(type(x))
print(type(lop))
#
a,b=5,6

print("Gia tri:", a,b)

a,b = b,a

print("Hoan vi:", a,b)
#
print(not(0))
#
print("x=",end='')  #end=' ' thì không xuống dòng
x= int(input())     #x=
y= int(input("y=")) #y=
print(x,"+",y,"=",x+y)
print(f"{x} / {y} = {x/y}")
print(f"{x} + {y} = {x+y}") 
print(f"{x} - {y} = {x-y}") 
print(f"{x} * {y} = {x*y}") 
#
'''

a = int(input("a="))
i=1
tong=0
for i in range(1,a+1):
    tong=tong+i**i
    print(tong)
print(tong)
