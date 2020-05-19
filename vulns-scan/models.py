from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class VulnScanModel(models.Model):
    SITE_SCAN = 'Сканирование сетки'
    DIRECTORY_BRUTEFORCE = 'Брут  директорий'
    DOS_ATTACK = 'DOS атака'
    VULNERABILITY_SCAN = 'Сканирование на уязвимости'

    SCAN_TYPE = (
        ('', 'Вектор атаки'),
        (SITE_SCAN, 'Сканирование сетки'),
        (DIRECTORY_BRUTEFORCE, 'Брут  директорий'),
        (DOS_ATTACK, 'DOS атака'),
        (VULNERABILITY_SCAN, 'Сканирование на уязвимости')
    )

    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', )
    name = models.CharField(max_length=250, blank=True, unique=True, verbose_name='название теста')
    site_ip = models.CharField(max_length=32, blank=True, verbose_name='ip сайта')
    scan_type = models.CharField(choices=SCAN_TYPE, max_length=250, blank=True, verbose_name='вектор атаки')

    city = models.CharField(max_length=250, blank=True, verbose_name='город')
    vulns = models.TextField(blank=True, verbose_name='Уязвимости')

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
        return reverse('vulns-scan-result', kwargs={'slug':self.slug})