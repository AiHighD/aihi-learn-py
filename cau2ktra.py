class SinhVien:
    def __init__(self,maSV,tenSV,queQuan,diemTB):
        self.maSV=maSV
        self.tenSV=tenSV
        self.queQuan=queQuan
        self.diemTB=diemTB
    def nhap(self):
        self.maSV = input("Nhap ma sinh vien: ")
        self.tenSV = input("Nhap ten sinh vien: ")
        self.queQuan = (input("Nhap que quan: "))
        self.diemTB = float(input("Nhap diem trung binh: "))
    def xuat(self):
        print()
        print("Ma sinh vien la:",self.maSV)
        print("Ten sinh vien la:",self.tenSV)
        print("Que quan:",self.queQuan)
        print("Diem trung binh:",self.diemTB)
        print()
sv1=SinhVien("", "", "", 0)
sv1.nhap()
sv1.xuat()
class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien=[]
    def nhap(self):
        n=int(input("Nhap vao so sinh vien:"))

        for i in range(n):
            print(f"Nhap thong tin sinh vien thu {i+1}:")
            maSV=input("Nhap ma sinh vien:")
            tenSV=input("Nhap ten sinh vien:")
            queQuan=(input("Nhap que quan:"))
            diemTB=float(input("Nhap diem trung binh:"))
            print()
            sv=SinhVien(maSV, tenSV, queQuan, diemTB)
            self.listSinhVien.append(sv)
    
    def xuat(self):
        print("Danh sach sinh vien:")
        index=1
        for sv in self.listSinhVien:
            print()
            print(f"Sinh vien thu {index}:")
            sv.xuat()
            index+=1

    def thongTin(self):
        print()
        print("Danh sach sinh vien co que quan Thai Nguyen la:")
        for sv in self.listSinhVien:
            if "Thai Nguyen" not in sv.queQuan:
                print("Khong co ai o Thai Nguyen!")
            if(sv.queQuan=="Thai Nguyen"):
                sv.xuat()
    def sapXepDTB(self):
        print()
        print("Danh sach sau sắp xếp:")
        self.listSinhVien.sort(key=lambda sv: sv.diemTB)
        Quan_ly_sinh_vien.xuat()
    def hienThiMaxDTB(self):
        list_dtb=[sv.diemTB for sv in self.listSinhVien ]
        print("Diem trung binh max la:")
        print(max(list_dtb))

Quan_ly_sinh_vien=QuanLySinhVien()
Quan_ly_sinh_vien.nhap()
Quan_ly_sinh_vien.xuat()
Quan_ly_sinh_vien.sapXepDTB()
Quan_ly_sinh_vien.thongTin()
Quan_ly_sinh_vien.hienThiMaxDTB()


