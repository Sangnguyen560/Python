class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)

    @staticmethod
    def __TimUCLN(a, b):
        while b:
            a, b = b, a % b
        return a

    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq


x = PhanSo(int(input("Nhập tử  số thứ nhất: ")), int(input("Nhập mẫu số thứ nhất: ")))
y = PhanSo(int(input("Nhập tử  số thứ hai: ")), int(input("Nhập mẫu số thứ hai: ")))

print(f'''\nKết Quả các bài toán phân số:
{x} + {y}= {x+y}
{x} - {y}= {x-y}
{x} x {y}= {x*y}
{x} / {y}= {x/y} ''')


