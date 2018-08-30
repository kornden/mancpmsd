from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sites.models import Site

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='mankivkacpmsd.us.to', name='mankivkacpmsd.us.to')
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['doctors', 'units', 'freedrugs']

    def location(self, item):
        return reverse(item)