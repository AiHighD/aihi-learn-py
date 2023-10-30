'''
    List
'''
import math as mt
#ham ktra scp trong list
def kt_nt_vt(x):
    if n<2:
        return False
    for i in range(2,mt.isqrt(n)+1):
        if x%i==0:
            return False
    return True
def kt_scp(x):
    return (mt.sqrt(x)==mt.isqrt(x))

#nhap vao 1 list
n=int(input("Nhap so phan tu n="))
l=[]

while n<=0 or n>=100:
    print("Nhap lai!")
    n=int(input("Nhap so phan tu n="))
print("==========")
for i in range(n):
    x=int(input(f"l[{i}] = "))
    l.append(x)
print(l)
# list_scp=[]
# for i in range(n):
#     if(kt_scp(l[i])):
#         list_scp.append(l[i])
# print(list_scp)

#sap xep tang
print("sap xep tang",sorted(l))
#sap xep giam
print("sap xep giam",sorted(l, reverse=True))

#lay ra phan tu am
list_am = []

list_scp = []

# for item in l:
#     if item<0:
#         list_am.append(item)
# print(list_am)
#
# for item in l:
#     if(kt_scp(item)):
#         list_scp.append(item)
#         l.remove(item)
# print(list_scp)

#ktra nguyen to
# list_nt=[]

# for i in range(n):
#     if kt_nt_vt(l[i] and i%2==0):
#         list_nt.append(l[i])
# print(list_nt)

# lst1 = [1,3,5,6,7]
# print("Dao nguoc list",lst1[::-1])
# print("list con",lst1[1:3:1])
# print("so phan tu",len(lst1))
# lst1.append(8) # them phan tu vao cuoi danh sách

new_list=l # gán new_list= list cũ, khi xóa 1 giá trị của list cũ thì list mới cũng mất

new_list_2=l.copy() #copy list, khi xóa giá trị list copy k bị mất

l.__delitem__(0) # del item vi tri 0

print(l,new_list,new_list_2)

#duyet tren mang copy thi gia tri index k bi dich chuyen, vi vay nen duyet tren mang copy, sau do remove gia tri tren ham chinh
#vidu

list_copy=l.copy()


        
        

