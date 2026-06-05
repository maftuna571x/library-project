"""
================================================================
  64-DARS UY VAZIFASI — Templates va render()
================================================================
       
KO'RSATMA:
Har bir topshiriq uchun:
  1. NAMUNAga qarang
  2. View funksiyasini yozing (shu faylda)
  3. Template faylni yarating (main/templates/main/ ichida)
  4. Brauzerda tegishli URL ni oching va natijani ko'ring

Loyihani ishga tushirish:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py load_data
    python manage.py runserver

Keyin brauzerda oching: http://127.0.0.1:8000/
"""

from django.shortcuts import render, get_object_or_404
from .models import Muallif, Kitob


# ================================================================
#   1-TOPSHIRIQ.  Bosh sahifa
# ================================================================
#
# Vazifa:
#   "main/bosh_sahifa.html" template'ini yarating va shu sahifada
#   <h1> tegi bilan "Kutubxonaga xush kelibsiz!" deb yozing.
#   Shu funksiya bosh sahifani ko'rsatadi.
#
# NAMUNA — eng oddiy render():
#   def salom_view(request):
#       return render(request, 'main/salom.html')
#
# URL: http://127.0.0.1:8000/

def bosh_sahifa(request):
      return render(request, 'main/bosh_sahifa.html')


# ================================================================
#   2-TOPSHIRIQ.  Context bilan ma'lumot uzatish (string)
# ================================================================
#
# Vazifa:
#   "main/salom.html" template'ini yarating. View'dan template'ga
#   'ism' o'zgaruvchisini uzating (qiymati: 'Ali').
#   Template'da: <h1>Salom, {{ ism }}!</h1> yozing.
#
# NAMUNA:
#   def salom_view(request):
#       kontekst = {'ism': 'Hasan'}
#       return render(request, 'main/salom.html', kontekst)
#
# URL: http://127.0.0.1:8000/salom/

def salom(request):
    kontekst = {'ism': 'Ali'}
    return render(request, 'main/salom.html', kontekst)



# ================================================================
#   3-TOPSHIRIQ.  Obyektni context'da uzatish (nuqta orqali murojaat)
# ================================================================
#
# Vazifa:
#   DB dan birinchi muallifni oling va template'ga uzating.
#   "main/muallif.html" da uning ma'lumotlarini chiqaring:
#     - {{ muallif.ism_familiya }}
#     - {{ muallif.tugilgan_yili }}
#     - {{ muallif.shahar }}
#
# NAMUNA:
#   def kitob_view(request):
#       kitob = Kitob.objects.first()
#       return render(request, 'main/kitob.html', {'kitob': kitob})
#
# URL: http://127.0.0.1:8000/muallif/

def muallif_view(request):
    muallif = Muallif.objects.first()
    return render(request, 'main/muallif.html', {'muallif': muallif})


# ================================================================
#   4-TOPSHIRIQ.  Ro'yxat ({% for %} bilan)
# ================================================================
#
# Vazifa:
#   Barcha kitoblarni DB dan oling va "main/kitoblar.html" da
#   {% for %} sikli orqali har birini <li> tegi bilan chiqaring.
#   Agar kitoblar yo'q bo'lsa, {% empty %} blokida xabar chiqaring.
#
# NAMUNA — view:
#   def mualliflar_view(request):
#       mualliflar = Muallif.objects.all()
#       return render(request, 'main/mualliflar.html',
#                     {'mualliflar': mualliflar})
#
# NAMUNA — template:
#   <ul>
#     {% for m in mualliflar %}
#       <li>{{ m.ism_familiya }}</li>
#     {% empty %}
#       <li>Mualliflar yo'q</li>
#     {% endfor %}
#   </ul>
#
# URL: http://127.0.0.1:8000/kitoblar/


def kitoblar_royxati(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'main/kitoblar.html', {'kitoblar': kitoblar}) 


# ================================================================
#   5-TOPSHIRIQ.  Filtrlar bilan ishlash
# ================================================================
#
# Vazifa:
#   "main/filtrlar.html" template'ida quyidagi filtrlarni
#   ishlatib ko'rsating:
#     - {{ matn|upper }}       — katta harf
#     - {{ matn|lower }}       — kichik harf
#     - {{ matn|title }}       — har so'z birinchi harfi katta
#     - {{ matn|length }}      — uzunligi
#     - {{ son|add:10 }}       — qo'shish
#     - {{ ism|default:"Mehmon" }} — qiymat yo'q bo'lsa
#
#   View'dan template'ga uzating:
#     matn = 'salom dunyo'
#     son = 5
#     ism = ''
#
# NAMUNA:
#   def filter_test(request):
#       return render(request, 'main/test.html', {
#           'narx': 50000,
#           'sana': datetime.now()
#       })
#
# URL: http://127.0.0.1:8000/filtrlar/

def filtrlar(request):
    return render(request, 'main/filtrlar.html', {
        'matn': 'salom dunyo',
        'son': 5,
        'ism': ''
    })


# ================================================================
#   6-TOPSHIRIQ.  {% if %} va {% for %} birga
# ================================================================
#
# Vazifa:
#   Barcha kitoblarni oling. "main/shartlar.html" da {% for %}
#   bilan ro'yxatda chiqaring, lekin har bir kitob uchun:
#     {% if kitob.mavjud %}
#       — yashil rangda chiqaring (style="color: green")
#     {% else %}
#       — qizil rangda "Mavjud emas" deb yozing
#     {% endif %}
#
# NAMUNA — template:
#   {% for k in kitoblar %}  
#     {% if k.narx > 50000 %}
#       <p style="color: red">{{ k.nom }} — qimmat</p>
#     {% else %}
#       <p style="color: green">{{ k.nom }} — arzon</p>
#     {% endif %}
#   {% endfor %}
#
# URL: http://127.0.0.1:8000/shartlar/

def shartlar(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'main/shartlar.html', {
        'kitoblar': kitoblar
    })


# ================================================================
#   7-TOPSHIRIQ.  URL parametri va {% url %} tegi
# ================================================================
#
# Vazifa:
#   muallif_id URL'dan keladi. Shu ID bo'yicha muallifni DB dan
#   oling (get_object_or_404 ishlatish tavsiya etiladi).
#   "main/muallif_detail.html" da:
#     - Muallifning ma'lumotlarini chiqaring
#     - Uning kitoblarini ro'yxat qilib chiqaring
#       ({{ muallif.kitoblari.all }} — related_name orqali)
#
# NAMUNA:
#   def kitob_detail(request, kitob_id):
#       kitob = get_object_or_404(Kitob, pk=kitob_id)
#       return render(request, 'main/detail.html', {'kitob': kitob})
#
# URL: http://127.0.0.1:8000/muallif/1/

def muallif_detail(request, muallif_id):
    muallif = get_object_or_404(Muallif, pk=muallif_id)

    return render(request, 'main/muallif_detail.html', {
        'muallif': muallif
    })


# ================================================================
#   8-TOPSHIRIQ.  {% url %} tegi bilan navigatsiya
# ================================================================
#
# Vazifa:
#   kitob_id bo'yicha kitobni oling.
#   "main/kitob_detail.html" da:
#     - Kitob ma'lumotlarini ko'rsating
#     - {% url %} tegi bilan muallif sahifasiga link bering:
#       <a href="{% url 'muallif_detail' kitob.muallif.id %}">
#         {{ kitob.muallif.ism_familiya }}
#       </a>
#     - Bosh sahifaga "Orqaga" tugmasini qo'shing
#
# NAMUNA — template:
#   <a href="{% url 'bosh_sahifa' %}">Bosh sahifaga qaytish</a>
#
# URL: http://127.0.0.1:8000/kitob/1/

def kitob_detail(request, kitob_id):
    kitob = get_object_or_404(Kitob, pk=kitob_id)

    return render(request, 'main/kitob_detail.html', {
        'kitob': kitob
    })


# ================================================================
#   9-TOPSHIRIQ.  {% static %} tegi (statik fayllar)
# ================================================================
#
# Vazifa:
#   "main/static_test.html" template'ini yarating.
#   Eng yuqorida {% load static %} yozing.
#   Keyin bunday qator qo'shing:
#       <link rel="stylesheet" href="{% static 'main/style.css' %}">
#
#   main/static/main/style.css fayli allaqachon yaratilgan.
#   Sahifada {{ sarlavha }} ni <h1> bilan chiqaring va CSS
#   ishlayotganini tekshiring (yashil rangda chiqishi kerak).
#
# NAMUNA — template:
#   {% load static %}
#   <link rel="stylesheet" href="{% static 'main/style.css' %}">
#
# URL: http://127.0.0.1:8000/static-test/

def static_test(request):
    return render(request, 'main/static_test.html', {
        'sarlavha': 'Static test sahifasi'
    })




# ================================================================
#  10-TOPSHIRIQ.  {% extends %} va {% block %} (DRY printsipi)
# ================================================================
#
# Vazifa:
#   3 ta template yarating:
#
#   1. main/base.html  — bazaviy shablon. Unda:
#      - <title>{% block sarlavha %}Kutubxona{% endblock %}</title>
#      - <nav> ichida link'lar: Bosh sahifa, Haqida
#      - <main>{% block kontent %}{% endblock %}</main>
#      - <footer> ichida © 2026
#
#   2. main/home.html — base.html dan meros oladi.
#      {% extends 'main/base.html' %}
#      {% block sarlavha %}Bosh sahifa{% endblock %}
#      {% block kontent %}
#          <h1>Kutubxonaga xush kelibsiz!</h1>
#      {% endblock %}
#
#   3. main/haqida.html — xuddi shunday, lekin "Biz haqimizda"
#      matni bilan.
#
# Quyidagi 2 ta view tayyor — siz faqat template'larni yarating.
#
# URL: http://127.0.0.1:8000/home/
# URL: http://127.0.0.1:8000/haqida/

def home_page(request):
    return render(request, 'main/home.html')


def haqida_page(request):
    return render(request, 'main/haqida.html')
