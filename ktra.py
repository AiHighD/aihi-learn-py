print("*"*10,"Luong Trong Huan","*"*10) # de 01

# 1.a
# n = int(input("n="))

# while n<0:
#     print("Nhap lai!")
#     n = int(input("n="))
# i=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# 1.b

# n = int(input("n="))
# while n<0:
#     print("Nhap lai!")
#     n = int(input("n="))
# s=0
# i=1
# for i in range(1,n+1):
#     s+=i**3
# print(f"tong cua day la {s}")

# 2a
# checksnt = True
# i=1
# n = int(input("n="))
# while n<0:
#     print("Nhap lai!")
#     n = int(input("n="))
# if n<2:
#     checksnt=False
# elif n==2:
#     checksnt=True
# elif n%2==0:
#     checksnt=False
# else:
#     for i in range(3,n,2):
#         if n%i == 0:
#             checksnt=False
# if checksnt==True:
#     print(n,"la so nguyen to")
# else:
#     print(n,"khong la so nguyen to")
#2 b
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
i=1
ucln = 0
while a<0 or b<0 or c<0:
    print("Nhap lai!")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))

for i in range(1,min(a,b,c)+1):
    if a%i==0 and b%i==0 and c%i==0:
        ucln = i
print(ucln,f"la ucln cua {a},{b},{c}")  

# cho so co 3 chu so, tach ra hang chuc, hang tram, hang don vi

# a = int(input("a=")) # nhap so co 3 chu so

# donvi=int(a%10)
# chuc=int((a%100)/10)
# tram=int(a/100)

# print("hang don vi la",donvi)
# print("hang chuc la",chuc)
# print("hang tram la",tram)

