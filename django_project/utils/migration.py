import os
import django
from django_project.quotes.models import Quote, Tag, Author
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

client = MongoClient('mongodb+srv://clemontine839:Xzvv9843@cluster0.2lkwevd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.hw9

author = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description'],
    )
