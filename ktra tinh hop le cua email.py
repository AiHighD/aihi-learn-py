# check email hop le
import re
email=input("Nhap email:")

check='^[a-z_]+[a-z]+[-._0-9]*@[a-z]+.[a-z]+[0-9]+.vn$' # '^   &' ký hiệu bắt đầu('^) và ký hiệu kết thúc($') // dấu * có nghĩa là có thể có hoặc k
#'^[a-z_]+[a-z]+[-._0-9]*@[ictu]+.[edu]+.[vn]$' # bắt đầu bằng a-z hoặc _, chắc chắn phải có a-z @ chắc chắn có ictu + . chắc chắn có edu + . chắc chắn có vn
emailcheck= re.search(check, email)

if emailcheck:
    print("email hop le!")
else:
    print("email khong hop le!")
