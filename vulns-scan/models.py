from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class VulnScanModel(models.Model):
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', )
    name = models.CharField('Название', max_length=250, blank=True, unique=True)
    site_ip = models.CharField('IP-адрес', max_length=32, blank=True)

    # nullable data
    city = models.CharField('city', max_length=250, blank=True, null=True, default=None)
    vulns = models.TextField('Уязвимости', blank=True, null=True, default=None)

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
