# isupper() => lay ra chu hoa
# islower() => lay ra chu thuong
# isdigit()=> lay ra chu so
# upper()=> doi thanh chu hoa
# lower()=> doi thanh chu thuong
# 
"""
        String with .py
"""
str1=input("Nhap vao ho va ten:")
print("xin chao",str1)
# =============================================================================
# print("do dai chuoi:",len(str1))
# print("Xoa khoang trang truoc:",str1.strip())
# print("chuoi chu hoa",str1.upper())
# print("chuoi chua thuong",str1.lower())
# =============================================================================


# # lay ra chu thuong va dem so chu thuong
# list_kt_thuong=len([item for item in str1 if item.islower()])
# # lay ra chu Hoa va dem so ky tu
# list_kt_Hoa=len([item for item in str1 if item.isupper()])
# # lay ra chu so va dem so chu so
# list_kt_so=len([item for item in str1 if item.isdigit()])


# =============================================================================
# if(str1.startswith("Le")):
#     print("Day la ho Le")
# else:
#     print("Khong phai ho Le")
# 
# if(str1.endswith("Anh")):
#     print("Ten la Anh")
# else:
#     print("Khong phai ten Anh")
# 
# if(str1.find("Le") !=-1):
#     print("Day la ho Le")
# else:
#     print("Khong phai ho Le")
# 
# print("tach chuoi",str1.split(" "),str1.split(" ")[-1])
# 
# print("Chuoi doi dao nguoc:",str1[::-1])
# 
# list_word=str1.split(" ")
# 
# print(list_word)
# # Tim chuoi doi xung 
# for item in list_word:
#     if(item==item[::-1]):
#         print(item)
# # tong cac so trong chuoi
# s=0
# n=int(input("Nhap n="))
# 
# for kt in str(n):
#     s=s+int(kt)
# print("Tong cac so la:",s)
# 
# # list chu cai
# 
# list_thuong=[chr(i) for i in range(ord('a'),ord('z')+1)]
# list_hoa=[chr(i) for i in range(ord('A'),ord('Z')+1)]
# 
# print(list_hoa,list_thuong)
# 
# #tao list nhanh voi dieu kien
# 
# list_1=[i for i in range(0,21)]
# #danh sach so le cua list_1
# list_2=[i for i in list_1 if i%2==1]
# 
# print("danh sach duoc tao",list_1)
# print("danh sach so le",list_2)
# =============================================================================



