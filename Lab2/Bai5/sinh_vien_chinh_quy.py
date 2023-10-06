from sinh_vien import SinhVien
from datetime import datetime


class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int):
        super().__init__(maSo, hoTen, ngaySinh)
        self.__diemRL = diemRL

    def __str__(self) -> str:
        return super().__str__()+f"{self.__diemRL}"

    @property
    def DiemRL(self):
        return self.__diemRL

    @DiemRL.setter
    def DiemRL(self, diemRL):
        self.__diemRL = diemRL
