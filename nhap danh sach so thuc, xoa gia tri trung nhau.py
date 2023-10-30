'''
        Bai tap
'''

#1. nhap vao danh sach so thuc, loai bo cac phan tu trung nhau

n=int(input("Nhap so phan tu n="))

my_list=[]

while n<=0:
    n=int(input("Nhap so phan tu n="))

for i in range(n):
    x=float(input(f"a[{i}] = "))
    my_list.append(x)
print("Danh sach vua nhap la: ",my_list)

#set chi nhan gia tri khong trung nhau
# my_list=list(set(my_list))
# print(my_list)

#
# new_list=[]
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)
#

