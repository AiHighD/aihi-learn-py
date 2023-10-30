# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:26:41 2023

@author: admix

            Nhap xuat cho class va tra cuu thong tin
"""

class Video:
    def __init__(self,tenVideo,tacGia,theLoai,namSanXuat):
        self.tenVideo=tenVideo
        self.tacGia=tacGia
        self.theLoai=theLoai
        self.namSanXuat=namSanXuat

    # def hienthi(self):
    #     print("ten video la:",self.tenVideo)
    #     print("ten tac gia:",self.tacGia)
    #     print("the loai phim:",self.theLoai)
    #     print("nam xuat ban:",self.namSanXuat)
        
# vd1=Video("siuuuuuu", "anh bay", "phim hai ", "2020") # nhap gian tiep
# vd1.hienthi()

class QuanLy:
    def __init__(self):
        self.listVideo=[]
    def add(self,tenVideo,tacGia,theLoai,namSanXuat):
        vd=Video(tenVideo, tacGia, theLoai, namSanXuat)
        self.listVideo.append(vd)
    def hienthi(self):
        print()
        print("danh sach video:")
        index=1
        for vd in self.listVideo:
            print()
            print(f"video thu {index}:")
            print("ten video la:",vd.tenVideo)
            print("ten tac gia:",vd.tacGia)
            print("the loai phim:",vd.theLoai)
            print("nam xuat ban:",vd.namSanXuat)
            index+=1
    def find(self):
        print()
        print("danh sach video nam 2023:")
        for vd in self.listVideo:
            if (vd.namSanXuat==2023):
                print()
                print("ten video la:",vd.tenVideo)
                print("ten tac gia:",vd.tacGia)
                print("the loai phim:",vd.theLoai)
                print("nam xuat ban:",vd.namSanXuat)
quan_ly_video=QuanLy()

n=int(input("Nhap vao so luong video:"))

for i in range(n):
    print(f"Nhap thong tin video thu {i+1}:")
    tenVideo=input("Nhap ten video:")
    tacGia=input("Nhap ten tac gia:")
    theLoai=input("Nhap the loai:")
    namSanXuat=int(input("Nhap nam san xuat:"))
    print()
    quan_ly_video.add(tenVideo, tacGia, theLoai, namSanXuat)
quan_ly_video.hienthi()
quan_ly_video.find()
# tenVideo=input("Nhap ten video:")
# tacGia=input("Nhap ten tac gia:")
# theLoai=input("Nhap the loai:")
# namSanXuat=int(input("Nhap nam san xuat:"))
# vd=Video(tenVideo, tacGia, theLoai, namSanXuat)
# vd.hienthi()

