str1=input("Nhap vao chuoi ky tu:")

list_word=str1.split(" ")

for item in list_word:
    if(item==item[::-1]):
        print(item)

list_word=str1.split("@")
print(list_word[0])

