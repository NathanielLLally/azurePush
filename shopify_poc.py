#!/usr/bin/python













import shopify
import math

def do_stats(x,y):
        someValue = math.sqrt(x * x + y * y)
        return someValue

shop_url = "https://28cc767c61f1793e997fa6e67ab1367f:d062fa857a778c74fdac279d6fce20ec@two-birds-on-mulberry-street.myshopify.com/admin"
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current
product = shopify.Product.find(8161496645)
print(product.title)
order = shopify.Order.find(4656551237)
print("name:%s\ttotal_price:%s\n" % (order.name, order.total_price))

print(do_stats(float(order.total_price), 42))


