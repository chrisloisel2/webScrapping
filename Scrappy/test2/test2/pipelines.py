# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# Import de mongo
import pymongo


class Test2Pipeline:

    def open_spider(self, spider):
        print("Open Spider")
        self.client = pymongo.MongoClient(
            "mongodb+srv://christoloisel:Rose230323@cluster0.soahdz4.mongodb.net/")
        self.db = self.client["yolotest"]  # Nom de votre base de données

    def process_item(self, item, spider):
        print("Pipeline: ", item)
        # placer ma collection dans la base de données
        self.db["test2"].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        print("Close Spider")
        # Fermeture de la connexion à la fin du spider
        self.client.close()
