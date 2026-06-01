"""
Boshlang'ich ma'lumotlarni yuklash buyrug'i.

Ishlatish:
    python manage.py load_data
"""

from django.core.management.base import BaseCommand
from main.models import Muallif, Kitob


class Command(BaseCommand):
    help = "Kutubxona uchun boshlang'ich ma'lumotlarni yuklaydi"

    def handle(self, *args, **kwargs):
        self.stdout.write("Eski ma'lumotlar o'chirilmoqda...")
        Kitob.objects.all().delete()
        Muallif.objects.all().delete()

        # Mualliflar
        self.stdout.write("Mualliflar qo'shilmoqda...")
        qodiriy = Muallif.objects.create(
            ism_familiya='Abdulla Qodiriy',
            tugilgan_yili=1894,
            shahar='Toshkent',
            bio="O'zbek adabiyotining yirik vakili, romanchi va publitsist."
        )
        cholpon = Muallif.objects.create(
            ism_familiya="Cho'lpon",
            tugilgan_yili=1897,
            shahar='Andijon',
            bio="Atoqli shoir, dramaturg va tarjimon."
        )
        oybek = Muallif.objects.create(
            ism_familiya='Oybek',
            tugilgan_yili=1905,
            shahar='Toshkent',
            bio="Yozuvchi, shoir, adabiyotshunos."
        )

        # Kitoblar
        self.stdout.write("Kitoblar qo'shilmoqda...")
        Kitob.objects.create(nom="O'tkan kunlar", muallif=qodiriy, yil=1925, narx=50000)
        Kitob.objects.create(nom='Mehrobdan chayon', muallif=qodiriy, yil=1929, narx=45000)
        Kitob.objects.create(nom='Sarob', muallif=qodiriy, yil=1934, narx=40000)
        Kitob.objects.create(nom='Kecha va kunduz', muallif=cholpon, yil=1936, narx=55000)
        Kitob.objects.create(nom='Navoiy', muallif=oybek, yil=1944, narx=60000, mavjud=False)
        Kitob.objects.create(nom="Qutlug' qon", muallif=oybek, yil=1940, narx=35000)

        self.stdout.write(self.style.SUCCESS(
            f"\nMuvaffaqiyatli yuklandi!\n"
            f"  Mualliflar: {Muallif.objects.count()} ta\n"
            f"  Kitoblar:   {Kitob.objects.count()} ta"
        ))
