# n=int(input("N="))
# print(f"tinh tong cac so tu 1->{n}:",n*(n+1)/2)
"""
        dictionnary with py
"""

#khai bao dict

dicMonHoc={
    "mon hoc":"Lap trinh python",
    "So tin chi": 3,
    "He dao tao":"dhcq"
}

print(dicMonHoc)

#khai bao dict
dictBock=dict()
print(type(dictBock))

#lay gia tri

print("mon hoc:",dicMonHoc["mon hoc"])
print("so tin chi:",dicMonHoc.get("So tin chi"))

#lay ra các khóa, giá trị
print(dicMonHoc.keys())
print(dicMonHoc.values())

#Duyệt các phần tử

for ikey in dicMonHoc:
    print(ikey,":",dicMonHoc[ikey])

# thêm, sửa, xóa trong dict

dicMonHoc["hoc phi"]=377
dicMonHoc["nam hoc"]=2023
# sửa
dicMonHoc["nam hoc"]=2003
# xóa
dicMonHoc.__delitem__("mon hoc")

#

print(dicMonHoc)
print(len(dicMonHoc))

dicDiemPY={"huan":10,"huy":9,"khanh":9,"thang":8}
print(type(dicDiemPY))

print("diem trung binh la:",sum(dicDiemPY.values())/len(dicDiemPY))

n=int(input("Nhap so sinh vien:"))

#khai bao dict
dictDiem=dict()

for i in range(n):
    ikey=input("Nhap ten sinh vien:")
    ivalue=int(input("Nhap diem:"))
    dictDiem[ikey]=ivalue
print("Danh sach:",dictDiem)


print(max(dictDiem.values()))