from sinh_vien import SinhVien
from datetime import datetime


class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int):
        super().__init__(maSo, hoTen, ngaySinh)
        self.__thoiGianDaoTao = tgdt
        self.__trinhdo = trinhdo

    def __str__(self) -> str:
        return super().__str__()+f"{self.__trinhdo}\t{self.__thoiGianDaoTao}"

    @property
    def TrinhDo(self):
        return self.__trinhdo

    @TrinhDo.setter
    def TrinhDo(self, trinhdo):
        self.__trinhdo = trinhdo
