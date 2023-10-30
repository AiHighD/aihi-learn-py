n=int(input("Nhap so phan tu n="))


while n<1:
    n=int(input("Nhap so phan tu n="))

my_list=[]

for i in range(n):
    x=int(input(f"a[{i}]="))
    my_list.append(x)
print("List vua nhap la:",my_list)

k=int(input("Nhap k="))

while i<n:
    if k not in my_list:
        print(f"{k} khong co o trong list")
    else:
        print(f"{k} xuat hien tai:",end=" ")
        for i in range(n):
            if(my_list[i]==k):
                print(f"a[{i}]",end=" ")
    i=i+1
    
print()
list_tbc=[]
for item in my_list:
    if item%2==1 and item%5==0:
        list_tbc.append(item)

print("trung binh cong cac so le chia het cho 5 la: ",sum(list_tbc)/len(list_tbc))
