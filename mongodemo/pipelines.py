import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MongodemoPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGO_URI']
        )
        db = connection[settings['MONGO_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # col = item['db']
            # self.db[col].insert(dict(item))
            _id=self.collection.insert(dict(item))
            log.msg(_id)
            val=str(_id)
            f = open("output.text", "a+")
            f.write(val)
            f.write(",")
            log.msg("Data added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item