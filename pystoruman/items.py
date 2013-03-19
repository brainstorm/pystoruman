# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class StorumanItem(Item):
    invoice_nr = Field()
    date = Field()
    amount = Field()
    paid = Field()
