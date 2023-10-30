'''
        Bai tap ve nha 06- Luong Trong Huan
'''
import math as mt
n=int(input("Nhap n="))
while n<0:
    print("Nhap lai!")
    n=int(input("Nhap n="))
# def kt_scp(x):
#     return mt.sqrt(x)==mt.isqrt(x)
# def kt_snt(x):
#     if x<2: return False
#     else:
#         for i in range(2,mt.isqrt(x)+1):
#             if x%i==0:
#                 return False
#         return True
# def kt_shh(x):
#     tong=0
#     if x==0:
#         return False
#     for i in range(1,x):
#         if x%i==0:
#             tong=tong+i
#     if tong==x:
#         return True
#     else:
#         return False
    
def tinhTongS(x):
    S=0
    for i in range(1,x+1):
        S=S+i
    return S
print("Tong la",tinhTongS(n))

# if(kt_scp(n)):
#     print(n,"la so cp")
# else:
#     print(n,"khong la so cp")

# if(kt_snt(n)):
#     print(n,"la snt")
# else:
#     print(n,"khong la snt")
    
# if(kt_shh(n)):
#     print(n,"la shh")
# else:
#     print(n,"khong la shh")
    
