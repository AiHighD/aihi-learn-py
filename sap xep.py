import math as mt
# ham kiem tra so chinh phuong
def scp(x):
    return mt.sqrt(x)==mt.isqrt(x)

# =============================================================================
n=int(input("Nhap so phan tu:"))

my_list=[]
while n<=0:
    n=int(input("Nhap so phan tu:"))
for i in range(n):
    x=int(input(f"a[{i}]="))
    my_list.append(x)
print(my_list)

for item in my_list:
    if scp(item):        
        max_scp=item
for item in my_list:
    if scp(item) and max_scp<item :
        max_scp=item

print("so scp lon nhat:",max_scp)

# for i in range(len(my_list)-1):
#     min_e=min(my_list[i:])
#     index=my_list[i:].index(min_e)+i
#     if min_e<my_list[i]:
#         my_list[i],my_list[index]=my_list[index],my_list[i]


# for i in range(len(my_list) - 1):
#         for j in range(len(my_list) - i - 1):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print(my_list)


