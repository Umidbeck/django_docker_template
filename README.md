📦 Loyihani O'rnatish
Dasturiy Ta'minot Talablari
Docker (20.10.17+)

Docker Compose (2.10.2+)

Git (optional)

1. Loyihani Clone Qilish
bash
git clone https://github.com/sizning-repo/django-docker-template.git myproject
cd myproject
2. Muhit Sozlamalari
bash
cp .env.example .env
.env faylini tahrirlang (kamida quyidagilarni yangilang):

ini
DJANGO_SECRET_KEY=your-secret-key-here
POSTGRES_PASSWORD=your-strong-password
🚀 Ishga Tushirish
1. Konteynerlarni Yaratish va Ishga Tushirish
bash
docker-compose up -d --build
2. Dasturni Dastlabki Sozlash
bash
# Ma'lumotlar bazasi migratsiyalari
docker-compose exec web python manage.py migrate

# Admin paneli uchun superuser yaratish
docker-compose exec web python manage.py createsuperuser
3. Statik Fayllarni Yig'ish (Agar kerak bo'lsa)
bash
docker-compose exec web python manage.py collectstatic --noinput
🌐 Dasturga Kirish
Asosiy sahifa: http://localhost:8000

Admin paneli: http://localhost:8000/admin

