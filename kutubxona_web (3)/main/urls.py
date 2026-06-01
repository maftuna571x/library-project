"""
main app URL'lari.

Har bir topshiriq uchun alohida URL bor. Talaba brauzerda ochib
natijani ko'rishi mumkin.

URL'lar:
    /                    — Bosh sahifa (1-topshiriq)
    /salom/              — 2-topshiriq
    /muallif/            — 3-topshiriq
    /kitoblar/           — 4-topshiriq
    /filtrlar/           — 5-topshiriq
    /shartlar/           — 6-topshiriq
    /muallif/<id>/       — 7-topshiriq
    /kitob/<id>/         — 8-topshiriq
    /static-test/        — 9-topshiriq
    /home/               — 10-topshiriq (extends bilan)
    /haqida/             — 10-topshiriq (extends bilan)
"""

from django.urls import path
from . import views

urlpatterns = [
    # 1-topshiriq: Bosh sahifa
    path('', views.bosh_sahifa, name='bosh_sahifa'),

    # 2-topshiriq: Salom sahifasi
    path('salom/', views.salom, name='salom'),

    # 3-topshiriq: Muallif obyekti
    path('muallif/', views.muallif_view, name='muallif'),

    # 4-topshiriq: Kitoblar ro'yxati
    path('kitoblar/', views.kitoblar_royxati, name='kitoblar'),

    # 5-topshiriq: Filtrlar
    path('filtrlar/', views.filtrlar, name='filtrlar'),

    # 6-topshiriq: if/for shartlar
    path('shartlar/', views.shartlar, name='shartlar'),

    # 7-topshiriq: Muallif detali
    path('muallif/<int:muallif_id>/', views.muallif_detail, name='muallif_detail'),

    # 8-topshiriq: Kitob detali
    path('kitob/<int:kitob_id>/', views.kitob_detail, name='kitob_detail'),

    # 9-topshiriq: Static fayllar bilan ishlash
    path('static-test/', views.static_test, name='static_test'),

    # 10-topshiriq: Extends bilan
    path('home/', views.home_page, name='home'),
    path('haqida/', views.haqida_page, name='haqida'),
]
