import os
import time
import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """PostgreSQL database connectionni kutish"""

    def handle(self, *args, **options):
        self.stdout.write('PostgreSQLga ulanishni tekshirilmoqda...')
        max_retries = 30
        retry_delay = 1

        for _ in range(max_retries):
            try:
                conn = psycopg2.connect(
                    dbname=os.getenv('POSTGRES_DB'),
                    user=os.getenv('POSTGRES_USER'),
                    password=os.getenv('POSTGRES_PASSWORD'),
                    host=os.getenv('POSTGRES_HOST'),
                    port=os.getenv('POSTGRES_PORT')
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS('PostgreSQLga ulanish muvaffaqiyatli!'))
                return
            except psycopg2.OperationalError:
                self.stdout.write('PostgreSQL hali tayyor emas, qayta urinilmoqda...')
                time.sleep(retry_delay)

        self.stdout.write(self.style.ERROR('PostgreSQLga ulanish muvaffaqiyatsiz!'))
        exit(1)