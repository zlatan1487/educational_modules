from django import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='karp.zidan@mail.ru',
            first_name='Vitaliy',
            last_name='Karpukhin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('1989')
        user.save()
