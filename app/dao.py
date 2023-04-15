from datetime import datetime
from sqlalchemy import and_, or_
from app.models import PhongHoc, CaHoc, TaiKhoan, LopHoc, PhieuMuonPhong
from app import db


def auth_user(username, password):
    return TaiKhoan.query.filter(TaiKhoan.mssv.__eq__(username),
                                    TaiKhoan.mat_khau.__eq__(password)).first()


def load_room(so_lau):
    query = PhongHoc.query
    if so_lau:
        query = query.filter(PhongHoc.ten_phong.startswith(so_lau))
    return query.all()


def get_tai_khoan_by_id(user_id):
    return TaiKhoan.query.get(user_id)


def load_ca_hoc():
    return CaHoc.query.all()


def get_ca_hoc(ca_hoc_id):
    return CaHoc.query.get(ca_hoc_id)


def get_lich_hoc(so_lau, gio_bat_dau, gio_ket_thuc, thu):
    query = LopHoc.query.join(PhongHoc, LopHoc.phong_hoc_id.__eq__(PhongHoc.id)) \
        .join(CaHoc, LopHoc.ca_id.__eq__(CaHoc.id)) \
        .filter(PhongHoc.ten_phong.startswith(so_lau)
                , or_(and_(CaHoc.gio_bat_dau.__eq__(gio_bat_dau), CaHoc.gio_ket_thuc.__le__(gio_ket_thuc))
                      , and_(CaHoc.gio_bat_dau.__eq__(gio_bat_dau), CaHoc.gio_ket_thuc.__ge__(gio_ket_thuc))
                      , and_(CaHoc.gio_ket_thuc.__eq__(gio_ket_thuc), CaHoc.gio_bat_dau.__le__(gio_bat_dau))
                      , and_(CaHoc.gio_ket_thuc.__eq__(gio_ket_thuc), CaHoc.gio_bat_dau.__ge__(gio_bat_dau))
                      , and_(CaHoc.gio_bat_dau.__le__(gio_bat_dau), CaHoc.gio_ket_thuc.__ge__(gio_ket_thuc)))
                , LopHoc.thu_trong_tuan.__eq__(thu))
    return query.all()


def save_room(request):
    print(request)
    phieu_muon_phong = PhieuMuonPhong(tai_khoan_id=int(request['tai_khoan_id']),
                                      ly_do=request['ly_do'],
                                      ca_id=int(request['ca_hoc_id']),
                                      phong_hoc_id=get_phong_hoc_by_name(request['ten_phong']).id,
                                      ngay_muon=datetime.strptime(request['ngay_muon'], "%Y-%m-%d"),
                                      thoi_gian_dat=datetime.now(),
                                      trang_thai="DANG_CHO_DUYET")
    # print(phieu_muon_phong)
    
    db.session.add(phieu_muon_phong)
    result=True
    try:
        db.session.commit()
    except Exception as e:
        db.session.flush()
        result=False
    return result


def get_phong_hoc_by_name(ten_phong):
    return PhongHoc.query.filter(PhongHoc.ten_phong.contains(ten_phong)).first()


def get_phieu_muon(so_lau, gio_bat_dau, gio_ket_thuc, ngay_muon):
    query = PhieuMuonPhong.query.join(PhongHoc, PhieuMuonPhong.phong_hoc_id.__eq__(PhongHoc.id)) \
        .join(CaHoc, PhieuMuonPhong.ca_id.__eq__(CaHoc.id)) \
        .filter(PhongHoc.ten_phong.startswith(so_lau)
                , or_(and_(CaHoc.gio_bat_dau.__eq__(gio_bat_dau), CaHoc.gio_ket_thuc.__le__(gio_ket_thuc))
                      , and_(CaHoc.gio_bat_dau.__eq__(gio_bat_dau), CaHoc.gio_ket_thuc.__ge__(gio_ket_thuc))
                      , and_(CaHoc.gio_ket_thuc.__eq__(gio_ket_thuc), CaHoc.gio_bat_dau.__le__(gio_bat_dau))
                      , and_(CaHoc.gio_ket_thuc.__eq__(gio_ket_thuc), CaHoc.gio_bat_dau.__ge__(gio_bat_dau))
                      , and_(CaHoc.gio_bat_dau.__le__(gio_bat_dau), CaHoc.gio_ket_thuc.__ge__(gio_ket_thuc)))
                , PhieuMuonPhong.ngay_muon.__eq__(ngay_muon), PhieuMuonPhong.trang_thai.__ne__("TU_CHOI"))
    return query.all()


def get_phieu_muon_theo_trang_thai(ma_tai_khoan, trangthai):
    query = db.session.query(TaiKhoan.ho_ten, TaiKhoan.dai_dien_to_chuc, TaiKhoan.mssv, TaiKhoan.so_dien_thoai,
                             PhongHoc.ten_phong, CaHoc.gio_bat_dau, CaHoc.gio_ket_thuc,
                             PhieuMuonPhong.ngay_muon, PhieuMuonPhong.ly_do, PhieuMuonPhong.thoi_gian_dat,
                             PhieuMuonPhong.id) \
        .join(TaiKhoan, TaiKhoan.id.__eq__(PhieuMuonPhong.tai_khoan_id)) \
        .join(PhongHoc, PhongHoc.id.__eq__(PhieuMuonPhong.phong_hoc_id)) \
        .join(CaHoc, CaHoc.id.__eq__(PhieuMuonPhong.ca_id)) \
        .filter(PhieuMuonPhong.tai_khoan_id.__eq__(ma_tai_khoan), PhieuMuonPhong.trang_thai.__eq__(trangthai))
    return query.all()


