from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return [
            "home",
            "shop",
            "about",
            "legal",
        ]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated