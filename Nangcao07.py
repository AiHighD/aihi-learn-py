import math as mt

n=int(input("Nhap vao so phan tu n="))

while n<1 or n>100:
    n=int(input("Nhap vao so phan tu n="))

# =============================================================================
# my_list=[]
# 
# for i in range(n):
#     x=int(input(f"a[{i}]="))
#     my_list.append(x)
# print(my_list)
# =============================================================================

# =============================================================================
# m1=[]
# m2=[]
# for i in range(n):
#     if (my_list[i]<0):
#         m1.append(my_list[i])
#     else:
#         m2.append(my_list[i])
# print("<0 :",m1,"   ",">0 :",m2)
# =============================================================================

def snt(x):
    if x<2:
        return False
    else:
        for i in range(2,mt.isqrt(x)):
            if x%i==0:
                return False
    return True

def scp(x):
    return mt.sqrt(x)==mt.isqrt(x)

def shh(x):
    tong=0
    for i in range(1,int(x/2)+1):
        if x%i==0:
            tong=tong+i
    if(tong==x):
        return True
    else:
        return False
# l_snt=[]
# l_scp=[]
# l_shh=[]
# for item in my_list:
#     if(scp(item)):
#         l_scp.append(item)
# for item in my_list:
#     if(snt(item)):
#         l_snt.append(item)
# print(max(l_scp))

# max=l_scp[0]
# for item in l_scp:
#     if(item>max):
#         max=item
# print(max)
# print(min(l_snt))

# =============================================================================
# max=my_list[0]
# for i in range(n):
#     if(my_list[i]>max):
#         max=my_list[i]
#         vitri=i
#
# print(max,f"tai a[{vitri}]")
# =============================================================================

# =============================================================================
# list_am=[]
# 
# for item in my_list:
#     if(item<0):
#         list_am.append(item)
# tong=0.0
# for item in list_am:
#     tong=tong+item
# print("gia tri trung binh la: ",tong/len(list_am))
# =============================================================================


            


        
            