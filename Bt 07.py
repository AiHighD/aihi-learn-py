import math as mt
n=int(input("Nhap so phan tu n="))
my_list=[]

while n<=1 or n>=100:
    print("Nhap lai!")
    n=int(input("Nhap so phan tu n="))
print("==========")
for i in range(n):
    x=int(input(f"l[{i}] = "))
    my_list.append(x)
print("danh sach vua nhap:",my_list)
# Ham ktra so hoan hao
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
# list_shh_vtChan=[]
# for i in range(n):
#     if (kt_shh(my_list[i]) and i%2==1):
#         list_shh_vtChan.append(my_list[i])
# print("Cac so hoan hao trong danh sach o vi tri chan",list_shh_vtChan)

# def kt_scp(x):
#     return mt.sqrt(x)==mt.isqrt(x)

# list_scp_vt_le =[]
# for i in range(n):
#     if(kt_scp(my_list[i]) and i%2==0):
#         list_scp_vt_le.append(my_list[i])
# print("danh sach scp vi tri le:",list_scp_vt_le)

# list_scp_in_list=[]
# k=int(input("nhap k="))
# for i in range(n):
#     if(kt_scp(my_list[i]) and my_list[i]<k):
#         list_scp_in_list.append(my_list[i])
# print(f"Cac so chinh phuong trong danh sach nho hon {k}:",list_scp_in_list)    


# def kt_snt(x):
#     if x<2: return False
#     else:
#         for i in range(2,mt.isqrt(x)+1):
#             if x%i==0:
#                 return False
#         return True
# list_snt=[]
# for i in range(n):
#     if(kt_snt(my_list[i])):
#         list_snt.append(my_list[i])
# print("cac so nguyen to trong danh sach:",list_snt)
# def liet_ke_nt(n):
#     list_n_snt=[]
#     num=2
#     dem=0
#     while dem<n:
#         if(kt_snt(num)):
#            list_n_snt.append(num)
#            dem=dem+1
#         num=num+1
#     return list_n_snt

# n = int(input("Nhập số nguyên tố cần liệt kê: "))

# ketqua=liet_ke_nt(n)
# print(f"{n} so nguyen to dau tien la: {ketqua}")

# Hàm chèn 1 số x vào sau vị trí đầu danh sách

def chen_x(x):
    my_list.insert(1, x)
    return my_list

x=int(input("Nhap x="))
chen_x(x)
print(my_list)





