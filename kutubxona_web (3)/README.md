# Django Templates va render() — Uy vazifasi

IT Shaharcha o'quv markazi • Django darslari • 64-dars

## Loyiha tuzilishi

```
kutubxona_web/
├── config/                      # Django proyekt sozlamalari
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                        # Asosiy app
│   ├── models.py                # Muallif, Kitob modellari
│   ├── views.py                 # ← VIEW FUNKSIYALARNI SHU YERGA YOZASIZ
│   ├── urls.py                  # URL'lar (tayyor)
│   ├── templates/main/          # ← TEMPLATE FAYLLARNI SHU YERGA YOZASIZ
│   ├── static/main/style.css    # CSS (9-topshiriq uchun tayyor)
│   └── management/commands/
│       └── load_data.py         # Boshlang'ich ma'lumotlar
├── manage.py
├── savollar.txt                 # ← Nazariy savollar
├── topshiriqlar.txt             # ← Amaliy topshiriqlar (o'qish uchun)
└── requirements.txt
```

## Boshlash

### 1. Virtual muhit va Django

```bash
# Virtual muhit yarating va faollashtiring
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Django'ni o'rnating
pip install -r requirements.txt
```

### 2. Ma'lumotlar bazasini tayyorlash

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py load_data
```

### 3. Saytni ishga tushirish

```bash
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000/**

## Vazifa qanday bajariladi

Har topshiriq uchun 2 ta narsa qilish kerak:

1. **`main/views.py`** — view funksiyasini yozing (har topshiriq uchun namuna izoh sifatida bor)
2. **`main/templates/main/`** — template fayl yarating

URL'lar `main/urls.py` da tayyor. Talaba faqat view va template'ni yozadi.
 
## Topshiriqlar URL'lari

| Topshiriq | URL |
|-----------|-----|
| 1. Bosh sahifa | `/` |
| 2. Salom (context) | `/salom/` |
| 3. Muallif obyekti | `/muallif/` |
| 4. Kitoblar ro'yxati | `/kitoblar/` |
| 5. Filtrlar | `/filtrlar/` |
| 6. {% if %} shartlar | `/shartlar/` |
| 7. Muallif detali | `/muallif/1/` |
| 8. Kitob detali | `/kitob/1/` |
| 9. CSS bilan | `/static-test/` |
| 10. Extends | `/home/` va `/haqida/` |

## Qo'shimcha topshiriq: `base.html` navbar

`main/templates/main/base.html` fayli tayyor qoldirilgan, lekin uning
ichidagi `<nav>` (navbar) **bo'sh**. Uni o'zingiz to'ldirishingiz kerak:

1. `base.html` ni oching va `<nav>` blokini toping.
2. Komment (`{# ... #}`) ko'rinishidagi ko'rsatmaga qarang.
3. Navbarga `{% url %}` tegi bilan link'lar qo'shing, masalan:

   ```django
   <a href="{% url 'bosh_sahifa' %}">Bosh sahifa</a>
   <a href="{% url 'haqida' %}">Haqida</a>
   ```

4. `http://127.0.0.1:8000/home/` ni oching — navbar har bir sahifada
   ko'rinishi kerak (chunki barcha sahifalar `base.html` dan meros oladi).

> Eslatma: navbar `base.html` da bir marta yoziladi, lekin
> `{% extends %}` tufayli barcha sahifalarda avtomatik chiqadi (DRY).

## Topshirish

1. Barcha 10 ta topshiriqni bajaring
2. Har URL'ni brauzerda tekshiring
3. `savollar.txt` ga javoblarni yozing
4. GitHub'ga yuklang
5. Link'ni o'qituvchiga yuboring

## Maslahat

- View'ni yozdingizmi — brauzerda darhol tekshiring
- Xato chiqsa — Django sahifasidagi xato matnini diqqat bilan o'qing
- Template'da {% tag %} larni yopishni unutmang ({% endif %}, {% endfor %})
