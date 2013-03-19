from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest

from pystoruman.settings import BOT_NAME, STORUMAN_USER, STORUMAN_PASSWORD
from pystoruman.items import StorumanItem

class StorumanSpider(BaseSpider):
    name = BOT_NAME
    start_urls = [
            "https://minasidor.storumanenergi.se/Login.aspx?ReturnUrl=%2fInvoices.aspx",
    ]
    # ASP.NET and the "___doPostBack()" nonsense
    # http://doc.scrapy.org/en/latest/faq.html#what-s-this-huge-cryptic-viewstate-parameter-used-in-some-forms
    def parse(self, response):
        return [FormRequest.from_response(
                    response,
                    formdata={'ctl00$MainContent$LoginUser$UserName': STORUMAN_USER,
                              'ctl00$MainContent$LoginUser$Password': STORUMAN_PASSWORD,
                              '__EVENTTARGET': 'ctl00$MainContent$LoginUser$LoginButton'},
                    callback=self.parse_invoices,
                )]

    def parse_invoices(self, response):
        hxs = HtmlXPathSelector(response)
        items = []

        # XXX: no pagination implemented, only last 9 invoices available
        for invoice in range(2, 11):
            item = StorumanItem()

            item['invoice_nr'] = hxs.select("//*[@id=\"ctl00_MainContent_InvoiceGrid_ctrl{inv}_InvoicePDF\"]/text()".format(inv=invoice-2)).extract()[0]
            item['date'] = hxs.select("//*[@id='invoices']/div[{inv}]/div[3]/text()".format(inv=invoice)).extract()[0]
            item['amount'] = hxs.select("//*[@id='invoices']/div[{inv}]/div[4]/text()".format(inv=invoice)).extract()[0]
            item['paid'] = hxs.select("//*[@id='invoices']/div[{inv}]/div[5]/text()".format(inv=invoice)).extract()[0]

            items.append(item)
        return items
