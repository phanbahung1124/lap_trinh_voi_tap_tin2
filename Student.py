
class SinhVien:
    def __init__(self,fullname,yob,score):
        self.hoten = fullname
        self.namsinh = yob
        self.dtb = score
    def __str__(self):
        message = '[hoten: '+self.hoten+';namsinh:' + str(self.namsinh) + ';dtb:' + str(self.dtb)+']'
        return message


def main():
    sv1 = SinhVien('Le Duy Anh',2004,10)
    sv2 = SinhVien('Phan Ba Hung',2004,10)
    print(sv1)

if __name__ =="__main__":
    main()