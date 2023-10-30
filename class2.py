# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:11:48 2023

@author: admix
"""

class HCN:
    def __init__(self,chieuDai,chieuRong):
        
        self.chieuDai=chieuDai
        self.chieuRong=chieuRong
    def hienThi(self):
        print("Kich thuoc hcn la: {0}x{1}".format(self.chieuDai,self.chieuRong))
    
    def tinhChuVi(self):
        print("chu vi la:",(self.chieuDai+self.chieuRong)*2)
    def tinhDienTich(self):
        print("dien tich la:",(self.chieuDai*self.chieuRong))

hcn1=HCN(35,20)

hcn1.hienThi()
hcn1.tinhChuVi()
hcn1.tinhDienTich()


