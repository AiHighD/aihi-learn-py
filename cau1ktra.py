"""
            Luong Trong Huan
"""

class SinhVien:
    def __init__(self,maSV,tenSV,namSinh,diemTB):
        self.maSV=maSV
        self.tenSV=tenSV
        self.namSinh=namSinh
        self.diemTB=diemTB 
    def nhap(self):
        self.maSV = input("Nhap ma sinh vien: ")
        self.tenSV = input("Nhap ten sinh vien: ")
        self.namSinh = int(input("Nhap nam sinh: "))
        self.diemTB = float(input("Nhap diem trung binh: "))
    def xuat(self):
        print()
        print("Ma sinh vien la:",self.maSV)
        print("Ten sinh vien la:",self.tenSV)
        print("Sinh nam:",self.namSinh)
        print("Diem trung binh:",self.diemTB)
        print()

sv1=SinhVien("","",0,0)
sv1.nhap()
sv1.xuat()

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien=[]
    def nhap(self):
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print("\nNhap thong tin sinh vien thu", i+1)
            maSV = input("Ma sinh vien: ")
            tenSV = input("Ten sinh vien: ")
            namSinh = int(input("Nam sinh: "))
            diemTB = float(input("Diem trung binh: "))
            sv = SinhVien(maSV, tenSV, namSinh, diemTB)
            self.listSinhVien.append(sv)
    def xuat(self):
        print()
        print("Danh sach sinh vien:")
        index=1
        for sv in self.listSinhVien:
            print()
            print(f"Sinh vien thu {index}:")
            sv.xuat()
            index+=1
            
    def tuoi(self):
        print()
        index=1
        for sv in self.listSinhVien:
            print(f"tuoi sinh vien thu {index} la:",2023-sv.namSinh)
            index+=1
        print()
    def hienThiTen(self):
        ten=input("Nhap ten sinh vien can hien thi:")
    
        for sv in self.listSinhVien:
            if ten not in sv.tenSV:
                print("khong co hoc sinh nay")
            if(ten==sv.tenSV):
                print("Ma sinh vien:",sv.maSV)
                print("Ten sinh vien:",sv.tenSV)
                print("Nam sinh:",sv.namSinh)
                print("Diem trung binh:",sv.diemTB)
        
Quan_ly_sinh_vien=QuanLySinhVien()
Quan_ly_sinh_vien.nhap()
Quan_ly_sinh_vien.xuat()
Quan_ly_sinh_vien.tuoi()
Quan_ly_sinh_vien.hienThiTen()




