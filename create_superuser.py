import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
django.setup()

User = get_user_model()
if not User.objects.filter(username=os.environ['SUPERUSER_NAME']).exists():
    User.objects.create_superuser(
        username=os.environ['SUPERUSER_NAME'],
        email=os.environ['SUPERUSER_EMAIL'],
        password=os.environ['SUPERUSER_PASSWORD']
    )
