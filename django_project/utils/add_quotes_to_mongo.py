import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb+srv://clemontine839:Xzvv9843@cluster0.2lkwevd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.hw9

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })