import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@velvetcreature.fr", "TvojeHeslo123")
    print("ADMIN CREATED!")
else:
    print("Admin already exists")