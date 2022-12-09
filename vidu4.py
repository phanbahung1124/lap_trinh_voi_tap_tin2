from Student import SinhVien
class SinhVien:
    def __init__(self, fullname, yob, score):
        self.hoten = fullname
        self.namsinh = yob
        self.dtb = score
    def __str__(self):
        message = '[hoten: ' + self.hoten + ';namsinh:' + str(self.namsinh) + ';dtb:' + str(self.dtb) + ']'
        return message
    def __gt__(self, obj):
        return(self.dtb > obj.dtb)
    def __ge__(self,obj):
        return(self.dtb >= obj.dtb)
    def __lt__(self,obj):
        return(self.dtb < obj.dtb)
    def __le__(self,obj):
        return(self.dtb <= obj.dtb)
    def __eq__(self,obj):
        return(self.dtb == obj.dtb)

def main():
    sv = [SinhVien('Pham Nhat Huy', 2004, 10),SinhVien('Phan Ba Hung', 2004, 11),SinhVien('Le Nguyen Vu Duy', 2004, 8.0),SinhVien('Phan Nam Ha', 2004, 7.0),SinhVien('Tran Huu Bao Anh', 2004, 9.0),SinhVien('Nguyen Nhat Minh', 2004, 8.5)]
    sv = sorted(sv, reverse= True)
    for item in sv:
        print(item)
    sv2 = sorted(sv)
    for item in sv:
        print(item)
if __name__ =='__main__':
    main()