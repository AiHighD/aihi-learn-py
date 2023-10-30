
m=int(input("Nhap so hang m="))
n=int(input("Nhap so cot n="))

while m<1:
    m=int(input("Nhap so hang m="))
while n<1:
    n=int(input("Nhap so cot n="))
maxtrix=[]
print("Nhap lan luot cac phan tu:")
a=[]
for i in range(m):
    for j in range(n):
        a.append(int(input(f"a{(i+1),(j+1)}=")))
    maxtrix.append(a)
print("ma tran")
for i in range(m):
    for j in range(n):
        print(maxtrix[i][j],end=" ")
    print()

main_line=([maxtrix[i][i] for i in range(n)])
print("duong cheo chinh:",main_line)
sup_line=([maxtrix[i][n-1-i] for i in range(n)])
print("duong cheo phu:",sup_line)

# chuyen vi mxn => nxm
m,n=n,m
print("chuyen vi")
for i in range(m):
    for j in range(n):
        print(maxtrix[j][i],end=" ")
    print()
    