# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymongo


class MongoDBPipeline(object):
    collection_name = 'scrapy_items'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            "mongodb+srv://christoloisel:Rose230323@cluster0.soahdz4.mongodb.net/")
        self.db = self.client["pipeliner"]  # Nom de votre base de données

    def close_spider(self, spider):
        # Fermeture de la connexion à la fin du spider
        self.client.close()

    def process_item(self, item, spider):
        # Insertion de l'item dans la collection MongoDB
        self.db[self.collection_name].insert_one(dict(item))
        return item
