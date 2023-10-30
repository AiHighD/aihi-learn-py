"""
        Kiem tra so
"""
print("="*20,"Luong Trong Huan","="*20)
# Nhap a
a=int(input("a="))
'''
# Ktra chan le

if(a%2==1):
    print(f"{a} la so le")
else:
    print(f"{a} la so chan")
    
# Ktra am duong

if(a<0):
    print(f"{a} la so am")
elif(a>0):
    print(f"{a} la so duong")
else:
    print(f"{a} la so 0")

i=1

while(i<=a):
    print("*"*i)
    i=i+1
'''
'''
# tinh tong
i = 1
s = 0
while(i<=a):
    s=s+i
    i=i+1
print("tong la: ",s)
'''
# vong while
'''
i=1
s=0
while(a<=1 or a>=10):
    a=int(input("Nhap lai a="))
while(i<=a):
    s=s+i
    i=i+1
print("Tong la",s)
'''

#vong for with break

i=1
s=0
for i in range(1,a+1):
    s=s+i
    if(i==3): # dk ket thuc vong for
        break #ket thuc for khi gap dk cua if
print(f"s={s}")

i=1
s=0
#vong for with continue
for i in range(1,a+1):
    if(i==3): # dk ket thuc vong for
        continue # bo qua dk cua if chay tiep chuong trinh
    s=s+i
print(f"s={s}")

