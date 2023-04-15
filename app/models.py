from datetime import datetime
from app import db, app
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, Float, Enum, Text, Boolean, Date, Time
from enum import Enum as UserEnum, Enum as StatusEnum, Enum as DayInWeekEnum, Enum as TinhTrangEnum, \
    Enum as TrangThaiEnum
from flask_login import UserMixin


# Tat ca cac model deu phai ke thua db.Model
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class GiangVien(BaseModel):
    ho_gv = Column(String(50), nullable=True)
    ten_gv = Column(String(50), nullable=True)
    gioi_tinh = Column(String(15), nullable=True)
    day = relationship('Day', backref='giang_vien', lazy=True)

    def __str__(self) -> str:
        return self.ho_gv + self.ten_gv


class TinhTrang(TinhTrangEnum):
    SU_DUNG_DUOC = 1
    BAO_TRI = 2


class PhongHoc(BaseModel):
    ten_phong = Column(String(15), nullable=False)
    kich_co = Column(Integer, nullable=False)
    tinh_trang = Column(Enum(TinhTrang))
    lop_hoc = relationship('LopHoc', backref='phong_hoc', lazy=True)
    phieu_muon_phong = relationship('PhieuMuonPhong', backref='phong_hoc', lazy=True)

    def __str__(self) -> str:
        return self.ten_phong


class CaHoc(BaseModel):
    ten_ca = Column(String(100), nullable=False)
    gio_bat_dau = Column(Time)
    gio_ket_thuc = Column(Time)
    lop_hoc = relationship('LopHoc', backref='ca', lazy=True)
    phieu_muon = relationship('PhieuMuonPhong', backref='ca', lazy=True)

    def __str__(self) -> str:
        return self.ten_ca


class TaiKhoan(BaseModel, UserMixin):
    dai_dien_to_chuc = Column(String(50), nullable=False)
    ho_ten = Column(String(50), nullable=False)
    gmail = Column(String(50), nullable=True)
    so_dien_thoai = Column(String(10), nullable=True)
    mat_khau = Column(String(50), nullable=False)
    so_luot = Column(Integer, default=1)
    loai_tai_khoan = Column(String(50), nullable=False)
    mssv = Column(String(10), nullable=False)
    da_bi_khoa = Column(Boolean, default=False)
    phieu_muon = relationship('PhieuMuonPhong', backref='tai_khoan', lazy=True)

    def __str__(self) -> str:
        return self.ho_ten


class MonHoc(BaseModel):
    ten_mon = Column(String(50), nullable=False)
    lop_hoc = relationship('LopHoc', backref='mon_hoc', lazy=True)

    def __str__(self) -> str:
        return self.ten_mon


class DayInWeek(DayInWeekEnum):
    MON = 1
    TUE = 2
    WED = 3
    THUR = 4
    FRI = 5
    SAT = 6
    SUN = 7


class TrangThai(TrangThaiEnum):
    DANG_CHO_DUYET = 1
    TU_CHOI = 2
    SAN_SANG = 3
    THANH_CONG = 4
    THAT_BAI = 5
    DA_HUY = 6


class LopHoc(BaseModel):
    thu_trong_tuan = Column(Enum(DayInWeek))
    mon_hoc_id = Column(Integer, ForeignKey(MonHoc.id), nullable=False)
    ca_id = Column(Integer, ForeignKey(CaHoc.id), nullable=False)
    phong_hoc_id = Column(Integer, ForeignKey(PhongHoc.id), nullable=False)
    day = relationship('Day', backref="lop_hoc", lazy=True)


class Day(BaseModel):
    gv_id = Column(Integer, ForeignKey(GiangVien.id), nullable=False)
    lop_hoc_id = Column(Integer, ForeignKey(LopHoc.id), nullable=False)


class PhieuMuonPhong(BaseModel):
    thoi_gian_dat = Column(DateTime)
    ngay_muon = Column(Date)
    ly_do = Column(Text)
    tai_khoan_id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)
    ca_id = Column(Integer, ForeignKey(CaHoc.id), nullable=False)
    phong_hoc_id = Column(Integer, ForeignKey(PhongHoc.id), nullable=False)
    trang_thai = Column(Enum(TrangThai))


if __name__ == '__main__':
    with app.app_context():
        # pass
        db.drop_all()
        db.create_all()
        # name = 'Admin'
        # username = 'admin'
        # password = str(hashlib.md5('1'.encode('utf-8')).hexdigest())
        # avatar = 'https://res.cloudinary.com/dxjkpbzmo/image/upload/v1669562707/user_admin-removebg-preview_xtqp2h.png'
        # user = UserAccount(name=name, username=username, password=password, avatar=avatar, user_role=UserRole.ADMIN)
        # db.session.add(user)
        # db.session.commit()
        # db.drop_all()
