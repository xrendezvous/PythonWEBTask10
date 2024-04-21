from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        'mongodb+srv://clemontine839:Xzvv9843@cluster0.2lkwevd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    db = client.hw9
    return db

