pystoruman
==========

<a href="http://scrapy.org/">Scrapy</a> web crawler to fetch invoices from the
electrical company <a href="http://www.storumanenergi.se/">storuman</a>.

Quick start
===========

```
pip install scrapy && git clone https://github.com/brainstorm/pystoruman && cd pystoruman
```

Edit `settings.py` and edit `STORUMAN_USER` and `STORUMAN_PASSWORD`.

```
$ scrapy crawl storuman.se -o items.json -t json
(...)

$ cat items.json
[   {'amount': u'106,00',
     'date': u'2013-03-31',
     'invoice_nr': u'666623888',
     'paid': u'106,00'}
]
```
