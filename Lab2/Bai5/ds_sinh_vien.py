from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien import SinhVien
from datetime import datetime
from sv_phi_chinh_quy import SinhVienPhiCQ


class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1

    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
    
    @staticmethod
    def KiemTraSVCoDRL80(sv: SinhVien):
        if not isinstance(sv, SinhVienChinhQuy):
            return False
        if sv.DiemRL >= 80:
            return True
        return False

    def TimSVCoDiemRenLuyen80(self):
        return [sv for sv in self.dssv if self.KiemTraSVCoDRL80(sv)]

    @staticmethod
    def KiemTraSVCongaysinhtrc(sv: SinhVien):
        if not isinstance(sv, SinhVienPhiCQ):
            return False
        if sv.TrinhDo.lower() == "Cao đẳng".lower() and sv.ngaySinh < datetime(1999,8,15):
            return True
        return False

    def TimSVsinhtrcngay(self):
        return [sv for sv in self.dssv if self.KiemTraSVCongaysinhtrc(sv)]