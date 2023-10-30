import math as mt
n=int(input("Nhap so phan tu n="))


while n<1:
    n=int(input("Nhap so phan tu n="))

my_list=[]

for i in range(n):
    x=int(input(f"a[{i}]="))
    my_list.append(x)
print("List vua nhap la:",my_list)

def scp(x): # so 0 1 4 9 
    return mt.sqrt(x)==mt.isqrt(x)

list_only=[]
for item in my_list:
    if item not in list_only:
        list_only.append(item)
print(f"Trong day co: {len(list_only)} so")

for item in list_only:
    print(f"{item} xuat hien :{my_list.count(item)} lan")

list_scp=[]
for i in range(n):
    if(scp(my_list[i]) and i%2==1):
       list_scp.append(my_list[i])
if(len(list_scp)<1):
    print("khong co scp o vi tri chan!")
else:
    print("trung binh cong cac so chinh phuong vi tri chan la:",sum(list_scp)/len(list_scp))


