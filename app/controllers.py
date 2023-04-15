from datetime import date, timedelta
from app import dao
from flask import render_template, redirect, jsonify
from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from app.decorator import annonymous_user
from datetime import datetime


# 24h url
def home():
    return render_template('index.html')


# login người dùng
@annonymous_user
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form['uname']
        password = request.form['pwd']
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            n = request.args.get("next")
            return redirect(n if n else '/')
    return render_template('login.html')


# logout
@login_required
def logout_my_user():
    logout_user()
    return redirect('/')


@login_required
def book_room():
    list_ca_hoc = dao.load_ca_hoc()
    floor = request.args.get('select_floor')
    if floor is None:
        floor = 1
    list_phong_hoc = dao.load_room(so_lau=floor)
    if (len(list_phong_hoc) % 2) != 0:
        half_phong_hoc = int(len(list_phong_hoc) / 2) + 1
    else:
        half_phong_hoc = int(len(list_phong_hoc) / 2)
    ca = request.args.get('select-ca-hoc')
    if ca is None:
        ca = 1
    else:
        ca = int(ca)

    date_book = request.args.get('date-book')
    if date_book is None:
        date_book = date.today() + timedelta(days=1)
    else:
        date_book = datetime.strptime(date_book, "%Y-%m-%d").date()
    ca_hoc = dao.get_ca_hoc(ca_hoc_id=ca)
    day_of_week = date_book.strftime('%a').upper()
    lich_hoc = dao.get_lich_hoc(so_lau=floor, gio_bat_dau=ca_hoc.gio_bat_dau,
                                gio_ket_thuc=ca_hoc.gio_ket_thuc, thu=day_of_week)
    phieu_muon_phong = dao.get_phieu_muon(so_lau=floor, gio_bat_dau=ca_hoc.gio_bat_dau,
                                gio_ket_thuc=ca_hoc.gio_ket_thuc, ngay_muon=date_book)
    tag_list = dao.get_tag()
    return render_template('book_room.html', list_ca_hoc=list_ca_hoc, list_phong_hoc=list_phong_hoc,
                           max_phong_hoc=len(list_phong_hoc), half_phong_hoc=half_phong_hoc, tag_list=tag_list,
                           floor=floor, ca=ca, ngay_dat=date_book, lich_hoc=lich_hoc, phieu_muon_phong=phieu_muon_phong)


def get_ca_hoc(ca_hoc_id):
    ca_hoc = dao.get_ca_hoc(ca_hoc_id=ca_hoc_id)
    return jsonify({
        "gio_bat_dau": ca_hoc.gio_bat_dau.strftime("%H:%M"),
        "gio_ket_thuc": ca_hoc.gio_ket_thuc.strftime("%H:%M")
    })


def save_book_room():
    # print(request.json['ngay_muon'])
    if request.json['ten_phong']:
        if dao.save_room(request.json):
            return jsonify({
                "status": 200
            })
    return jsonify({
        'status': 500
    })


@login_required
def xem_phieu_muon():
    phieu_cho_duyet = dao.get_phieu_muon_theo_trang_thai(current_user.id, "DANG_CHO_DUYET")
    phieu_cho_duyet = sorted(phieu_cho_duyet, key=lambda x: x[9], reverse=True)
    phieu_tu_choi = dao.get_phieu_muon_theo_trang_thai(current_user.id, "TU_CHOI")
    phieu_tu_choi = sorted(phieu_tu_choi, key=lambda x: x[9], reverse=True)
    phieu_san_sang = dao.get_phieu_muon_theo_trang_thai(current_user.id, "SAN_SANG")
    phieu_san_sang = sorted(phieu_san_sang, key=lambda x: x[9], reverse=True)
    phieu_thanh_cong = dao.get_phieu_muon_theo_trang_thai(current_user.id, "THANH_CONG")
    phieu_thanh_cong = sorted(phieu_thanh_cong, key=lambda x: x[9], reverse=True)
    return render_template('coupon_view.html', phieu_cho_duyet=phieu_cho_duyet, phieu_tu_choi=phieu_tu_choi,
                           phieu_san_sang=phieu_san_sang, phieu_thanh_cong=phieu_thanh_cong)