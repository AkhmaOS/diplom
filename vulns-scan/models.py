from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class VulnScanModel(models.Model):
    # auto
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', )
    # get from users
    name = models.CharField('Название', max_length=250, blank=True, unique=True)
    site_ip = models.CharField('IP-адрес', max_length=32, blank=True)

    # nullable data  \ callback shodan
    city = models.CharField('city', max_length=250, blank=True, null=True, default=None)
    cve = models.ForeignKey('CveScanModel', on_delete=models.CASCADE, null=True, default=None)
    site_title = models.CharField('title', blank=True, null=True, default=None, max_length=250)
    robots = models.CharField('robots.txt', blank=True, null=True, default=None, max_length=250)
    org = models.CharField('domain org', blank=True, null=True, default=None, max_length=250)
    ports = models.CharField('ports', blank=True, null=True, default=None, max_length=250)
    country_name = models.CharField('Страна', default=None, null=True, blank=True, max_length=250)

    class Meta:
        verbose_name = 'Vuln Scan'
        verbose_name_plural = 'Vulns Scans'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vulns-scan-result', kwargs={'slug': self.slug})


class CveScanModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    cve = models.CharField('vuln name', null=True, default=None, blank=True, max_length=250)
    verified = models.BooleanField('подтверждение', default=False, blank=True)

    def __str__(self):
        return self.cve