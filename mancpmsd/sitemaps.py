from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['doctors', 'units', 'freedrugs']

    def location(self, item):
        return reverse(item)
