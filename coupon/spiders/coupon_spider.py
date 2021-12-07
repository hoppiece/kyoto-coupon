import scrapy

from coupon.items import CouponItem


class CouponSpiderSpider(scrapy.Spider):
    name = "coupon_spider"

    def start_requests(self):
        for i in range(1, 250):
            url = f"https://premium-gift.jp/allkyoto/use_store?events=page&id={i}&store=&addr=&industry="
            yield scrapy.Request(url)

    def parse(self, response):
        cards = response.xpath("//div[@class='store-card__item']")
        for c in cards:
            name = c.xpath("*[@class='store-card__title']/text()").get()
            tag = c.xpath("*[@class='store-card__tag']/text()").get()
            address = c.xpath(
                "*[@class='store-card__table']/tbody/tr[1]/td/text()"
            ).get()
            tel = c.xpath("*[@class='store-card__table']/tbody/tr[2]/td/text()").get()
            url = c.xpath("*[@class='store-card__table']/tbody/tr[3]/td/a/text()").get()
            yield CouponItem(name=name, tag=tag, address=address, tel=tel, url=url)
