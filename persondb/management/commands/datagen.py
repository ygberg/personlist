from django.core.management.base import BaseCommand,CommandError
from faker import Faker
from persondb.models import Person

class Command(BaseCommand):
    help = 'fake data for databse'

    def handle(self, *args, **options):
        fake = Faker()
        for i in range (10):
            name = fake.first_name()
            last = fake.last_name()
            mail = fake.email()
            Person.objects.get_or_create(first_name = name,last_name=last,email=mail)
            print(Person.objects.all())


print(Person.objects.all())
print()