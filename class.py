"""
        opp with .py
"""

class ConNguoi:
    hoTen="Trong Huan"
    tuoi=20
    gioiTinh="nam"
print(ConNguoi)

print(ConNguoi.hoTen)

class SinhVien:
    maSV="dtc21h4801010006"
    lopHoc="KHMTK20A"
    monHoc="Python"
    namHoc=2023
    def hienThi(self):
        print("ma sv",self.maSV)
        print("lop hoc",self.lopHoc)
        print("nam hoc",self.namHoc)
class SinhVien2:
    def __init__(self,idSV,namHoc,monHoc):
        self.maSV=idSV
        self.namHoc=namHoc
        self.monHoc=monHoc
    def hienThi(self):
        print("ma sv",self.maSV)
        print("lop hoc",self.monHoc)
        print("nam hoc",self.namHoc)
  # Kế thừa      
class SinhVienKHMT(SinhVien):
    def __init__(self,idSV,namHoc,monHoc,nganhHoc):
        #ke thua lop cha
        super().__init__(idSV,namHoc,monHoc)
        #khai bao cac thuoc tinh moi
        self.nganhHoc=nganhHoc
        
    def hienThi(self):
        #ke thua lop cha
        super().hienThi()
        print("nganh hoc: ",self.nganhHoc)
    
class KHMT_K20A(SinhVienKHMT):
    def __init__(self, idSV, namHoc, monHoc, nganhHoc,khoaHoc):
        super().__init__(idSV, namHoc, monHoc, nganhHoc)
        self.khoaHoc=khoaHoc
    def hienThi(self):
        super().hienThi()
        print("khoa hoc: ",self.khoaHoc)

sv1=SinhVien()
sv2=SinhVien2("dtc21", 2000, "python")
sv2.hienThi()
class HocSinh:
    pass
name=sv1.monHoc
age=sv1.namHoc
classroom=sv1.lopHoc
idSV=sv1.maSV
sv1.hienThi()
print(name,age,classroom,idSV)


