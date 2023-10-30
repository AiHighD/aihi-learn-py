n=int(input("Nhap so phan tu n="))
my_list=[]

while n<=0 :
    print("Nhap lai!")
    n=int(input("Nhap so phan tu n="))
print("==========")
for i in range(n):
    x=int(input(f"l[{i}] = "))
    my_list.append(x)
print("list vua nhap:",my_list)

x=int(input("Nhap x="))

#ktra xem x co xuat hien trong list hay khong va o vi tri nao
while i<n:
    if x not in my_list:
        print("x khong co o trong list")
    else:
        for i in range(n):
            if(my_list[i]==x):
                print(f"{x} xuat hien tai: l[{i}]")
    i=i+1

# or

if x not in my_list:
    print("x khong co o trong list")
else:
    print(f"{x} xuat hien tai: ",end = "")
    for i in range(n):
        if(my_list[i]==x):
            print(i, end =" ")

