import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServiceProject.settings')
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
with open('user_report.txt', 'w') as f:
    for user in users:
        f.write(f"Username: '{user.username}', Email: '{user.email}', is_superuser: {user.is_superuser}, is_staff: {user.is_staff}, last_name: '{user.last_name}'\n")
